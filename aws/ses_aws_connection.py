import smtplib
user = "AKIA4MTWMGIRIKGJ57EM"
pw   = "BFY2Rjk+ECEJyOqsbEdhcz+a8ThpSKO9tsa1rAmKGbWM"
host = 'email-smtp.ap-south-1.amazonaws.com'
port = 465
me = "ezygst.info@caratred.com"
you   = ('ramunavvvvailable@caratred.com',)
body = 'Test'
msg  = ("From: %s\r\nTo: %s\r\n\r\n"
       % (me, ", ".join(you)))

msg = msg + body

s = smtplib.SMTP_SSL(host, port, 'caratred.com')
s.set_debuglevel(2)
s.login(user, pw)

s.sendmail(me, you, msg)
import boto3

sns_client = boto3.client('sns')

# Create an SNS topic
response = sns_client.create_topic(Name='SESBounceNotifications')
topic_arn = response['TopicArn']
print(f"Created SNS topic: {topic_arn}")
