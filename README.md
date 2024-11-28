# Maharashtra-Election-Analysis

## Overview
This project focuses on analyzing the recent Maharashtra Legislative Assembly election results. Using data scraped from the Election Commission website, we have created a comprehensive Power BI dashboard to visualize and understand the election trends, party performances, and candidate results.

This project demonstrates the use of **Python for web scraping** and **Power BI for data visualization,** providing actionable insights into election outcomes.

## Objective
1) Scrape and process election data from the official Election Commission website.
2) Perform data cleaning and preprocessing.
3) Create a multi-page, interactive Power BI dashboard.
4) Present election insights, including:
   - Party-wise seat distribution.
   - Candidate-wise performance.
   - Regional trends and constituency analysis.
   
## Key Features
### Interactive Dashboard:
[View the Interactive Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiZmFiMjJmNTUtNWM5NC00OGEwLTk4ZjYtZTJjOWYyNjVmN2FjIiwidCI6IjlmYzdjOWQ0LWQ2MjctNGRmNy05NGE3LWQwMDhhYzQ3MDM4NyJ9)

### Python Web Scraping:
- Extracted detailed election data such as party names, seat counts, leading and trailing candidates, and constituency-level performance using Python libraries.
- [View Web Scraping Code](https://github.com/Yogesh3454/Maharashtra-Election-Analysis/blob/main/web_scraping_all_pages.py)

### Power BI Dashboard:
- Visualized party-wise seat distribution using bar and pie charts.
- Highlighted top-performing constituencies and candidates.
- Regional analysis using geographical maps.

## Data Sources
- Election data scraped from the Election Commission of India website.
- [Scraped Data is Here...](https://github.com/Yogesh3454/Maharashtra-Election-Analysis/blob/main/Election%20Result.csv)
  
## Steps to Reproduce
### 1) Web Scraping:
- Download the Python web scraping script from **Data Source*.
- Follow the instructions in the script to extract data from the Election Commission website.

### 2) Data Cleaning:
- Use Python or Power BI to clean and preprocess the scraped data (e.g., handle missing values, rename columns).

### 3) Dashboard Creation:
- Import the cleaned data into Power BI.
- Design visualizations for key insights:
  - **Party-wise Seat Distribution:** Bar and pie charts.
  - **Regional Trends:** Maps to display constituencies.
  - **Candidate Analysis:** Tables with leading/trailing candidates.
    
### 4) Analysis:
- Use DAX to calculate additional metrics, such as vote share percentage and seat gains/losses.
- Publish the dashboard for stakeholder access.

## Project Screenshots
**Party-Wise Seat Distribution:**
  - BJP+SHS+NCP [BJP+SHS+NCP](image.png)

  - INC+SHSUBT+NCPSP [INC+SHSUBT+NCPSP](image 1.png)
(Bar chart)[image 2 - Copy.png]
(Partywise Seates)[image 3.png]

## Interactive Dashboard
![View Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiZmFiMjJmNTUtNWM5NC00OGEwLTk4ZjYtZTJjOWYyNjVmN2FjIiwidCI6IjlmYzdjOWQ0LWQ2MjctNGRmNy05NGE3LWQwMDhhYzQ3MDM4NyJ9)

## Results
- Comprehensive analysis of party performances:
  - BJP secured the highest seats (132), followed by SHS (57) and NCP (41).
  - Seat distribution among alliances:
    - **BJP+SHS+NCP:** 79.86% of total seats.
    - **INC+NCPSP+SHSUBT:** 15.97% of total seats.
    - **Others:** 4.17% of total seats.
- Key constituencies analyzed for their competitive dynamics.
- Interactive geographical and categorical insights.

## Technologies Used
- **Web Scraping:** Python (BeautifulSoup, pandas, Selenium).
- **Data Visualization:** Power BI.
- **Data Processing:** Python, Power BI.

## How to Run the Project
**Step 1: Install Power BI Desktop**
Download and install Power BI Desktop from the official Microsoft website.
Ensure that your system meets the minimum requirements to run Power BI.

**Step 2: Download the Project Files**
Clone the project repository or download it as a ZIP file:
```bash
git clone https://github.com/your-repository/project-link.git
```
Extract the ZIP file (if downloaded) to your local system.

**Step 3: Open the Power BI File**
Navigate to the folder containing the project files.
Locate the .pbix file (e.g., Maharashtra_Election_Analysis.pbix).
Double-click the .pbix file, or open it from Power BI Desktop:
Launch Power BI Desktop.
Go to File > Open and select the .pbix file.

**Step 4: Connect to the Data Source (Optional)**
If the dataset is stored locally or hosted online, Power BI may prompt you to verify or update the data source.
Update the file path or web link for the data source if required:
Go to Transform Data > Data Source Settings.
Update the path or credentials as needed.

**Step 5: Refresh the Data**
Click the Refresh button in Power BI to load the latest data.
Ensure the data connections are valid and the required files (e.g., CSV or database) are accessible.

**Step 6: Explore the Dashboard**
Navigate through the pages of the dashboard to explore various visualizations:
Party-wise Seat Distribution.
Regional Trends and Maps.
Candidate-Wise Performance.
Use slicers, filters, and tooltips for interactive analysis.

**Step 7: Publish the Dashboard (Optional)**
To share the dashboard:
Go to File > Publish > Publish to Power BI Service.
Log in with your Power BI account.
Select a workspace and upload the file.
Share the link to your dashboard with stakeholders.

**Step 8: Troubleshooting**
- Missing Data Source: Check if the data file (e.g., CSV or database) is in the correct location.
- Data Refresh Issues: Verify network connectivity and data access permissions.
- Performance: Optimize the data model by reducing the size of datasets or disabling unnecessary visualizations.



## LinkedIn Post
[View LinkedIn Post.](https://www.linkedin.com/posts/yogeshgunjal75_doc-activity-7267454239839281152-lkS9/?utm_source=share&utm_medium=member_android)



## Future Enhancements
- Automate data updates directly from the Election Commission website.
- Add sentiment analysis based on public/social media data about the elections.
- Enhance geographical visualizations with constituency demographics.

## Contributors
- **Name:** Yogesh Gunjal
- **Role:** Data Analyst
- **Email:** yogeshgunjal75@gmail.com
