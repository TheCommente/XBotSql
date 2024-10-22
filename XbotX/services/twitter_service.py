# services/twitter_service.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_driver():
    """
    Creates a new Selenium WebDriver instance using the ChromeDriver.
    Returns:
        driver (webdriver.Chrome): The WebDriver instance.
    """
    chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
    service = Service(chromedriver_path)  # Correctly create a Service object
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def login_to_twitter(driver):
    """
    Automates the login process to Twitter.
    Args:
        driver (webdriver.Chrome): The WebDriver instance controlling the browser.
    """
    username = os.getenv("TWITTER_USERNAME")
    password = os.getenv("TWITTER_PASSWORD")

    print("Logging in to Twitter...")
    driver.get("https://x.com/i/flow/login")  # Navigate to the Twitter login page
    
    # Wait for the username input field to appear and then enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "text")))
    username_input = driver.find_element(By.NAME, "text")
    username_input.send_keys(username)
    
    # Wait for the "Next" button to be clickable and click it
    next_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Next' or text()='הבא']"))
    )
    next_button.click()
    
    # Wait for the password input field to appear and then enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(password)
    
    # Wait for the "Log in" button to be clickable and click it
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Log in' or text()='כניסה']"))
    )
    login_button.click()
    
    # Wait for a few seconds to allow login to complete
    time.sleep(5)
    print("Logged in successfully.")

def tweet_with_image(driver, message, image_path=None):
    """
    Composes a tweet with an optional image and posts it.
    Args:
        driver (webdriver.Chrome): The WebDriver instance controlling the browser.
        message (str): The content of the tweet.
        image_path (str or None): The file path to the image to be attached to the tweet.
    """
    print(f"Composing tweet: {message}")
    driver.get("https://twitter.com/compose/tweet")  # Navigate to the tweet compose page
    
    # Wait for the tweet box to appear and enter the tweet content
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "public-DraftStyleDefault-block"))).send_keys(message)
    
    # If an image is provided, upload it
    if image_path:
        print(f"Uploading image: {image_path}")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        ).send_keys(image_path)
        time.sleep(5)
    
    post_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='tweetButton']"))
    )
    post_button.click()
    print("Tweet posted successfully.")
    time.sleep(3)
