from threading import Thread
from flask import Flask

app = Flask('')

@app.route('/')
def home():
    return f"I am up and running! "

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_running():
    t = Thread(target=run)
    t.start()