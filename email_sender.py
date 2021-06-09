import smtplib

from email.message import EmailMessage

email = EmailMessage()
email.set_content("this email is dent from python")
email["From"] = "Soniya Gujjar"
email["To"] = "kamalrathi049@gmail.com"
email["Subject"] = "Email from python"

s = smtplib.SMTP("soniyagujjar049@gmail.com")
s.send_message(email)
print("done")
s.quit()
