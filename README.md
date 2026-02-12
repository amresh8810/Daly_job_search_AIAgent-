# 🤖 AI Job Search Agent (Daily Auto-Update)

Ye ek powerful AI Agent hai jo rozana automatically internet se jobs dhoondhta hai aur unhe ek Excel file (`all_jobs_list.csv`) mein save kar deta hai. 

## ✨ Features
- **Daily Automated Search:** GitHub Actions ka use karke ye rozana subah 9:30 AM (IST) par chalta hai.
- **Direct Apply Links:** Har job ke saath uska direct application page link hota hai.
- **Local & Cloud Sync:** Aap ise apne computer par bhi chala sakte hain aur ye GitHub par bhi auto-update hota hai.
- **Excel format:** Saara data `CSV` format mein save hota hai jo Excel mein asani se khul jata hai.

## 🛠️ Tech Stack
- **Python** (Main logic)
- **SerpApi** (Google Jobs data ke liye)
- **GitHub Actions** (Automation ke liye)

## 🚀 Setup Instructions (For Beginners)

### 1. API Key Setup
- [SerpApi](https://serpapi.com/) par free account banayein.
- GitHub repo ki **Settings > Secrets > Actions** mein jayein.
- Ek naya secret add karein: `SERP_API_KEY` aur apni key wahan paste kar dein.

### 2. Local Run (Computer par chalane ke liye)
Agar aap ise apne computer par manually chalana chahte hain:
1. `pip install requests` karein.
2. `config.py` mein apni API key rakhein.
3. `run_job_agent.bat` file par double click karein.

## 📁 File Structure
- `job_agent.py`: Main AI logic.
- `all_jobs_list.csv`: Yahan aapki saari jobs save hoti hain.
- `.github/workflows/daily_jobs.yml`: Automation ka schedule.

---
Made with ❤️ by [Amresh](https://github.com/amresh8810)
