from flask import Flask, app
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config('MAIL_SERVER') = 'smtp.gmail.com'
app.config('MAIL_PORT') = 465
app.config('MAIL_USERNAME') = 'xyz@gmail.com'
app.config('MAIL_PASSWORD') = '***'
app.config('MAIL_USE_TLS') = False
app.config('MAIL_USE_SSL') = True
mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hello', sender = 'xyz@gmail.com', recipient = 'abc@gmail.com')
    msg.body = "hello Flask! This is an email."
    mail.send(msg)
    return "Message sent"

if __name__ == "__main__":
    app.run(debug=True)