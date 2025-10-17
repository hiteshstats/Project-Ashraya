from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
import os

application = Flask(__name__)

# Configuration
YOUR_EMAIL = os.getenv("YOUR_EMAIL")
YOUR_PASSWORD = os.getenv("YOUR_PASSWORD")

@application.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        favourite = request.form.get("favourite")
        send_email(favourite)
        return render_template("index.html", success=True)
    return render_template("index.html", success=False)

def send_email(favourite):
    subject = "New Favourite Thing of the Month  "
    body = f"Your girlfriend’s favourite thing for this month is: {favourite}"
    msg = MIMEText(body)
    msg["Subject"] = "Ashraya's new favourite of the month 💖 "
    msg["From"] = YOUR_EMAIL
    msg["To"] = YOUR_EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(YOUR_EMAIL, YOUR_PASSWORD)
        server.send_message(msg)
