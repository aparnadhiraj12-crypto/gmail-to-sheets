import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.gmail_service import (
    authenticate_gmail,
    fetch_unread_messages,
    get_message,
    mark_as_read
)

from src.sheets_service import append_row
from src.email_parser import get_email_body
from src.state import load_last_message_id, save_last_message_id
from config import SPREADSHEET_ID


def main():
    print("Starting Gmail → Sheets sync...")

    service = authenticate_gmail()
    messages = fetch_unread_messages(service)

    if not messages:
        print("No unread emails found.")
        return

    last_id = load_last_message_id()
    newest_id = None

    for msg in messages:
        msg_id = msg['id']

        # Stop when we reach already-processed email
        if msg_id == last_id:
            break

        if newest_id is None:
            newest_id = msg_id

        email = get_message(service, msg_id)
        headers = email['payload']['headers']

        sender = subject = date = ""

        for h in headers:
            if h['name'] == 'From':
                sender = h['value']
            elif h['name'] == 'Subject':
                subject = h['value']
            elif h['name'] == 'Date':
                date = h['value']

        body = get_email_body(email['payload'])

        append_row(
            SPREADSHEET_ID,
            [sender, subject, date, body]
        )

        mark_as_read(service, msg_id)
        print(f"Processed: {subject}")

    if newest_id:
        save_last_message_id(newest_id)

    print("Sync completed successfully.")


if __name__ == "__main__":
    main()
