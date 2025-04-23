from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

service = Service('C:/Users/DrDoom/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')

driver = webdriver.Chrome(service=service)
driver.get("https://www.bookswagon.com/?srsltid=AfmBOoqBhkhiu3TffwPXZkgEVae4dUwRFvXNzzvxqCu4Ajy7cJ4PF8g7")

book_data=[]

quotes = driver.find_elements(By.CLASS_NAME, "card")
for quote in quotes:
    title=quote.find_element(By.CLASS_NAME,"card-text").find_element(By.CLASS_NAME,"booktitle").text.strip()
    if title == '':
        continue
    price=quote.find_element(By.CLASS_NAME,"actualprice").text.strip()[1:]
    try:
        initprice = quote.find_element(By.CSS_SELECTOR, "span.initialprice del").text.strip()[1:]
    except:
        initprice = "N/A"
    author=quote.find_element(By.CLASS_NAME,"author").text.strip()
    book_data.append({'TITLE':title,'Price':price,'Initial_Price':initprice if initprice != "N/A" else initprice,'Author':author})
driver.quit()

df = pd.DataFrame(book_data)
with open('books_selenium.csv', 'w', newline='', encoding='utf-8') as f:
    df.to_csv(f, index=False)

print("Book data saved to 'books_selenium.csv'")
