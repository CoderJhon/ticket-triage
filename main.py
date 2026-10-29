#Prints a ticket preview from a client email


#fromEmail = "jpalomino@kpinterface.com"
#subjectEmail = "Ticket System"
#messageEmail = "Test preview for a client email to the ticket system"



import os
import imaplib
import email
from dotenv import load_dotenv
from email import policy

load_dotenv()
address = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")

mail = imaplib.IMAP4_SSL("imap.gmail.com")   # connect on 993
mail.login(address, password)                # log in
mail.select("INBOX")                         # open the inbox
status, data = mail.search(None, "ALL")      # get every email's ID
latest_id = data[0].split()[-1]

status, msg_data = mail.fetch(latest_id, "(RFC822)")
raw_email = msg_data[0][1]

msg = email.message_from_bytes(raw_email, policy=policy.default)
body = msg.get_body(preferencelist=("plain",)).get_content().strip()


sender = msg["From"]
subject = msg["Subject"]

print("-" * 20)
print("NEW TICKET")
print(f"From: {sender}")
print(f"Subject: {subject}")
print("Message: " + body)
print("-" * 20)


mail.logout()