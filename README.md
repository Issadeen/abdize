# Truck Maintenance Notification System

A WhatsApp-to-Email notification system for truck maintenance requests.

## Local Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables in `.env` file
4. Run the app: `python app.py`

## PythonAnywhere Deployment
1. Log in to PythonAnywhere
2. Open a Bash console
3. Clone your repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git ~/abdize
   ```
4. Create virtual environment:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.9 abdize-env
   workon abdize-env
   pip install -r requirements.txt
   ```
5. Create `.env` file in the project directory
6. Configure Web app:
   - Add new web app
   - Choose manual config (Python 3.9)
   - Set source code: /home/Issaerium/abdize
   - Set working directory: /home/Issaerium/abdize
   - Set WSGI file path: /var/www/issaerium_pythonanywhere_com_wsgi.py
7. Reload the web app

## Environment Variables Required
- TWILIO_ACCOUNT_SID
- TWILIO_AUTH_TOKEN
- TWILIO_WHATSAPP_NUMBER
- SMTP_SERVER
- SMTP_PORT
- SMTP_USERNAME
- SMTP_PASSWORD
- FROM_EMAIL

## Testing the Webhook
1. **Send a Test Message:**
   - Use WhatsApp to send a maintenance request to your Twilio number.
2. **Verify Email Receipt:**
   - Check the designated email to ensure the maintenance request was received and formatted correctly.
3. **Check Application Logs:**
   - Navigate to the **Web** tab on PythonAnywhere.
   - Review the **Error Log** and **Access Log** for any issues.
