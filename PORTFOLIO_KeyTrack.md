# 👁️ KeyTrack – Python-Based Forensic Input Logger for Security Awareness

## 🔍 **Introduction**

As a final-year Computer Science student passionate about security and automation, I created **KeyTrack**, a forensic key event monitoring tool. This project demonstrates my ability to build real-world security utilities while applying concepts of **system monitoring, user context logging, secure data handling**, and **automated reporting**.

**KeyTrack** is an educational tool that:
- Captures keystrokes across applications
- Tracks the currently focused window title
- Logs data with timestamps in a forensically relevant format
- Captures screenshots during suspicious input patterns
- Generates timeline-based HTML reports
- Supports secure logging through encryption

## ⚙️ **Why I Built This**

Security professionals often rely on user behavior analysis and timeline reconstruction for post-breach investigations. I wanted to simulate part of that workflow — not just for technical understanding but also to demonstrate how forensic tools are engineered with precision.

This project ties together:
- Python's system-level capabilities
- Modular design and input monitoring
- Visual reporting for human-readable evidence

## 🧱 **Tech Stack**
- 🐍 **Python** for input capture and automation
- 🖱️ **pynput** for keyboard listening
- 🧠 **pywin32** for window tracking
- 🖼️ **Pillow** for screenshot capture
- 🗝️ **Cryptography** for secure logging
- 🧾 **Jinja2** for timeline-based HTML reporting

## 🔬 **How It Works**

### 1. 🎯 **Keyboard Logging**
Captures all keyboard input using `pynput.Listener`, and logs each key press in real-time.

```python
from pynput.keyboard import Listener
```

### 2. 🪟 **Active Window Tracking**
Detects which window is focused at the time of each input (e.g., Chrome, Notepad) using `win32gui`.

```python
win32gui.GetWindowText(win32gui.GetForegroundWindow())
```

### 3. 🕓 **Timestamped Logging**
Each entry is stored with a precise timestamp for forensic sequencing.

### 4. 📸 **Conditional Screenshot Capture**
Takes a screenshot when suspicious activity is detected — e.g., user presses Enter.

### 5. 🔐 **Encrypted Storage (Optional)**
Uses `cryptography.fernet` to encrypt log contents for privacy and safe sharing.

### 6. 📝 **HTML Report Generation**
After logging, a timeline-style report is generated showing:
- When and where inputs occurred
- Which keys were pressed
- Visual structure for easier analysis

## 🧪 **Sample CLI Use**

```bash
# Run key monitoring
python main.py

# After logging some input, generate a report
python reporter.py
```

## 📁 **Project Structure**
- `main.py` – Entry point
- `logger.py` – Handles keystroke and context logging
- `tracker.py` – Tracks active windows
- `screenshots/` – Captures during key events
- `encryptor.py` – Secures logs using Fernet
- `reporter.py` – Creates HTML forensic timeline
- `templates/report.html` – Jinja2 report template

## 💡 **What I Learned**

- How keyloggers function for security research
- Real-time logging with window context
- Event-driven screenshot capture in Python
- How to structure log data for timeline analysis
- Ethical application of surveillance tools for learning

## 🧠 **What’s Next?**
To enhance KeyTrack further:
- Export HTML to PDF
- Add ML-based anomaly detection
- Remote log syncing
- Slack alert for suspicious combinations

## 🔗 **Project Access**
🧾 GitHub: [https://github.com/yourusername/keytrack-forensic-monitor](https://github.com/yourusername/keytrack-forensic-monitor)  
📸 Screenshots & Demos: (optional)

## 🙋‍♂️ About Me
I’m a final-year B.Tech CSE student passionate about security automation, OS internals, and ethical hacking. KeyTrack showcases my drive to explore system-level security programming and apply it to practical forensics tooling.