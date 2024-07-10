import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

def find_word_in_webpage(url, word):
    html_content = fetch_webpage(url)
    if html_content is None:
        return
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Search for the specific word in the text content of the webpage
    if word in soup.get_text():
        print(f"The word '{word}' was found in the webpage.")
    else:
        print(f"The word '{word}' was NOT found in the webpage.")

if __name__ == "__main__":
    url = input("Enter the URL of the webpage: ")
    word = input("Enter the word to search for: ")
    find_word_in_webpage(url, word)




