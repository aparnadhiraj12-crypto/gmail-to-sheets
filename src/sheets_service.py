from googleapiclient.discovery import build
from google.oauth2 import service_account
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICE_ACCOUNT_PATH = os.path.join(BASE_DIR, '../credentials/service_account.json')

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets'
]

def get_sheets_service():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_PATH, scopes=SCOPES
    )
    return build('sheets', 'v4', credentials=creds)
    return build('sheets', 'v4', credentials=creds)

def append_row(spreadsheet_id, values):
    service = get_sheets_service()

    body = {"values": [values]}
    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range="Sheet1!A:D",
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute()
