🧩 URL Shortener Web Application

A simple and efficient URL Shortener built with Python, Flask, SQLite, and HTML/CSS.
This application allows users to enter a long URL and instantly receive a short, shareable link.
The system stores URL mappings in a local database and redirects users to the original URL when the short code is accessed.

🚀 Features

Convert long URLs into short, unique codes

Automatic short code generation (letters + numbers)

Database storage using SQLite

Redirect to original URLs using dynamic routing

Error handling for invalid or expired short URLs

Clean and minimal UI built with HTML & Flask templates

🛠️ Tech Stack

Python 3

Flask Framework

SQLite Database

HTML 

📁 Project Structure
url-shortener/
│
├── app.py
├── database.py
│
├── templates/
│   └── index.html
│
└── README.md

⚙️ How It Works

User enters a long URL in the form

The system generates a unique short code

The mapping (long URL ↔ short code) is saved in SQLite

User sees a final short URL like:

http://localhost:5000/aB3x


When someone visits the short URL, the app:

Looks up the long URL

Redirects the browser to the original site

▶️ How to Run the Project Locally
1. Clone the Repository
git clone https://github.com/your-username/url-shortener.git
cd url-shortener

2. Install Dependencies
pip install flask

3. Run the Flask App
python app.py

4. Open in Browser

Visit:

http://127.0.0.1:5000/

🔧 Future Enhancements

Custom short URLs (user-defined)

Analytics (click count, timestamps, IP logs)

User authentication for private links

QR Code generation for short URLs