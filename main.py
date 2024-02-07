import os
import requests
from bs4 import BeautifulSoup

def find_video_tags(url, iframe_txt_path):
    try:
        # Fetch HTML content from the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find video tags (iframe, object, video)
        video_tags = soup.find_all(['iframe', 'object', 'video'], {'src': True})

        # Save video tags to iframe.txt
        with open(iframe_txt_path, 'a') as iframe_file:
            for tag in video_tags:
                iframe_file.write(str(tag) + '\n')

        return video_tags
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch the website content: {e}")
        return []

def get_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file_content(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def choose_iframe_tag(iframe_tags):
    print("Choose an <iframe> tag:")
    for i, tag in enumerate(iframe_tags, start=1):
        print(f"{i}. {tag}")

    choice = input("Enter the number of the <iframe> tag you want to use: ")
    try:
        choice_index = int(choice) - 1
        if 0 <= choice_index < len(iframe_tags):
            return iframe_tags[choice_index]
        else:
            print("Invalid choice. Please enter a valid number.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def update_html_file(html_file, iframe_tag):
    print(f"Updating HTML file: {html_file}")
    html_content = get_file_content(html_file)
    updated_content = html_content.replace('<iframe', iframe_tag)
    write_file_content(html_file, updated_content)
    print(f"Updated {html_file}")

def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    iframe_txt_path = os.path.join(script_directory, "iframe.txt")

    if not os.path.exists(iframe_txt_path):
        print("Creating iframe.txt in the script directory.")
        open(iframe_txt_path, 'a').close()

    # Get the website URL from the user
    website_url = input("Enter the website URL: ")

    video_tags = find_video_tags(website_url, iframe_txt_path)

    if not video_tags:
        print("No video tags found.")
        return

    # Continue with the second part of the script

    with open(iframe_txt_path, 'r') as iframe_file:
        iframe_tags = [tag.strip() for tag in iframe_file.readlines()]

    if not iframe_tags:
        print("Error: No <iframe> tags found in iframe.txt.")
        return

    selected_iframe_tag = choose_iframe_tag(iframe_tags)

    if selected_iframe_tag is None:
        return

    folder_choice = input("Select HTML folder (videos/others): ")

    if folder_choice.lower() == 'videos':
        folder_path = os.path.join(script_directory, "videos")
    elif folder_choice.lower() == 'others':
        folder_path = os.path.join(script_directory, "others")
    else:
        print("Invalid folder choice. Please choose 'videos' or 'others'.")
        return

    html_file = input(f"Enter the HTML file to update in {folder_choice} folder: ")

    html_file_path = os.path.join(folder_path, html_file)

    if not os.path.exists(html_file_path) or not html_file.endswith(".html"):
        print(f"Error: {html_file} not found or not a valid HTML file.")
        return

    update_html_file(html_file_path, selected_iframe_tag)

if __name__ == "__main__":
    main()

