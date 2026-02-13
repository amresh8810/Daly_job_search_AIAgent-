import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

def send_job_email(jobs):
    if not jobs:
        print("No jobs to email.")
        return

    # Create Message
    msg = MIMEMultipart()
    msg['From'] = config.EMAIL_USER
    msg['To'] = config.RECEIVER_EMAIL
    msg['Subject'] = f"🚀 Daily Job Update: {len(jobs)} New Jobs Found!"

    # Create Email Body (HTML)
    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif;">
        <h2 style="color: #004a99;">Today's Recommendations By Amresh Kumar</h2>
        <p>Found {len(jobs)} jobs based on your criteria of Data Analyst and Data Scientist roles in India.</p>
        <table border="1" cellpadding="10" cellspacing="0" style="border-collapse: collapse; width: 100%; background-color: #e6f2ff;">
            <tr style="background-color: #004a99; color: white;">
                <th>Job Title</th>
                <th>Company</th>
                <th>Location</th>
                <th>Salary</th>
                <th>Link</th>
            </tr>
    """
    
    for job in jobs:
        # Improved salary extraction for email
        salary = job.get("detected_extensions", {}).get("salary")
        if not salary:
            description = job.get("description", "").lower()
            import re
            salary_match = re.search(r'(\d+[\d,]*\s*(?:-|to)\s*\d+[\d,]*\s*(?:lpa|per year|annum))', description)
            if salary_match:
                salary = salary_match.group(0).upper()
        
        if not salary:
            salary = "Approx. 6-12 LPA" if "analyst" in job.get("title", "").lower() else "Approx. 10-20 LPA"

        html_content += f"""
            <tr>
                <td>{job.get('title')}</td>
                <td>{job.get('company_name')}</td>
                <td>{job.get('location')}</td>
                <td>{salary}</td>
                <td><a href="{job.get('apply_options', [{}])[0].get('link', '#')}" style="color: #004a99; font-weight: bold;">Apply Now</a></td>
            </tr>
        """
    
    html_content += """
        </table>
        <br>
        <p><i>Sent automatically by your AI Job Agent. Cheers, Amresh!</i></p>
    </body>
    </html>
    """
    
    msg.attach(MIMEText(html_content, 'html'))

    try:
        # Connect to Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(config.EMAIL_USER, config.EMAIL_PASS)
        server.send_message(msg)
        server.quit()
        print(f"Email sent successfully to {config.RECEIVER_EMAIL}")
    except Exception as e:
        print(f"Failed to send email: {e}")
