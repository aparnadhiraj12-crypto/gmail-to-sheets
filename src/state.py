import os

STATE_FILE = os.path.join(os.path.dirname(__file__), '..', 'last_message_id.txt')

def load_last_message_id():
    try:
        with open(STATE_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def save_last_message_id(message_id):
    with open(STATE_FILE, "w") as f:
        f.write(message_id)
