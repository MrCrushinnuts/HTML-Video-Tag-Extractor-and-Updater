# HTML Video Tag Extractor and Updater

This Python script simplifies the process of embedding videos into HTML files by automating the extraction and updating tasks. It allows users to fetch video tags (specifically `<iframe>`, `<object>`, and `<video>`) from the HTML content of a website and update HTML files with selected video tags.

## Features

- Fetch HTML content from a website URL.
- Extract video tags from the fetched HTML content.
- Save extracted video tags to a text file.
- Choose and update HTML files with selected video tags.
- Supports updating multiple HTML files in different directories.

## Installation

1. **Clone the repository:**

git clone https://github.com/your-username/html-video-tag-extractor.git

markdown


2. **Install dependencies:**

pip install requests beautifulsoup4

markdown


## Usage

1. **Run the script:**

python main.py

markdown


2. **Enter the website URL when prompted.**

3. **Follow the instructions to choose an `<iframe>` tag and specify the HTML file to update.**

## Example

Suppose you want to embed a video from a website that supports direct embedding:
1. Run the script and enter the URL of the page containing the video.
2. Choose the appropriate `<iframe>` tag from the list.
3. Specify the HTML file where you want to embed the video.
4. The script will update the HTML file with the selected `<iframe>` tag, embedding
    Choose the appropriate <iframe> tag from the list.
    Specify the HTML file where you want to embed the video.
    The script will update the HTML file with the selected <iframe> tag, embedding the video.
