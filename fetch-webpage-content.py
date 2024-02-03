# FetchWebpageContent.py
# This script retrieves and prints the text content from specific elements of a webpage using requests and BeautifulSoup.

import requests  # For making HTTP requests to a specified URL.
import bs4  # BeautifulSoup, for parsing HTML and extracting the data needed.
import webbrowser  # Although unused, could be for opening URLs in a browser.

# Set headers to mimic a real browser request.
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.3'
}

# Make a GET request to the specified URL.
res = requests.get('https://gamefaqs.gamespot.com/boards/578278-zelda-no-densetsu-the-hyrule-fantasy/79484897', headers=headers)

# Verify the request was successful by checking the status code.
if res.status_code == 200:
    # Parse the webpage's HTML content using BeautifulSoup.
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Select elements with the class 'msg_text' which contain the desired text.
    titleElem = soup.select('.msg_text')

    # Iterate through each selected element and print its text content.
    for i in range(len(titleElem)):
        titleText = titleElem[i].text  # Extract the text from the current element.
        print(f'{titleText}')
else:
    # Inform the user if the webpage could not be successfully retrieved.
    print(f"Failed to retrieve the webpage, status code: {res.status_code}")
