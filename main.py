import smtplib
import server
import random
import time
import os

server.keep_running()

list_of_messages = ["Always believe that something wonderful will probably never happen",
                    "Due to recent cutbacks, the light at the end of the tunnel has been turned off",
                    "Until you spread your wings, you will never know that you can\'t fly",
                    "Always remember that you are unique - just like everybody else",
                    "Everything happens for a reason. Sometimes the reason is that you\'re stupid and make bad decisions",
                   "You\'re only as good as your last fuck-up.",
                   "Going outside is highly overrated"]
list_of_time_options = [1800,
                        3600]

def choose_message(lst_msg):
  random_msg = random.choice(lst_msg)
  lst_msg.remove(random_msg)
  return random_msg

sender_email = os.environ['sender_email']
sender_password = os.environ['sender_password']
reciever_email = os.environ['reciever_email']

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(sender_email, sender_password)

for i in range(len(list_of_messages)):
  message = 'Subject: {}\n\n{}'.format(f"Day {i + 1}", f'{choose_message(list_of_messages)}')
  server.sendmail(sender_email, reciever_email, message)
  print(f"{i + 1} emails sent!")
  time.sleep(random.choice(list_of_time_options))