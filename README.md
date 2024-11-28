# Email Campaign Script for SurfaTech Integrated Solutions  

This Python script enables the sending of professional, visually appealing advertising emails to a large number of recipients. It is designed for **SurfaTech Integrated Solutions** to showcase their innovative surface treatment solutions, including powder coating, spray gun sales, and customized services. The email subject is **"Enhance Your Surface Treatment with SurfaTech Integrated Solutions"** and the body of the email contains a beautifully designed HTML layout that highlights the company's key services and offerings.

---

## Features  
- **HTML Email Support**: Sends beautifully designed HTML emails with images and banners.  
- **Customizable Content**: Easily update the subject line, email body, and branding elements.  
- **Batch Emailing**: Sends emails to multiple recipients in a single execution.  
- **Error Handling**: Provides informative error messages for failed email deliveries.  

---

## Prerequisites  
To use this script, ensure you have the following installed and configured:  
- **Python 3.x**  
- Required Python Libraries:  
  - `smtplib`  
  - `email`  

---

## Setup  

1. **Clone or Download the Script**  
   Clone this repository or download the script to your local system.

2. **Install Required Libraries**  
   This script uses Python's built-in libraries (`smtplib` and `email`), so no additional installation is necessary.

3. **Set Up an Email Account**  
   Use a Gmail account to send emails. Ensure you have:  
   - Enabled **Less Secure App Access** or generated an **App Password** for security.  
   - Your email and app password ready for use.

4. **Prepare the Recipient List**  
   Add recipient email addresses in the `recipient_list` variable within the script.

---

## Usage  

### **1. Update Sender Information**  
Replace the placeholder values in the script with your email credentials:
python
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"

### **2.Customize the Email Content**
Modify the subject line and body for your email campaign as needed:
Python:
- subject = "Enhance Your Surface Treatment with SurfaTech Integrated Solutions"
- body = "<!-- Your HTML email content goes here -->"

### **3.Run the Script**
Execute the script in your Python environment:

python mail.py
