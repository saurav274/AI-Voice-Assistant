import mysql.connector
import os
from dotenv import load_dotenv
import webbrowser

# Load environment variables from the .env file
load_dotenv(".env")

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

def get_website(site_name):
    # Use a parameterized query to safely search for the website
    cursor.execute(
        "SELECT url FROM sites WHERE site_name=%s",
        (site_name,)
    )
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

def open_site(site_name):
    url = get_website(site_name)

    if url:
        webbrowser.open(url)
        return True

    return False

#Check this and add comments so user can understand this
