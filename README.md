# Gmail to Google Sheets Sync

This Python script automatically syncs unread emails from your Gmail inbox to a Google Sheets spreadsheet. It fetches email details (sender, subject, date, body) and appends them as rows to the specified sheet, then marks the emails as read.

## Features

- Fetches unread emails from Gmail.
- Extracts sender, subject, date, and body.
- Appends data to Google Sheets.
- Marks processed emails as read.
- Uses OAuth for Gmail access and service account for Sheets access.

## Prerequisites

- Python 3.7+
- Google Cloud Project with Gmail API and Google Sheets API enabled.
- OAuth 2.0 credentials for Gmail.
- Service account key for Sheets.
- A Google Sheets spreadsheet shared with the service account.

## Setup

### 1. Clone or Download the Repository

Ensure you have the project files in a directory.

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Set Up Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Enable the following APIs:
   - Gmail API
   - Google Sheets API

### 4. Create Credentials

#### For Gmail (OAuth):

1. In the Cloud Console, go to "APIs & Services" > "Credentials".
2. Click "Create Credentials" > "OAuth 2.0 Client IDs".
3. Select "Desktop application" and create.
4. Download the JSON file and save it as `credentials/credentials.json` in the `credentials/` folder.

#### For Sheets (Service Account):

1. In the Cloud Console, go to "IAM & Admin" > "Service Accounts".
2. Create a new service account (e.g., "gmail-sheets-bot").
3. Generate a key (JSON) and download it.
4. Save it as `credentials/service_account.json`.

### 5. Share the Google Sheet

1. Create or open your Google Sheets spreadsheet.
2. Click "Share" and add the service account email (from `service_account.json`) as an Editor.
3. Copy the spreadsheet ID from the URL (the long string between `/d/` and `/edit`).

### 6. Configure the Script

1. Open `config.py` and replace `'your_spreadsheet_id_here'` with your actual spreadsheet ID.

### 7. Run the Script

Navigate to the `src/` directory and run:

```bash
python main.py
```

The first run will prompt for Gmail authorization via a browser. Grant permissions.

## Usage

- Run `python main.py` to sync unread emails.
- The script will process up to 10 unread emails per run.
- Data is appended to "Sheet1" in columns A-D: Sender, Subject, Date, Body.

## Project Structure

```
gmail-to-sheets/
├── config.py                 # Configuration file with spreadsheet ID
├── credentials/
│   ├── credentials.json      # OAuth credentials for Gmail
│   └── service_account.json  # Service account key for Sheets
├── proof/
│   ├── proof.txt             # Text proof of successful execution
│   ├── gmail_unread_emails.png  # Screenshot of unread emails
│   ├── google_sheet_output.png  # Screenshot of synced data in Sheets
│   ├── oauth_consent.png     # Screenshot of OAuth consent screen
│   └── demo_video_link.txt   # Link to demonstration video
├── src/
│   ├── main.py               # Main script
│   ├── gmail_service.py      # Gmail API functions
│   ├── sheets_service.py     # Sheets API functions
│   ├── email_parser.py       # Email parsing utilities
│   ├── state.py              # State management (last message ID)
│   └── __init__.py
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── last_message_id.txt       # Stores the last processed message ID
```

## Troubleshooting

- **Import Errors**: Ensure you're running from the `src/` directory or the script path is correct.
- **Authentication Errors**: Re-run to re-authenticate or check credentials.
- **Permission Errors**: Ensure the sheet is shared with the service account and APIs are enabled.
- **No Emails Processed**: Check for unread emails in your inbox.

## Security Notes

- Keep `credentials/` files secure and do not commit them to version control.
- The service account has access to your Sheets; limit its permissions as needed.

## License

This project is for educational purposes. Use at your own risk.

## Video Link
https://youtu.be/3J_pUraLYEQ

## Thank You
