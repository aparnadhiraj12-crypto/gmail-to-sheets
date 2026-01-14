# src/gmail_service.py

import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# ✅ Updated scope (needed to mark emails as read and access Sheets)
SCOPES = [
    'https://www.googleapis.com/auth/gmail.modify'
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_PATH = os.path.join(BASE_DIR, '../credentials/credentials.json')
TOKEN_PATH = os.path.join(BASE_DIR, 'token.json')


def authenticate_gmail():
    """Authenticate the user and return a Gmail API service instance."""
    creds = None

    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_PATH, SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'w') as token_file:
            token_file.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    return service


def fetch_unread_messages(service, max_results=10):
    """
    Fetch unread email MESSAGE METADATA (IDs only).
    Actual email content will be fetched separately.
    """
    results = service.users().messages().list(
        userId='me',
        labelIds=['INBOX', 'UNREAD'],
        maxResults=max_results
    ).execute()

    return results.get('messages', [])


def get_message(service, message_id):
    """Fetch full email data using message ID."""
    return service.users().messages().get(
        userId='me',
        id=message_id,
        format='full'
    ).execute()


def mark_as_read(service, message_id):
    """Mark an email as read."""
    service.users().messages().modify(
        userId='me',
        id=message_id,
        body={'removeLabelIds': ['UNREAD']}
    ).execute()
