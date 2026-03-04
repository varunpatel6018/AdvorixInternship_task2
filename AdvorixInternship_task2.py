import imaplib
import email

# Login credentials
username = "example@gmail.com"
password = "your app password"

# Connect to Gmail
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)

# Select inbox
mail.select("inbox")

# Search for all emails
status, messages = mail.search(None, "ALL")

email_ids = messages[0].split()

# Read latest 5 emails
for i in email_ids[-5:]:
    status, msg = mail.fetch(i, "(RFC822)")

    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])

            print("From:", msg["from"])
            print("Subject:", msg["subject"])

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        print("Body:", part.get_payload(decode=True).decode())
            else:
                print("Body:", msg.get_payload(decode=True).decode())

            print("=" * 50)