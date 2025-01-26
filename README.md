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
6. **Set Twilio webhook URL in Twilio Console:**
   - Navigate to your Twilio number settings.
   - Update the webhook URL to:
     ```bash
   - Set working directory: /home/Issaerium/abdize
   - Set WSGI file path: /var/www/issaerium_pythonanywhere_com_wsgi.py
7. Reload the web app

## Environment Variables Required
   - Set source code: /home/Issaerium/abdize
   - Set working directory: /home/Issaerium/abdize
   - Set WSGI file path: /var/www/issaerium_pythonanywhere_com_wsgi.py
8. Reload the web app

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
**Steps to Reload:**
2. **Verify Email Receipt:**
   - Check the designated email to ensure the maintenance request was received and formatted correctly.
3. **Check Application Logs:**
   - Navigate to the **Web** tab on PythonAnywhere.
   - Review the **Error Log** and **Access Log** for any issues.


1. **Navigate to the Web Tab:**
   - Log in to [PythonAnywhere](https://www.pythonanywhere.com/).
   - Find your web app in the list.
   - Click the **Reload** button to apply all changes.

### 4. **Test Your Application**

Ensure that your application is functioning correctly with the updated webhook URL.


---
   - Click on the **Web** tab in the dashboard.

2. **Reload the Application:**