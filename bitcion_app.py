import requests
from bs4 import BeautifulSoup
import smtplib

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}

url = "https://www.google.com/search?client=firefox-b-d&channel=trow&q=bitcoin+price"

print("Enable less-decure app access before entering your email and password")

sender = input("Your email: ")
password = input("Your password: ")
send_to = input("Sending to: ")

def send_email():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login(sender,password)

  subject = "Bitcoin price has changed!"
  body = f"The price has dropped from {current_price} to {updated_price}. We want you to take a look- {url}"
  message = f"Subject:{subject}\n\n\n{body}"

  server.sendmail(sender,send_to,message)
  server.quit()
  print("EMAIL HAS BEEN SENT!")

page = requests.get(url,headers=headers)
soup = BeautifulSoup(page.content,"html.parser")

current_price = "1,915,400.72"
updated_price = soup.find(class_="DFlfde SwHCTb").get_text()
print(updated_price)

if current_price != updated_price:
  send_email()