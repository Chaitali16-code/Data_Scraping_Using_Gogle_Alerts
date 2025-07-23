# Data_Scraping_Using_Gogle_Alerts
Forward Alerts to a Gmail Label and Read via Python
🔧 Setup:
Create Google Alerts
Go to: https://www.google.com/alerts
Set alerts for your desired keyword(s)
Set “Deliver to” → your Gmail
Label the Emails (optional but helpful)
Create a label (e.g., GoogleAlerts)
Create a Gmail filter to automatically apply this label to alerts
Enable Gmail API
Go to Google Cloud Console
Create a project
Enable Gmail API
Create OAuth 2.0 credentials
Download credentials.json
Use Python to Access Gmail
 Install required libraries:
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
