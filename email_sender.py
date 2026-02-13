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
    <body>
        <h2>Today's Job Recommendations</h2>
        <p>Found {len(jobs)} jobs based on your criteria.</p>
        <table border="1" cellpadding="10" cellspacing="0" style="border-collapse: collapse; width: 100%;">
            <tr style="background-color: #f2f2f2;">
                <th>Job Title</th>
                <th>Company</th>
                <th>Location</th>
                <th>Link</th>
            </tr>
    """
    
    for job in jobs:
        html_content += f"""
            <tr>
                <td>{job.get('title')}</td>
                <td>{job.get('company_name')}</td>
                <td>{job.get('location')}</td>
                <td><a href="{job.get('apply_options', [{}])[0].get('link', '#')}">Apply Now</a></td>
            </tr>
        """
    
    html_content += """
        </table>
        <br>
        <p><i>Sent automatically by your AI Agent.</i></p>
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
