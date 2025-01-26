import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables from .env file
load_dotenv()

# Twilio credentials from environment variables
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
TO_WHATSAPP_NUMBER = os.getenv("TO_WHATSAPP_NUMBER")

# Email SMTP credentials
SMTP_SERVER = os.getenv("EMAIL_SMTP_SERVER")
SMTP_PORT = int(os.getenv("EMAIL_PORT"))
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Function to send email
def send_email(driver_name, reg_no, driver_no, vendor, recipient_email):
    subject = "Truck Repair Request"
    email_body = f"""
    Date: 25/Jan/2024

    Dear RRU team Eldoret,

    The truck below has developed a mechanical problem and is going to be repaired at Hass along Uganda road.
    We kindly request your esteemed office to allow the below truck to be repaired within the next 24 hours.

    Reporting for Repairs/Fueling/Return Back/Others
    Name of Driver: {driver_name}
    Reg. No or Chassis No.: {reg_no}
    Driver No: {driver_no}
    Container No: WET CARGO
    Entry No: 
    Vendor: {vendor}
    Seal No: 
    Place of Repair: HASS
    Exact location of above: Along Uganda road
    Estimated repair time hrs: 24 hrs
    """

    msg = MIMEText(email_body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_USERNAME
    msg["To"] = recipient_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USERNAME, [recipient_email], msg.as_string())

    print(f"Email sent successfully to {recipient_email}")

# Function to receive WhatsApp messages
def check_whatsapp_messages():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    messages = client.messages.list(limit=5)  # Get last 5 messages

    for msg in messages:
        if msg.from_ == TO_WHATSAPP_NUMBER and msg.direction == "inbound":
            content = msg.body.strip().split("\n")
            if len(content) >= 5:
                reg_no, driver_name, driver_no, vendor, email = content
                send_email(driver_name, reg_no, driver_no, vendor, email)
                print(f"Processed message from {driver_name}")
            else:
                print("Invalid message format received.")

# Run the process
if __name__ == "__main__":
    check_whatsapp_messages()
