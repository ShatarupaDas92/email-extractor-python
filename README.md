📧 Email Extractor using Python

> ✅ **Task 3 - CodeAlpha Internship**
>
> 🔖 Internship Project: Automate real-life repetitive tasks with Python  
> 🚀 Task Name: Email Extraction from a `.txt` file  
> 👩‍💻 Submitted by: Shatarupa Das

📌 Project Overview
This project automates the task of extracting **email addresses** from a `.txt` file and saving them to another file using **Python**. It uses regular expressions (regex) to identify email patterns and handles file reading/writing seamlessly.

**Tech Stack & Concepts Used:**
- Python
- Regular Expressions (`re`)
- File Handling
- `os` module
- Basic Automation

🗂️ Folder Structure

email-extractor-python/

├── input.txt # Input file containing raw text with emails

├── output.txt # Output file to save extracted emails

├── extract_emails.py # Python script to automate the task

├── README.md # Project documentation

🚀 How It Works
1. Reads content from `input.txt`.
2. Extracts all valid email addresses using a regex pattern.
3. Removes duplicates and sorts them.
4. Saves the cleaned list to `output.txt`.

📥 Sample Input (`input.txt`)
Contact us at hr@company.org or info@service.net
Also reach out to shatarupadas15@gmail.com for any collaboration!

📤 Sample Output (`output.txt`)
hr@company.org
info@service.net
shatarupadas15@gmail.com


🔄 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/email-extractor-python.git
2. Navigate to the folder:

bash

  Copy
  
  Edit
  
  cd email-extractor-python
  
3. Run the script:

bash

  Copy
  
  Edit
  python extract_emails.py
