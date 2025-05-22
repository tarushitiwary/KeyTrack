# KeyTrack - Forensic Input Monitoring & Incident Response Tool

**KeyTrack** is a comprehensive, Python-based forensic tool designed for ethical hacking labs, security awareness training, and digital forensics education. It records keyboard inputs, captures contextual metadata, generates visual HTML reports, and provides an extendable architecture for cyber defense simulation.

---

## 🚀 Features

### 🔍 Keystroke Logging
Captures every key pressed along with the exact timestamp and the name of the currently focused application window. This emulates real-world forensic scenarios where understanding user activity across time is crucial.

### 🧭 Active Window Tracking
Uses Windows APIs to log which program was active at the moment of each keystroke. Helps correlate user input with specific apps (e.g., login into browsers, terminal, or messaging tools).

### 🖼️ Screenshot Capture (Event-Driven)
Takes a screenshot automatically on high-signal key events (like `Enter`) to provide visual context for user actions. Screenshots are timestamped and linked in reports.

### 📑 HTML Timeline Reports
Generates visually enriched HTML reports using Jinja2 templating. Each report is mobile-friendly, includes search/filter functionality, and presents inputs in a structured forensic timeline.

### 🔐 Encrypted Log Option
Supports log encryption using the `cryptography` library’s Fernet module. Useful for securely transmitting logs or storing sensitive data during incident investigations.

### 📊 Modular Architecture
Each feature is modular: keystroke logging, window tracking, screenshot capture, and reporting live in separate Python modules. This makes it easy to test, replace, or expand each part.

### 🔄 Cross-Compatible with Security Automation
Can be easily integrated into larger detection or automation workflows, such as auto-generating reports post-breach simulation or piping logs to alerting systems.

### 📁 Screenshot and Log Management
Organizes all logs in the `logs/` folder and screenshots in the `screenshots/` folder, with file names structured by timestamp for easy correlation.

### 🌐 Optional IP Metadata
Expandable to log system metadata such as IP address, hostname, or active user—ideal for tracking in multi-user training environments.

---

## 🛠️ Installation

### 🔧 Requirements
- Python 3.10+
- pip
- Windows OS (for active window tracking with pywin32)

### 📦 Setup & Dependencies

```bash
git clone [https://github.com/tarushitiwary/KeyTrack]
cd KeyTrack
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\activate
pip install -r requirements.txt
