##import psutil
#print("The CPU usage is:", psutil.cpu_percent(4))

import paramiko

import csv
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

commands = [
    
    "top -b -n1 | grep 'Cpu(s)' | awk '{print $2 +$4}' ",
    "free | grep Mem | awk '{print $4/$2 * 100.0}'",
    "date +%d/%m/%Y%t%H:%M:%S"
]
username = "ubuntu01"
hostname = '192.168.0.102'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect(hostname=hostname,username=username)
except:
    print("[!] can not connect to ssh server")
    exit()

lst = []
ls = []
for command in commands:
    print("*"*50, command, "*"*50)
    stdin, stdout, stderr = ssh.exec_command(command)
    ls = (stdout.read().decode())
    print(ls)
    lst.append(ls)
    print(lst)
    err = stderr.read().decode()
    if err:
        print(err)

fieldnames = ['VM name','IpAddress','CPU_usage', 'RAM_usage','TIME_Stamp']

lst1 = lst[0].split("\n")
lst2 = lst[1].split("\n")
lst3=lst[2].split("\n")
print(lst1[1])
with open("data.csv","w") as fw:
    writer = csv.writer(fw)
    writer.writerow(fieldnames)
    writer.writerow([username,hostname,lst1[0],lst2[0],lst3[0]])


emailfrom = "prathyusharaju233@gmail.com"
emailto = "rishiroyal666@gmail.com"
fileToSend = "data.csv"
username = "prathyusharaju233@gmail.com"
password = "shiridisai"

msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = "checkout whether the output csv file is received or not"
msg.preamble = "checkout whether the output csv file is received or not"
ctype,encoding=mimetypes.guess_type(fileToSend)
if ctype is None or encoding is not None:
    ctype = "application/octet-stream"

maintype, subtype = ctype.split("/", 1)

if maintype == "text":
    fp = open(fileToSend)
    # Note: we should handle calculating the charset
    attachment = MIMEText(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "image":
    fp = open(fileToSend, "rb")
    attachment = MIMEImage(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "audio":
    fp = open(fileToSend, "rb")
    attachment = MIMEAudio(fp.read(), _subtype=subtype)
    fp.close()
else:
    fp = open(fileToSend, "rb")
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(attachment)
attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
msg.attach(attachment)

server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(username,password)
server.sendmail(emailfrom, emailto, msg.as_string())
server.quit()