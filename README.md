# send-auto-emails
This will use browser by using the web socket link and send email from python automatically by using the selenium.

## Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

## Project Setup
### 1. Clone the Repository
```bash
git clone https://github.com/sohail-eng/send-auto-emails.git
cd send-auto-emails
```

### 2. Create a Virtual Environment (Recommended)
#### Windows
```cmd
python -m venv venv
venv\Scripts\activate
```

#### Ubuntu/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Running the Application

#### Setting up files
Before running the application, Please create `emails.txt` and `config.json` files, you can copy from `example-` files.

#### Run Browser
Please run chrome in debug mode, here is the code for linux, please find for windows by yourself.
```commandline
google-chrome --remote-debugging-port=9222 --user-data-dir="C:\chrome-debug"
```
```bash
python main.py
```
