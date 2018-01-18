import smtplib, sys

my_email_address = sys.argv[1] # Receiving the email id and password from command line
password = sys.argv[2]


smtpObject = smtplib.SMTP_SSL('smtp.gmail.com', 465) # Encryption is enabled by default in this port

smtpObject.login(my_email_address, password) 

to_email = "to_email_address@example.com"
subject = "Subject: Using SMTP through Python"
body = "This is the message I want to send via email"

print("Sending email to " + to_email)
smtpObject.sendmail(my_email_address, to_email, subject + '\n' + body)
