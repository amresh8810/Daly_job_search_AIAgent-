import requests
import json
import config
import csv
import os

demo_file = "demo_test.csv"

def run_demo():
    print("--- LIVE DEMO ---")
    print(f"Searching for: {config.JOB_KEYWORDS}")
    
    params = {
        "engine": "google_jobs",
        "q": config.JOB_KEYWORDS,
        "location": config.JOB_LOCATION,
        "api_key": config.SERP_API_KEY
    }

    try:
        response = requests.get("https://serpapi.com/search", params=params)
        jobs = response.json().get("jobs_results", [])[:3]

        with open(demo_file, mode='w', newline='', encoding='utf-8-sig') as file:
            writer = csv.DictWriter(file, fieldnames=["Title", "Company", "Location"])
            writer.writeheader()
            for job in jobs:
                title = job.get("title", "N/A")
                company = job.get("company_name", "N/A")
                location = job.get("location", "N/A")
                writer.writerow({"Title": title, "Company": company, "Location": location})
                print(f"Found: {title} at {company}")

        print("\nSUCCESS: Data saved to demo_test.csv")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_demo()
