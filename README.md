📘 Simple Web Scraper
A beginner-friendly, end-to-end web scraping project that downloads web pages, extracts useful information, and saves the results into a clean CSV file.
This project is designed to build your fundamentals in requests, HTML parsing, BeautifulSoup, and CSV creation with pandas.


🚀 Features
Fetches HTML content from any website
Parses and extracts structured information
Stores results into a clean CSV
Error-handled, beginner-friendly code
Fully open for extension and improvements


🧠 What You Will Learn
This mini-project teaches you the real thinking process of a data engineer:
How to break a project into small steps
How to collect data from the internet
How to parse HTML tags and extract information
How to save clean tabular data using pandas
How to create a modular Python script
How to think logically and build code from scratch

📂 Project Structure
simple_web_scraper/
│
├── scraper.py          # Main Python script
├── requirements.txt    # List of dependencies
└── output/
    └── books.csv       # Final extracted CSV file (generated)

📦 Installation
1. Clone this repository
git clone https://github.com/<your-username>/simple_web_scraper.git
cd simple_web_scraper
2. Create and activate a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
3. Install all dependencies
pip install -r requirements.txt


▶️ Usage
Run the scraper:
python scraper.py
After running, you will see a file generated:
output/books.csv
It contains:
Title	Price	Availability	Rating


🧩 How It Works (High-Level Logic)
1. Load the webpage
We use requests to download the HTML.

2. Parse HTML
We use BeautifulSoup to navigate tags like h3, p, img, etc.

3. Extract required fields
For each product/book, we collect:
Title
Price
Availability
Rating

4. Create a DataFrame
All extracted data gets converted to a pandas DataFrame.

5. Save it
We export the final results to output/books.csv.


🛠️ Technologies Used
Python 3
Requests → for downloading pages
BeautifulSoup4 → for parsing HTML
Pandas → for generating CSV output

📌 Example Output (CSV)
title,price,availability,rating
"A Light in the Attic","£51.77","In stock","Three"
"Tipping the Velvet","£53.74","In stock","One"


🧱 Extend This Project
Once you finish the base version, try adding:
Pagination (scrape all pages 1–50)
Download images
Store results in SQLite
Add CLI arguments (URL input)
Convert CSV → JSON
Each extension makes you more confident in writing your own logic.


👩‍💻 Author
Anika
Data Engineer | ETL Developer | Learner by Doing
Building skills through practical, real-world mini-projects.


⭐ If you like this project
Give the repo a ★ on GitHub and try the next mini-project!