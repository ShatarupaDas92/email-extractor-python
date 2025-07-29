import re
import os

def read_input_file(file_path):
    if not os.path.exists(file_path):
        print(f"❌ Error: The file '{file_path}' does not exist.")
        return ""
    with open(file_path, 'r') as file:
        print(f"📂 Reading content from: {file_path}")
        return file.read()


def extract_emails_from_text(text):
    
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    print("🔍 Extracting emails using regex...")
    return re.findall(pattern, text)


def write_emails_to_file(emails, output_path):
    
    unique_emails = sorted(set(emails))
    if not unique_emails:
        print("⚠️ No email addresses found.")
    else:
        with open(output_path, 'w') as file:
            for email in unique_emails:
                file.write(email + "\n")
        print(f"✅ {len(unique_emails)} email(s) written to: {output_path}")


def main():
    input_file = "input.txt"   
    output_file = "output.txt" 

    print("🚀 Starting Email Extraction Script...\n")
    text = read_input_file(input_file)

    if text:  
        emails = extract_emails_from_text(text)
        write_emails_to_file(emails, output_file)
    else:
        print("🚫 No content found to process.")

    print("\n🎯 Task Completed.")


if __name__ == "__main__":
    main()
