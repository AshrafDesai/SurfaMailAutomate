import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_advertising_email(sender_email, sender_password, recipient_list):
    """
    Sends a visually appealing and professional advertising email with a banner and aligned sections.
    """
    # Email subject and body with advanced styling
    subject = "Where Innovation Meets Durability: SurfaTech Integrated is Your Solution"
    body = """
    <html>
    <body style="margin: 0; padding: 0; font-family: Arial, sans-serif; color: #333;">
        <!-- Full-width Banner -->
        <div style="background-color: #f4f4f4; text-align: center; padding: 10px;">
            <img src="https://surfatechintesoln.netlify.app/img/about1.png" 
                 alt="SurfaTech Banner" style="max-width: 100%; height: auto;">
        </div>
        
        <!-- Main Content Section -->
        <div style="padding: 20px; background-color: #ffffff;">
            <h1 style="color: #4CAF50; text-align: center; font-size: 24px; margin: 0;">Elevate Your Products with Precision Finishing</h1>
            <p style="text-align: center; font-size: 16px; margin: 10px 0;">
                Discover cutting-edge solutions for <strong>powder coating</strong>, <strong>spray gun sales</strong>, and customized surface treatments.
            </p>
            
            <!-- Features Section -->
            <div style="display: flex; flex-wrap: wrap; justify-content: space-around; margin: 20px 0;">
                <!-- Feature 1 -->
                <div style="flex: 1; padding: 10px; text-align: center; max-width: 200px;">
                    <img src="https://5.imimg.com/data5/SELLER/Default/2022/9/YE/WU/VD/46243521/steel-powder-coating-service.jpeg" 
                         alt="Powder Coating" style="width: 100px; height: 100px; border-radius: 50%;">
                    <h3 style="color: #333;">Powder Coating</h3>
                    <p style="font-size: 14px;">Durable, eco-friendly finishes that last.</p>
                </div>
                <!-- Feature 2 -->
                <div style="flex: 1; padding: 10px; text-align: center; max-width: 200px;">
                    <img src="https://5.imimg.com/data5/SELLER/Default/2021/12/VI/XW/CU/2348807/wagner-flexio-590-handheld-paint-sprayer-500x500.jpg" 
                         alt="Spray Gun Sales" style="width: 100px; height: 100px; border-radius: 50%;">
                    <h3 style="color: #333;">Spray Gun Sales</h3>
                    <p style="font-size: 14px;">Top-quality products with expert support.</p>
                </div>
                <!-- Feature 3 -->
                <div style="flex: 1; padding: 10px; text-align: center; max-width: 200px;">
                    <img src="https://www.zhyao-coatingline.com/data/watermark/main/20240710/668e425698856_.webp" 
                         alt="Custom Solutions" style="width: 100px; height: 100px; border-radius: 50%;">
                    <h3 style="color: #333;">Custom Solutions</h3>
                    <p style="font-size: 14px;">Tailored services to meet your unique needs.</p>
                </div>
                <!-- Feature 4 -->
                <div style="flex: 1; padding: 10px; text-align: center; max-width: 200px;">
                    <img src="https://surfatechintesoln.netlify.app/img/service3.jpg" 
                         alt="Paint Booth Setup" style="width: 100px; height: 100px; border-radius: 50%;">
                    <h3 style="color: #333;">Paint Booth Setup</h3>
                    <p style="font-size: 14px;">Assistance in setting up paint booths with new or used equipment.</p>
                </div>
                <!-- Feature 5 -->
                <div style="flex: 1; padding: 10px; text-align: center; max-width: 200px;">
                    <img src="https://surfatechintesoln.netlify.app/img/service4.jpg" 
                         alt="Repair Services" style="width: 100px; height: 100px; border-radius: 50%;">
                    <h3 style="color: #333;">Repair Services</h3>
                    <p style="font-size: 14px;">On-site and in-house repair services for powder coating equipment.</p>
                </div>
            </div>
            
            <!-- Call-to-Action Section -->
            <div style="text-align: center; margin: 30px 0;">
                <p style="font-size: 16px;">Visit our website to learn more about how we can help you achieve exceptional surface finishing results.</p>
                <a href="https://surfatechintesoln.netlify.app/" 
                   style="display: inline-block; background-color: #4CAF50; color: #ffffff; text-decoration: none; padding: 15px 25px; font-size: 16px; border-radius: 5px;">
                   Explore Our Solutions
                </a>
            </div>
        </div>
        
        <!-- Contact Section -->
        <div style="background-color: #4CAF50; color: #ffffff; padding: 20px; text-align: center;">
            <h2 style="margin: 0;">Contact Us Today!</h2>
            <p style="margin: 5px 0;">📞 Phone: +91 8928292594 | 📧 Email: <a href="mailto:surfaintsoln@gmail.com" style="color: #ffffff; text-decoration: underline;">surfaintsoln@gmail.com</a></p>
            <p style="margin: 5px 0;">🌐 <a href="https://surfatechintesoln.netlify.app/" style="color: #ffffff; text-decoration: underline;">Visit our Website</a></p>
        </div>
    </body>
    </html>
    """
    
    try:
        # Initialize SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email to each recipient
        for recipient in recipient_list:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = subject
            msg["From"] = sender_email
            msg["To"] = recipient
            msg.attach(MIMEText(body, "html"))
            server.sendmail(sender_email, recipient, msg.as_string())
            print(f"Email sent successfully to {recipient}")

        server.quit()
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
if __name__ == "__main__":
    sender_email = "surfaintsoln@gmail.com"
    sender_password = "aewd ubet rwzn jpqy"  # Use your app-specific password
    recipient_list = [
        "ashrafdesai6598@gmail.com",
        "mndesai1964@gmail.com"
        "ashrafdesai21@gmail.com"
    ]

    send_advertising_email(sender_email, sender_password, recipient_list)
