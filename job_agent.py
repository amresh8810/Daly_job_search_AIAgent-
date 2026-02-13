import requests
import json
import csv
from datetime import datetime
import os
import config
from email_sender import send_job_email

# Settings from config.py
SERP_API_KEY = config.SERP_API_KEY
JOB_KEYWORDS = config.JOB_KEYWORDS
JOB_LOCATION = config.JOB_LOCATION

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
        print(f"Error searching jobs: {e}")
        return []

def save_jobs(jobs):
    if not jobs:
        return

    filename = "all_jobs_list.csv"
    headers = ["Date", "Job Title", "Company", "Location", "Salary", "Apply Link"]
    file_exists = os.path.isfile(filename)
    
    try:
        with open(filename, mode='a', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            if not file_exists:
                writer.writeheader()
            
            for j in jobs:
                # 1. Try to get salary from API extensions
                salary = j.get("detected_extensions", {}).get("salary")
                
                # 2. If not found, look for "LPA", "Annual", or "Salary" in description
                if not salary:
                    description = j.get("description", "").lower()
                    import re
                    # Regex to find patterns like 5-10 LPA or 500,000 - 800,000
                    salary_match = re.search(r'(\d+[\d,]*\s*(?:-|to)\s*\d+[\d,]*\s*(?:lpa|per year|annum))', description)
                    if salary_match:
                        salary = salary_match.group(0).upper()
                
                if not salary:
                    salary = "Approx. 6-12 LPA (Market Avg)" if "analyst" in j.get("title", "").lower() else "Approx. 10-20 LPA (Market Avg)"
                
                writer.writerow({
                    "Date": datetime.now().strftime("%Y-%m-%d"),
                    "Job Title": j.get("title"),
                    "Company": j.get("company_name"),
                    "Location": j.get("location"),
                    "Salary": salary,
                    "Apply Link": j.get("apply_options", [{}])[0].get("link", "No link")
                })
        print(f"Saved {len(jobs)} jobs to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

if __name__ == "__main__":
    if not SERP_API_KEY or "PASTE" in SERP_API_KEY:
        print("⚠️ Warning: SERP_API_KEY not found. Search might fail.")
    
    # 1. Search for jobs
    results = search_jobs()
    
    if results:
        top_jobs = results[:10] # Top 10 jobs pick karein
        
        # 2. Save to CSV
        save_jobs(top_jobs)
        
        # 3. Send Email
        print("Sending email update...")
        send_job_email(top_jobs)
    else:
        print("No new jobs found today.")
