from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import time

# Setup Selenium
service = Service('path_to_chromedriver')  # Replace with the path to your chromedriver
driver = webdriver.Chrome(service=service)

# Load the page
url = 'https://workat.tech/company/amazon/interview-questions/problem-solving'
driver.get(url)

# Wait for content to load
time.sleep(5)

# Find all rows of the problem table
rows = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')

# Open a CSV file to write the data
with open('amazon_interview_problems.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Problem Name', 'Score', 'Accuracy', 'Difficulty', 'Companies'])

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if len(cells) >= 5:
            problem_name = cells[0].text
            score = cells[1].text
            accuracy = cells[2].text
            difficulty = cells[3].text
            companies = cells[4].text  # this may include logos/names

            writer.writerow([problem_name, score, accuracy, difficulty, companies])

driver.quit()
print("CSV file 'amazon_interview_problems.csv' has been created.")
