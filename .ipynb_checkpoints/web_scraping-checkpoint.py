from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import smtplib
from fetchwebitem import *
from processurl import *

url_csv = "urls.csv"
save_to_csv = True
price_csv = "price.csv"
send_email = False

############################################################################################
# Function to obtain a list urls from file
# dataframe object has 3 columns name, url and alert_discount
def get_urls(csv_file):
    df = pd.read_csv(csv_file)
    return df

# Function to obtain updated price for all products from the file
def process_products(df):
    updated_products = []
    for product in df.to_dict("records"):
        # product["url"] is the URL
        send_email = get_response(product)

# Function to compile message
def get_mail(df):
    subject = "Price Drop Alert"
    body = df[df["alert"]].to_string()
    subject_and_message = f"Subject:{subject}\n\n{body}"
    return subject_and_message

# Function to send email notification
def send_email():
    mail_user = "sunnyyunguan@gmail.com"
    mail_pass = "Ilovekids@6356!"
    mail_to = "sunnyyunguan@gmail.com"
    message_text = compile_message(df)
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login(mail_user, mail_pass)
    smtp.sendmail(mail_user, mail_to, message_text)
############################################################################################
def main():
    df = get_urls(url_csv)
    send_email = process_products(df)
   
    print("send_email:', send_email)
    #if send_email:
    #   send_mail(df_updated)
