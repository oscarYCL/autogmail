import smtplib
from email.message import EmailMessage
import password
import csv

client_name =[]
to_email = []

with open('client_list.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for line in reader:
        to_email.append(line[2])
        client_name.append(line[1])

del to_email[0]
del client_name[0]
i = 0


for email in to_email:
    email_msg = EmailMessage()  
    send_email = ""


    email_msg['Subject'] = 'Subject Of The Email'  
    email_msg['From'] = 'awssns'  
    email_msg['To'] =  email
    email_msg.set_content("Dear "+ client_name[i] + " :" + " Main Content or Body")  


    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  
    server.login(send_email, password.password)  
    server.send_message(email_msg)  
    server.quit()
    i += 1
        
