import requests
from bs4 import BeautifulSoup
import smtplib
import os 
from dotenv import load_dotenv

url =  input("enter the product url: ")
buy_price = float(input("whats the price you're looking for "))
response = requests.get(
    url= url, 
    headers= { 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept-Language": "en-US,en;q=0.5"
})

load_dotenv()
my_email = os.getenv("my_email")
password = os.getenv("my_password")
reciever_email = os.getenv("recievers_email")

sp = BeautifulSoup(response.text, "html.parser")

title = sp.find(id= "productTitle", class_= "a-size-large product-title-word-break").get_text().replace("  ","")
print(title)
price = sp.find(class_="a-offscreen").get_text()
print(price)
final_price = float(price.split("€")[1])
print(final_price)

message = f"Subject: Product Discount\n\n {title} is now {price}"

if final_price < buy_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user= my_email, password= password)
        connection.sendmail(from_addr= my_email, to_addrs= reciever_email, msg= message.encode('utf-8'))
        
