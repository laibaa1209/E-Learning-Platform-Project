import os
import random
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi

# Load .env
load_dotenv()

# Setup MongoDB
client = MongoClient(os.getenv("MONGO_URI"), tls=True, tlsAllowInvalidCertificates=False, tlsCAFile=certifi.where())
db = client['sample_mflix']  # Database name
users_collection = db['users']            # Collection name

# List all databases
print(client.list_database_names())
# List all collections in the database
print(db.list_collection_names())

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(to_email, otp):
    email_sender = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASS")

    msg = EmailMessage()
    msg['Subject'] = 'Your OTP Verification Code'
    msg['From'] = email_sender
    msg['To'] = to_email
    msg.set_content(f"Your OTP code is: {otp}")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(msg)

def save_user_to_db(name, email, password):
    user_data = {
        "name": name,
        "email": email,
        "password": password  # Normally you should hash the password! (can improve later)
    }
    users_collection.insert_one(user_data)

def is_email_registered(email):
    return users_collection.find_one({"email": email}) is not None

# Ensure the MongoClient is closed before the script exits
if __name__ == "__main__":
    try:
        # Your main script logic here
        pass
    finally:
        client.close()  # Explicitly close the MongoClient