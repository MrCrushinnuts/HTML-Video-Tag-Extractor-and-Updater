HTML Video Tag Extractor and Updater

This Python script simplifies the process of embedding videos into HTML files by automating the extraction and updating tasks. It allows users to fetch video tags (specifically <iframe>, <object>, and <video>) from the HTML content of a website and update HTML files with selected video tags.
Features

    Fetch HTML content from a website URL.
    Extract video tags from the fetched HTML content.
    Save extracted video tags to a text file.
    Choose and update HTML files with selected video tags.
    Supports updating multiple HTML files in different directories.

Installation

    Clone the repository:

git clone https://github.com/your-username/html-video-tag-extractor.git

Install dependencies:

    pip install requests beautifulsoup4

Usage

    python main.py

    Enter the website URL when prompted.

    Follow the instructions to choose an <iframe> tag and specify the HTML file to update.

Tutorial
Fetching Video Tags

    Enter the URL of the website containing the video(s) you want to extract.
    The script will fetch the HTML content from the provided URL.
    It will then extract the video tags (<iframe>, <object>, <video>) from the HTML content.

Saving Video Tags

    Extracted video tags will be saved to a text file named iframe.txt in the script directory.

Updating HTML Files

    Choose an <iframe> tag from the saved list.
    Select the HTML file you want to update.
    The script will update the chosen HTML file with the selected <iframe> tag.

Note: The script may not work with all websites, especially those that dynamically load content, such as YouTube. For such websites, manual embedding may be required.
Example

Suppose you want to embed a video from a website that supports direct embedding:

    Run the script and enter the URL of the page containing the video.
    Choose the appropriate <iframe> tag from the list.
    Specify the HTML file where you want to embed the video.
    The script will update the HTML file with the selected <iframe> tag, embedding the video.
