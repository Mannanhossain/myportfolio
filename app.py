import os
from flask import Flask, render_template, request, redirect, url_for
from twilio.rest import Client

app = Flask(__name__)

# Twilio credentials from environment variables
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.environ.get("TWILIO_PHONE")
MY_PHONE = os.environ.get("MY_PHONE")

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send_sms():
    name = request.form.get("name")
    email = request.form.get("email")
    message_text = request.form.get("message")

    sms_body = f"New portfolio message:\nName: {name}\nEmail: {email}\nMessage: {message_text}"

    client.messages.create(
        body=sms_body,
        from_=TWILIO_PHONE,
        to=MY_PHONE
    )

    return redirect(url_for("thankyou"))

@app.route("/thank-you")
def thankyou():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)
