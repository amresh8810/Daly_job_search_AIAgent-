# 🤖 AI Job Search Agent (Daily Auto-Update)

A powerful AI Agent that automatically searches for jobs on the internet daily and saves them into an Excel-ready file (`all_jobs_list.csv`).

## ✨ Features
- **Daily Automated Search:** Runs daily at 9:30 AM (IST) using GitHub Actions.
- **Direct Apply Links:** Includes direct application page links for every job found.
- **Local & Cloud Sync:** You can run it on your local machine or let it run automatically on GitHub.
- **Excel Compatible:** All data is saved in `CSV` format, making it easy to open in Excel or Google Sheets.

## 🛠️ Tech Stack
- **Python** (Core logic)
- **SerpApi** (Google Jobs data source)
- **GitHub Actions** (Workflow automation)

## 🚀 Setup Instructions (For Beginners)

### 1. API Key Setup
- Create a free account on [SerpApi](https://serpapi.com/).
- Navigate to your GitHub repository **Settings > Secrets and variables > Actions**.
- Add a new repository secret named `SERP_API_KEY` and paste your API key there.

### 2. Local Run (Running on your computer)
If you want to run the agent manually on your machine:
1. Install requirements: `pip install requests`
2. Set your API key in `config.py`.
3. Double-click the `run_job_agent.bat` file.

## 📁 File Structure
- `job_agent.py`: Main AI source code.
- `all_jobs_list.csv`: Destination file where all jobs are saved.
- `.github/workflows/daily_jobs.yml`: Automation schedule configuration.

---
Made with ❤️ by [Amresh](https://github.com/amresh8810)
