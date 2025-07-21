# Kickstarter Data Analysis & Insights

This project explores a dataset of over 370,000 Kickstarter projects launched between 2009 and 2017. The goal is to uncover meaningful insights about project success rates, backers, funding dynamics, and investor-attractive categories using Python and pandas.

##  Project Overview

Using exploratory data analysis (EDA), we answer key questions:

- Which categories have the highest success rates?
- How has project success evolved over time?
- What project achieved the highest funding-to-goal ratio?
- What categories attract the most backers and pledges?
- Which types of projects are most interesting for potential investors?

The code cleans and transforms the data, creates custom metrics like `Goal_Completion_Percent`, and extracts actionable insights without using visualizations (ideal for backend analysis or further dashboard integration).

##  Key Insights

- **Top categories by success rate**: Theater, Dance, Music, Comics
- **Average backers**: Successful projects attract significantly more backers than failed ones
- **Top investor-attractive projects**: Those with high completion %, strong backer support, and campaign momentum
- **Success trend**: The success rate declined slightly after 2014 as competition increased

##  Technologies Used

- Python
- pandas
- datetime
- Jupyter / VS Code (for testing)

##  Dataset Description

The dataset includes the following fields for each project:

- `Name` – Name of the Kickstarter project
- `Category` – Main category of the project
- `Launched` – Project launch date
- `Deadline` – Project deadline date
- `Goal` – Fundraising goal in USD
- `Pledged` – Amount of money pledged by backers
- `Backers` – Number of backers
- `State` – Project outcome (`Successful`, `Failed`, `Canceled`, etc.)
- `Country` – Country of origin

Additional derived fields include:

- `Goal_Completion_Percent` – Pledged / Goal * 100
- `Launch_Year` – Extracted from `Launched`
- `Campaign_Length` – Days between launch and deadline

##  Dataset Source

-  [Maven Analytics - Kickstarter Projects Dataset](https://mavenanalytics.io/project/19318)
- Contains over 375,000 Kickstarter projects (2009–2017)

##  How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/kickstarter-data-analysis-insights.git
   ```
2. Place `kickstarter_projects.csv` in the root folder.
3. Run `kickstarter_analysis.py` using Python 3.7+:
   ```bash
   python kickstarter_analysis.py
   ```

