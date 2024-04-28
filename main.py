import requests
import locale
from bs4 import BeautifulSoup
import lxml
import smtplib

my_email = "vivekgawarpython@gmail.com"
password = "gamkovfahzehlauu"

locale.setlocale(locale.LC_ALL, '')
URL = "https://www.amazon.in/Apple-iPhone-256GB-Deep-Purple/dp/B0BDK2FB2T/ref=sr_1_1_sspa?crid=2Y7LVACAAI0PM&keywords=iphone+14+pro+max&qid=1694256443&s=electronics&sprefix=iphon%2Celectronics%2C208&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"}

response = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("₹")[1]
price_as_float = locale.atof(price_without_currency)

if price_as_float < 100000:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="vivekgaver2016@gmail.com",
        msg=f"Subject:Price Drop Alert!\n\nThe price of Iphone 14 Pro Max is less than 150000 now! Get it now! \n{URL}"
    )
    connection.close()
