import smtplib

from email.message import EmailMessage

email = EmailMessage()
email.set_content("this email is dent from python")
email["From"] = "sender's Name"
email["To"] = "receiver's email"
email["Subject"] = "Email from python"

with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("sender's email", "password")
    smtp.send_message(email)
    print("done")
