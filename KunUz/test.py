import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_email = 'omonnuloraimkulov@gmail.com'
email_password = 'bpwr bjap qyvw chnm'
to_email = 'mominovsharif12@gmail.com'
subject = 'sharifjon'
message = 'mominov'
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

smtp_server = 'smtp.gmail.com'
smtp_port = 587
try:
    server = smtplib.SMTP(smtp_server, smtp_port)

    server.starttls()

    server.login(from_email, email_password)

    server.sendmail(from_email, to_email, msg.as_string())
    print('Email sent successfully!')

except Exception as e:
    print('Email could not be sent. Error:', str(e))

finally:
    server.quit()