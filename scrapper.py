import requests
from bs4 import BeautifulSoup
import time
import smtplib


URL = 'https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-F3-5-5-6/dp/B07B45D8WV/ref=sr_1_1?keywords=sony+a7&qid=1563012992&s=gateway&sr=8-1'

headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


def check_price():
        
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = price[1:10]
    
    if(converted_price == 1,55,000):
        send_mail()

    print(converted_price)
    print(title.strip())
        

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('michellesenorita3@gmail.com','wuanmhsvkpxhebps')

    subject = "Hey! Here's your fantastic offer from Amazon."
    body = 'Check the amazon link: https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-F3-5-5-6/dp/B07B45D8WV/ref=sr_1_1?keywords=sony+a7&qid=1563012992&s=gateway&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'michellesenorita3@gmail.com',
        'raikarshiva8@gmail.com',
        msg
    )

    print("Hey! Email has been sent to raikarshiva8@gmail.com")
    server.quit()


check_price()
