"""
Open a true5050 link and scrap the content until both links are found
"""
import requests
import bs4
import webbrowser
import sys, time

BASE_URL = 'http://true5050.com/'

def check_url(url):
    """
    Check if URL is a valid true5050 URL, containing the base URL and a path
    """
    if BASE_URL not in url or not url.startswith(BASE_URL) or len(url) <= len(BASE_URL):
        raise RuntimeError("Invalid true5050.com URL: " + url)

def get_links(url):
    """
    Return the links pointed by the true5050 URL
    """
    check_url(url)
    first_link, second_link = None, None
    while not first_link or not second_link:
        res = requests.get(url, allow_redirects=False)
        res.raise_for_status()
        link = bs4.BeautifulSoup(res.text, 'html.parser').select('a')[0].get('href')
        if not first_link:
            first_link = link
            print(first_link) # Not fancy output to comply with Python 2 AND 3
        elif link != first_link:
            second_link = link
            print(second_link)
        if not second_link: # Got only one link, not done yet
            time.sleep(1)
    return (first_link, second_link)

def main():
    """
    Entry point
    """
    if len(sys.argv) < 2:
        print("Usage: true50 <true5050.com URL>")
        return 1
    try:
        url = sys.argv[1]
        first_link, second_link = get_links(url)
        webbrowser.open(first_link)
        webbrowser.open(second_link)
    except (RuntimeError, IOError) as exception:
        print(exception)
        return 1
    return 0

if __name__ == '__main__':
    main()
