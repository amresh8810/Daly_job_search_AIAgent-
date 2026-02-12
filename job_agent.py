import requests
import json
import csv
from datetime import datetime
import os

# GitHub Secrets ya local config se API key lena
SERP_API_KEY = os.getenv("SERP_API_KEY")
JOB_KEYWORDS = os.getenv("JOB_KEYWORDS", "Web Developer")
JOB_LOCATION = os.getenv("JOB_LOCATION", "India")

def search_jobs():
    print(f"Searching for '{JOB_KEYWORDS}' in '{JOB_LOCATION}'...")
    params = {
        "engine": "google_jobs",
        "q": JOB_KEYWORDS,
        "location": JOB_LOCATION,
        "api_key": SERP_API_KEY
    }
    try:
        response = requests.get("https://serpapi.com/search", params=params)
        return response.json().get("jobs_results", [])
    except Exception as e:
        print(f"Error: {e}")
        return []

def save_jobs(jobs):
    if not jobs:
        print("No jobs found.")
        return

    filename = "all_jobs_list.csv"
    headers = ["Date", "Job Title", "Company", "Location", "Apply Link"]
    file_exists = os.path.isfile(filename)
    
    try:
        with open(filename, mode='a', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            if not file_exists:
                writer.writeheader()
            
            for j in jobs:
                writer.writerow({
                    "Date": datetime.now().strftime("%Y-%m-%d"),
                    "Title": j.get("title"),
                    "Company": j.get("company_name"),
                    "Location": j.get("location"),
                    "Apply Link": j.get("apply_options", [{}])[0].get("link", "No link")
                })
        print(f"Successfully saved {len(jobs)} jobs to {filename}")
    except Exception as e:
        print(f"Error saving: {e}")

if __name__ == "__main__":
    if not SERP_API_KEY:
        print("Error: SERP_API_KEY not found! Set it in GitHub Secrets.")
    else:
        results = search_jobs()
        save_jobs(results[:10])
