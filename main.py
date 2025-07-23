from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
import email

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)
service = build('gmail', 'v1', credentials=creds)

results = service.users().messages().list(userId='me', labelIds=['Label_123456'], maxResults=10).execute()
messages = results.get('messages', [])

for msg in messages:
    msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
    snippet = msg_data['snippet']
    print(snippet)
