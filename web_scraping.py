import pandas as pd
import smtplib
from processurl import *

url_csv = "urls.csv"
############################################################################################
# Function to obtain a list urls from file
# dataframe object has 3 columns name, url and alert_discount
def get_urls(csv_file):
    df = pd.read_csv(csv_file)
    return df

# Function to obtain updated price for all products from the file
def process_products(df):
    product_list = df.to_dict("records")
    print(len(product_list))
    for product in product_list:
        # product["url"] is the URL
        #print(product)
        alert = get_response(product)
        print(product["name"] + " {0}".format(alert))
        
# Function to compile message
def compile_message():
    subject = "product list is processed successfully!"
    body = "check output files."
    subject_and_message = f"Subject:{subject}\n\n{body}"
    return subject_and_message

# Function to send email notification
def send_email():
    print('sending email.')
    # mail_user = "username"
    # mail_pass = "password"
    # to = "recipient"
    # message_text = compile_message()
    # try :
    #     with smtplib.SMTP("smtpxxxxxx", 587) as smtp:
    #         smtp.starttls() # start TLS for security
    #         smtp.login(mail_user, mail_pass)
    #         smtp.sendmail(mail_user, to, message_text)
    #         smtp.quit() # terminate the session
    #         print("okay. Email has been sent.")
    # except :
    #     print("fail to send the email")
############################################################################################        
def main(): 
    df = get_urls(url_csv)
    process_products(df)
    send_email()

if __name__ == "__main__":
    main()