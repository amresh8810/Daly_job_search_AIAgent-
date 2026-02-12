import requests
import json
import config

def debug_links():
    print(f"DEBUG: Searching for '{config.JOB_KEYWORDS}'...")
    
    params = {
        "engine": "google_jobs",
        "q": config.JOB_KEYWORDS,
        "location": config.JOB_LOCATION,
        "api_key": config.SERP_API_KEY
    }

    response = requests.get("https://serpapi.com/search", params=params)
    results = response.json()
    jobs = results.get("jobs_results", [])
    
    if jobs:
        print("\n--- FIRST 2 JOBS RAW DATA ---")
        for i, job in enumerate(jobs[:2]):
            print(f"\nJob {i+1}: {job.get('title')}")
            print(f"Apply Options: {json.dumps(job.get('apply_options'), indent=2)}")
            print(f"Related Links: {json.dumps(job.get('related_links'), indent=2)}")
    else:
        print("No jobs found in Debug mode.")

if __name__ == "__main__":
    debug_links()
