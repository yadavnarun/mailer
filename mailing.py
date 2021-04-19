# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

scn = ["20U03027"]

fromaddr = "verydopeperson@gmail.com"
s = smtplib.SMTP('smtp.gmail.com', 587) # creates SMTP session

# start TLS for security
s.starttls()
s.login(fromaddr, "DopePerson123")

for scholar in range(len(scn)):

  toaddr = scn[scholar] + "@iiitbhopal.ac.in"

  print(toaddr)

  # instance of MIMEMultipart
  msg = MIMEMultipart()
  msg['From'] = fromaddr
  msg['To'] = toaddr
  msg['Subject'] = "Subject"
  body = "Body"
  msg.attach(MIMEText(body, 'plain'))

  # open the file to be sent ( names according to person name or number ) { also pdf/files should be in same directory or change directory }
  filename = scn[scholar] + ".pdf"
  attachment = open("./" + filename, "rb")

  p = MIMEBase('application', 'octet-stream') # instance of MIMEBase and named as p
  p.set_payload((attachment).read()) # To change the payload into encoded form
  encoders.encode_base64(p) # encode into base64
  p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  msg.attach(p) # attach the instance 'p' to instance 'msg'

  text = msg.as_string()

  # sending the mail
  s.sendmail(fromaddr, toaddr, text)


# terminating the session
s.quit()
