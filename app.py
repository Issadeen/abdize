from flask import Flask, request, jsonify
import os
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_validator import validate_email, EmailNotValidError
from dotenv import load_dotenv
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Load environment variables
load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))  # Convert to integer with default value
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
FROM_EMAIL = os.getenv("FROM_EMAIL")

# Remove the WEBSITE_HOSTNAME block and replace with:
APPLICATION_ROOT = '/'

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def parse_truck_request(message):
    """Parse truck maintenance notification format with detailed error checking"""
    try:
        lines = [line.strip() for line in message.split('\n') if line.strip()]
        
        missing_fields = []
        if len(lines) < 3:
            missing_fields.extend([
                "Registration Number" if len(lines) < 1 else None,
                "Driver Name" if len(lines) < 2 else None,
                "Mobile Number" if len(lines) < 3 else None
            ])
            missing_fields = [f for f in missing_fields if f]
        
        email_found = any('email:' in line.lower() for line in lines)
        if not email_found:
            missing_fields.append("Email Address")

        if missing_fields:
            return {
                'status': 'incomplete',
                'missing': missing_fields
            }
            
        # Original parsing logic continues here
        reg_no = lines[0]
        driver_name = lines[1]
        driver_no = lines[2]
        place_of_repair = lines[3] if len(lines) > 3 else "Workshop"
        
        email = None
        for line in lines:
            if 'email:' in line.lower():
                email = line.split('email:')[-1].strip()
                email = email.split()[0] if email else None
                break

        if email:
            return {
                'status': 'complete',
                'data': {
                    'reg_no': reg_no,
                    'driver_name': driver_name,
                    'driver_no': driver_no,
                    'place_of_repair': place_of_repair,
                    'email': email
                }
            }
    except Exception as e:
        print(f"Error parsing message: {str(e)}")
    return {'status': 'error', 'message': 'Failed to parse message'}

def create_repair_email(data):
    """Create repair notification email with clear, informative formatting"""
    return f"""Date: {datetime.now().strftime('%d/%b/%Y')}

Dear RRU Team Eldoret,

TRUCK MAINTENANCE NOTIFICATION - {data['reg_no']}

The truck below Has developed mechanical problem and will be undergoing repairs.

Vehicle & Driver Details:
----------------------
• Registration Number: {data['reg_no']}
• Driver's Name: {data['driver_name']}
• Mobile Number: {data['driver_no']}

Maintenance Information:
---------------------
• Location: {data['place_of_repair']}
• Site Details: Along Uganda Road
• Cargo Type: WET CARGO
• Expected Duration: 24 hours


Thank you for your attention to this matter."""

@app.route('/webhook', methods=['POST'])
def webhook():
    logger.info("Received a webhook request")
    # Get the incoming message from WhatsApp
    message_body = request.form.get('Body')
    from_number = request.form.get('From')

    if not message_body or not from_number:
        logger.error("Missing 'Body' or 'From' in the request")
        return jsonify({"status": "error", "message": "Missing 'Body' or 'From'"}), 400

    # Send immediate "seen" message
    try:
        client.messages.create(
            body="✓✓ Message seen. Processing your request...",
            from_=TWILIO_WHATSAPP_NUMBER,
            to=from_number
        )
        logger.info("Sent 'seen' message successfully")
    except Exception as e:
        logger.error(f"Error sending seen message: {str(e)}")
        return jsonify({"status": "error", "message": "Failed to send seen message"}), 500

    # Parse the truck request
    result = parse_truck_request(message_body)
    
    if result['status'] == 'incomplete':
        missing = ', '.join(result['missing'])
        help_message = f"""Your message is missing the following information:
• {missing}

Please send your message in this format:
KBZ123A  (Registration Number)
John Doe  (Driver Name)
0722123456  (Mobile Number)
Workshop  (Optional repair location)
email: example@email.com"""
        
        try:
            client.messages.create(
                body=help_message,
                from_=TWILIO_WHATSAPP_NUMBER,
                to=from_number
            )
            logger.info("Sent help message for incomplete information")
        except Exception as e:
            logger.error(f"Error sending help message: {str(e)}")
            return jsonify({"status": "error", "message": "Failed to send help message"}), 500
        return jsonify({"status": "error", "message": "Incomplete information"}), 400
    
    elif result['status'] == 'complete':
        # Original email sending logic here, using result['data'] instead of truck_data
        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            
            msg = MIMEMultipart()
            msg['From'] = FROM_EMAIL
            msg['To'] = result['data']['email']
            msg['Subject'] = 'Truck Repair Request'
            body = create_repair_email(result['data'])
            msg.attach(MIMEText(body, 'plain'))

            server.sendmail(FROM_EMAIL, result['data']['email'], msg.as_string())
            server.quit()

            reply_message = f"✓✓ Truck repair request sent to {result['data']['email']}. Please check your inbox."
            client.messages.create(
                body=reply_message,
                from_=TWILIO_WHATSAPP_NUMBER,
                to=from_number
            )
            logger.info("Sent repair request email successfully")
            return jsonify({"status": "success", "message": "Repair request sent"}), 200
        except Exception as e:
            error_msg = f"Error processing repair request: {str(e)}"
            logger.error(error_msg)
            try:
                client.messages.create(
                    body=error_msg,
                    from_=TWILIO_WHATSAPP_NUMBER,
                    to=from_number
                )
            except Exception as ex:
                logger.error(f"Error sending error message: {str(ex)}")
            return jsonify({"status": "error", "message": error_msg}), 500

    logger.error("Failed to process request")
    return jsonify({"status": "error", "message": "Failed to process request"}), 500

# Remove the test_env route
# @app.route('/test-env', methods=['GET'])
# def test_env():
#     twilio_sid = os.getenv('TWILIO_ACCOUNT_SID')
#     return jsonify({"TWILIO_ACCOUNT_SID": twilio_sid})

# Modify the main block for PythonAnywhere compatibility
if __name__ == "__main__":
    app.run(debug=False)
