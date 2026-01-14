import base64

def get_email_body(payload):
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                data = part['body']['data']
                return base64.urlsafe_b64decode(data).decode('utf-8')
    elif payload.get('body', {}).get('data'):
        return base64.urlsafe_b64decode(
            payload['body']['data']
        ).decode('utf-8')
    return ""
