from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd
import time

# Step 1: Set up Selenium WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

# Step 2: Base URL
base_url = "https://results.eci.gov.in/ResultAcGenNov2024/statewiseS131.htm"
driver.get(base_url)
time.sleep(5)  # Allow page to load

# Step 3: Initialize an empty list to store all data
all_data = []

# Step 4: Find the total number of pages
pagination = driver.find_element(By.XPATH, "//div[contains(@class, 'pagination')]")
page_links = pagination.find_elements(By.TAG_NAME, "a")
total_pages = len(page_links)

print(f"Total pages found: {total_pages}")

# Step 5: Loop through each page and scrape data
for page_num in range(1, total_pages + 1):
    print(f"Scraping page {page_num}...")
    
    # Step 5.1: Click on the page link
    page_button = driver.find_element(By.LINK_TEXT, str(page_num))
    ActionChains(driver).move_to_element(page_button).click().perform()
    time.sleep(3)  # Allow page to load

    # Step 5.2: Parse the page source
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Step 5.3: Find the table
    table = soup.find('table')
    if not table:
        print(f"No table found on page {page_num}")
        continue

    # Step 5.4: Extract table rows
    rows = table.find_all('tr')

    # Step 5.5: Extract and clean data
    for row in rows:
        columns = row.find_all('td')
        row_data = [col.text.strip() for col in columns]
        if row_data:  # Skip empty rows
            all_data.append(row_data)

# Step 6: Create a DataFrame
if all_data:
    # Define column names (adjust based on table structure)
    column_names = ['Constituency', 'Const. No.', 'Leading Candidate', 'Leading Party',
                    'Trailing Candidate', 'Trailing Party', 'Margin', 'Round', 'Status']

    # Handle column mismatch dynamically
    num_columns = len(all_data[0])
    if len(column_names) != num_columns:
        column_names = [f'Column {i+1}' for i in range(num_columns)]

    # Combine all data into a DataFrame
    df = pd.DataFrame(all_data, columns=column_names)

    # Save the combined data to a CSV file
    df.to_csv('maharashtra_election_results_all_combined.csv', index=False, encoding='utf-8')
    print("All pages' data saved to 'maharashtra_election_results_all_combined.csv'")
else:
    print("No data was extracted!")

# Step 7: Close the Selenium browser
driver.quit()