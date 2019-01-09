import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "p.blesson@sitpune.edu.in"
toaddr = "psblesson@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Intruder Alert!"
 
body = "Please check the attachment in relation to suspicious activity on the network"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "attacks.txt"
attachment = open("attacks.txt", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "onlyfortoday")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
