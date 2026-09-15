import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")

URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(URL, headers={"Accept-Language":"en-US"})
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
find_price = soup.find_all(name="span", class_="aok-offscreen")

price = [p.getText() for p in find_price][0].split("$")[1]

if float(price) < 100:
    #print(f"Instant Pot Duo is now ${price}\n{URL}")
    msg = EmailMessage()
    msg["Subject"] = "Amazon Price"
    msg["From"] = SMTP_ADDRESS
    msg["To"] = EMAIL_ADDRESS
    msg.set_content(f"Instant Pot Duo is now ${price}\n{URL}")

    with smtplib.SMTP(SMTP_ADDRESS, 587) as connection:
        connection.starttls()
        connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.send_message(msg)
