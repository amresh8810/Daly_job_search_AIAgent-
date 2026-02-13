import os

# API Keys (Priority: Environment Variables, then Hardcoded)
SERP_API_KEY = os.getenv("SERP_API_KEY", "68c5ef20de394832137b30a0e2ca37737f83ae93b861222503bc097e0b9f9dcd")

# Email Configuration
EMAIL_USER = os.getenv("EMAIL_USER", "amreshkumar08797@gmail.com")
EMAIL_PASS = os.getenv("EMAIL_PASS", "ddjsomyxvbuopsqr")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL", "amreshkumar08797@gmail.com")

# Job Search Settings
JOB_KEYWORDS = os.getenv("JOB_KEYWORDS", "Data Analyst OR Data Scientist")
JOB_LOCATION = os.getenv("JOB_LOCATION", "India")

# Google Sheet Integration
GOOGLE_SHEET_URL = "https://script.google.com/macros/s/AKfycbz8NZrJG7nW9i_FB-SmYVUQhKW79O-TYoVXN2fnex2o2MifE9Ojiot_lo4F1ac9o9ZN/exec"
