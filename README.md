# 📧 Email Sender Using Python

This project is a simple **Python script** to send emails using **Gmail's SMTP server**. It securely retrieves email credentials from environment variables and sends a formatted email.

## 🚀 Features
- Sends emails via **Gmail SMTP**.
- Uses **environment variables** for secure credential handling.
- Supports **custom subject and body** for emails.
- Uses **TLS encryption** for secure communication.

---

## 🔧 Setup Instructions

### **1. Clone the Repository**
git clone https://github.com/your-username/email-sender.git
cd email-sender


### **2. Set Up a Virtual Environment (Optional)**
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
# On Windows:
# .venv\Scripts\activate

### **3. Install Required Dependencies**
pip install smtplib

### **4. Set Environment Variables**
Before running the script, set your **Gmail credentials** securely:

#### **On Mac/Linux (Terminal)**
export EMAIL_USER="your-email@gmail.com"
export EMAIL_PASS="your-app-password"

#### **On Windows (Command Prompt)**
set EMAIL_USER=your-email@gmail.com
set EMAIL_PASS=your-app-password

Do not use your real password. Instead, generate an **App Password** in Google Security settings.

### **5. Run the Script**
python email_sender.py


## ⚠️ Troubleshooting

1. Google Blocks the Sign-in**
- Enable **2-Step Verification** in your Google account.
- Generate an **App Password** from [Google App Passwords](https://myaccount.google.com/apppasswords).
- Use the **App Password** instead of your actual email password.
 
 2. SMTP Authentication Error**
- Check if **environment variables** are correctly set (`echo $EMAIL_USER` on Mac/Linux).
- Ensure you have **enabled SMTP access** in your Google account.



Feel free to contribute or report issues! 😊


Let me know if you want any modifications! 

Let me know if you want any modifications! 