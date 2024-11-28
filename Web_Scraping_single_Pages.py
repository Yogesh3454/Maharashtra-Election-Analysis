from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Set up Selenium WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed
url = "https://results.eci.gov.in/ResultAcGenNov2024/partywisewinresult-743S13.htm"  # Replace with the URL
driver.get(url)

# Step 2: Wait for the table to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//table"))  # Wait until the table is present
)

# Step 3: Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Step 4: Extract table data
table = soup.find('table')  # Locate the main table
if table:
    rows = table.find_all('tr')  # Get all rows
    data = []
    for row in rows:
        columns = row.find_all('td')  # Get all columns
        if columns:  # Only process rows with columns
            data.append([col.text.strip() for col in columns])
else:
    print("No table found!")

# Step 5: Create a DataFrame
column_names = ['S.No','Constituency', 'Winning Candidate', 'Total Votes', 'Margin', 'Status']  # Adjust based on table structure
df = pd.DataFrame(data, columns=column_names[:len(data[0])])  # Match columns with scraped data

# Step 6: Save the data to a CSV file
df.to_csv('Independent.csv', index=False, encoding='utf-8')
print("Data extracted and saved to 'Independent.csv'.")

# Close the WebDriver
driver.quit()