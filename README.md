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
     ```
     https://Issaerium.pythonanywhere.com/webhook
     ```
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

## Steps to Reload:
1. **Navigate to the Web Tab:**
   - Log in to [PythonAnywhere](https://www.pythonanywhere.com/).
   - Find your web app in the list.
   - Click the **Reload** button to apply all changes.
   - Click on the **Web** tab in the dashboard.

   - Find your web app in the list.
   - Click the **Reload** button to apply all changes.

   ![Reload Button](https://i.imgur.com/your-reload-button-image.png) *(Replace with actual image if needed)*

---

   - Click the **Reload** button to apply all changes.

   ![Reload Button](https://i.imgur.com/your-reload-button-image.png) *(Replace with actual image if needed)*


If you encounter any further issues, monitor your application logs to identify and resolve them.

Double-check that the Twilio webhook URL is correctly pointing to your live PythonAnywhere endpoint.



   - Ensure all required variables (`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, etc.) are correctly defined without typos.

2. **Confirm Loading in `app.py`:**   - Ensure `load_dotenv()` is called correctly to load the `.env` file.3. **Test Environment Variables:**   - Click on the **Web** tab in the dashboard.2. **Reload the Application:**   - As you've already done, use a test route or print statements to confirm environment variables are being loaded.   ```bash   python -c "from dotenv import load_dotenv; load_dotenv(); import os; print(os.getenv('TWILIO_ACCOUNT_SID'))"   ```   - Ensure the output matches the value in your `.env` file.
---

**Steps:**

1. **Navigate to the Web Tab:**
   - Log in to [PythonAnywhere](https://www.pythonanywhere.com/).
   - Click on the **Web** tab in the dashboard.

2. **Access Error Logs:**
   - Under your web app's settings, locate the **Error Log** section.
   - Click on the **Error Log** to view recent errors.
   
   ![Error Log](https://i.imgur.com/your-error-log-image.png) *(Replace with actual image if needed)*

3. **Review the Logs:**
   - Look for any error messages or stack traces that indicate issues in your `app.py` or other parts of your application.
   - Common issues might include missing environment variables, syntax errors, or import errors.

#### b. **Twilio Console Logs**

**Steps:**


1. **Navigate to the Web Tab:**
   - Log in to [PythonAnywhere](https://www.pythonanywhere.com/).
   - Click on the **Web** tab in the dashboard.

2. **Reload the Application:**
   - Find your web app in the list.
   - Click the **Reload** button to apply all changes.

   ![Reload Button](https://i.imgur.com/your-reload-button-image.png) *(Replace with actual image if needed)*

---

### 8. **Monitor and Test**

**Summary:**
After implementing the above steps, monitor your application to ensure the issue is resolved.

**Steps:**

1. **Use cURL to Send a Test POST Request:**

   Open your terminal and execute the following command:

   ```bash

1. **Use cURL to Send a Test POST Request:**

   Open your terminal and execute the following command:

   **Expected Response:**
   ```json
   {
     "status": "success",
     "message": "Repair request sent"
   }
   ```

After making changes to your application, always reload the web app to apply them.

2. **Use Postman or Similar Tools:**

   - Open [Postman](https://www.postman.com/) or a similar API testing tool.
   - Create a new POST request to `https://Issaerium.pythonanywhere.com/webhook`.
   - In the body, select `x-www-form-urlencoded` and add the following key-value pairs:
     - `Body`: 
       ```
       KBZ123A
   - Send the request and verify that you receive a successful response.

### 5. **Check Twilio’s Request Inspector**

**Summary:**
Twilio provides a Request Inspector tool that allows you to view detailed information about webhook requests.

---
       email: example@email.com
       ```
     - `From`: `whatsapp:+254700000000`
       John Doe
       0722123456
       Workshop
   If you receive this response, your webhook is functioning correctly.

### 7. **Reload the Web App on PythonAnywhere**

**Summary:**
**Steps:**

   - Ensure that there are no code paths where the function could exit without returning a response, which would cause Twilio to experience a timeout.

---
   - Wrap critical sections of your code in try-except blocks to catch unexpected errors and respond with appropriate messages and status codes.

3. **Avoid Hanging Requests:**
2. **Handle Unexpected Errors:**
1. **Validate Return Statements:**
     return jsonify({"status": "success", "message": "Repair request sent"}), 200
     ```
   
   - Ensure that every possible execution path in the `webhook` function returns a valid HTTP response with the correct status code.
   - Example:
     ```python
**Steps:**
**Steps:**

1. **Access Twilio Request Inspector:**
   - In the [Twilio Console](https://www.twilio.com/console), navigate to **Monitor** > **Logs** > **Request Inspector**.

2. **Locate the Failed Request:**
   - Find the entry corresponding to the failed message with error code `11200`.
   - Click on the request to view detailed information.

3. **Review Request Details:**
   - **Request URL:** Ensure it matches `https://Issaerium.pythonanywhere.com/webhook`.
   - **HTTP Method:** Should be `POST`.
   - **Status Code:** Should now be `200`. If not, note the actual status code.
   - **Error Message:** Review any error messages provided by Twilio.

4. **Analyze the Details:**
   - Look for issues such as:
     - **Timeouts:** Ensure your webhook responds promptly.
     - **SSL Issues:** PythonAnywhere should have valid SSL certificates. Verify no SSL handshake errors.
     - **Firewall Restrictions:** Ensure your application isn't blocking incoming requests.

---

### 7. **Reload the Web App on PythonAnywhere**

**Summary:**
After making any changes to your application or configuration, always reload the web app to apply the updates.


1. **Log in to PythonAnywhere:**
   - Navigate to [PythonAnywhere](https://www.pythonanywhere.com/) and sign in.

2. **Navigate to the Web Tab:**
   - Click on the **Web** tab in the dashboard.

3. **Access Logs:**
   - **Error Logs:**
     - Locate the **Error Log** section and review any new error messages or stack traces.
   - **Access Logs:**
     - Locate the **Access Log** section to see incoming requests and their statuses.

4. **Analyze the Logs:**
   - **Error Log:**
     - Identify any new errors that occurred during the manual testing.
     - Common issues might include exceptions thrown during request processing.
   - **Access Log:**
     - Confirm that the `POST /webhook` requests are receiving `200` status codes after your changes.

---

### 6. **Check Twilio’s Request Inspector**

**Summary:**
Twilio provides a Request Inspector tool that allows you to view detailed information about webhook requests, which can help identify issues.


> **Action:**
> - If you added new dependencies, ensure they are listed in `requirements.txt`.
> - To install any new dependencies, run:
>   ```bash
>   pip install -r /home/Issaerium/abdize/abdize/requirements.txt
>   ```
> - After updating `requirements.txt`, reload your web app.

### 4. **Reload the Web App on PythonAnywhere**

**Summary:**
After making changes to your application code or configuration files, reload the web app to apply the updates.
**Steps:**

1. **Navigate to the Web Tab:**

   ![Reload Button](https://i.imgur.com/your-reload-button-image.png) *(Replace with actual image if needed)*

### 5. **Final Verification**

**Summary:**
Ensure that the `/webhook` endpoint correctly handles `POST` requests and responds appropriately. Also, verify that accessing it via a browser yields the expected message if the optional `GET` handler is implemented.

## Final Verification
1. **Access the Root Route:**
   - Open `https://issaerium.pythonanywhere.com/` in your browser.
   - **Expected Response:**
     ```
     Truck Maintenance Notification System is running.
   - Click on the **Web** tab in the dashboard.
     ```

2. **Test the `/webhook` Route:**
   - **Using cURL:**
     ```bash
     curl -X POST https://Issaerium.pythonanywhere.com/webhook \
     -d "Body=KBZ123A\nJohn Doe\n0722123456\nWorkshop\nemail: example@email.com" \
     -d "From=whatsapp:+254700000000"
     ```
     **Expected Response:**
     ```json
     {
       "status": "success",
       "message": "Repair request sent"
     }
     ```

   - **Using Postman:**
     - Open [Postman](https://www.postman.com/) or a similar tool.
     - Create a new `POST` request to `https://Issaerium.pythonanywhere.com/webhook`.
     - In the body, select `x-www-form-urlencoded` and add:
       - `Body`: 
         ```
         KBZ123A
         John Doe
         0722123456
         Workshop
         email: example@email.com
         ```
       - `From`: `whatsapp:+254700000000`
     - Send the request and verify the response.

3. **Access `/webhook` via Browser (Optional):**
   - Open `https://issaerium.pythonanywhere.com/webhook` in your browser.
   - **Expected Response (if GET handler is added):**
     ```
     This endpoint accepts POST requests only.
     ```
   - **If GET handler is not added, you will receive a 405 error**, which is expected behavior.

4. **Monitor Logs:**
   - **PythonAnywhere:**
     - Go to the **Web** tab.
     - Check both **Error Log** and **Access Log** for any new entries or errors.
   - **Twilio:**
     - In the [Twilio Console](https://www.twilio.com/console), navigate to **Monitor** > **Logs** > **Request Inspector**.
     - Verify that webhook requests have a `200` status code and no errors.

# Summary of Actions

1. **Added a GET Handler for `/webhook` (Optional):**
   - Allows friendly messaging when accessing the endpoint via a browser.
   
2. **Confirmed Twilio Webhook Configuration:**
   - Ensured Twilio is set to send `POST` requests to the correct webhook URL.

3. **Reloaded the Web App on PythonAnywhere:**
   - Applied all changes to ensure the application runs with the latest configurations.

4. **Performed Final Verification:**
   - Tested both `GET` and `POST` requests to ensure endpoints behave as expected.
   - Monitored logs to confirm successful processing of webhook requests.

# Next Steps

- **Monitor Application Logs:**
  - Continuously check the **Error Log** and **Access Log** on PythonAnywhere to identify and resolve any new issues.

- **Secure Sensitive Routes:**
  - If you added the `GET` handler for `/webhook`, ensure it does not expose sensitive information.

- **Enhance Application Functionality:**
  - Depending on your needs, consider adding more routes or features to your Flask application.

Feel free to reach out if you encounter further issues or need additional assistance!

   - Click the **Reload** button to apply all changes.
2. **Reload the Application:**
   - Find your web app in the list.
   - Log in to [PythonAnywhere](https://www.pythonanywhere.com/).
   - Click on the **Web** tab in the dashboard.