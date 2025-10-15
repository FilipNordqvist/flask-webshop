
from dotenv import load_dotenv
from flask import Flask, render_template
import os
from flask import request, redirect, url_for
import resend

app = Flask(__name__)
load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

r = resend.Emails.send({
  "from": "onboarding@resend.dev",
  "to": "filip_nordqvist@hotmail.com",
  "subject": "Hello World",
  "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
})


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/clothes')
def clothes():
    return render_template("clothes.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send', methods=['POST'])
def send_email():
    email = request.form.get('email')
    message = request.form.get('message')

    if not email or not message:
        return "Email and message required", 400

    try:
        r = resend.Emails.send({
            "from": "hnf.sweden@gmail.com",
            "to": email,
            "subject": "New message from webshop",
            "html": f"<p>{message}</p>"
        })
        print(r)  # För loggning/debug
        return redirect(url_for('contact'))
    except Exception as e:
        print("Error:", e)
        return "Failed to send email", 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
