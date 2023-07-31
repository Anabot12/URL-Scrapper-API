# url_scrapper/utils.py
import requests
from bs4 import BeautifulSoup

def get_context(soup):
    # Extract the meta description if available
    meta_description = soup.find('meta', attrs={"name": "description"})
    if meta_description:
        return meta_description.get('content')

    # If meta description is not available, extract the first paragraph of content
    first_paragraph = soup.find('p')
    if first_paragraph:
        return first_paragraph.get_text()

    # If no meta description or paragraph found, return an empty string
    return ''

def scrape_url(json_input):
    try:
        url = json_input.get('url')  # Extract the 'url' parameter from the JSON input
        if not url:
            return {'error': 'URL parameter missing in JSON input.'}

        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx errors
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the image URL from the webpage
        image_url = None
        img_tag = soup.find('img')
        if img_tag:
            image_url = img_tag['src']

        # Get the context (description) about the URL
        context = get_context(soup)

        # Build the dictionary with title, context, and image_url
        data = {
            'title': soup.title.string if soup.title else '',
            'context': context,
            'image_url': image_url if image_url else ''
        }

        return data
    except requests.exceptions.RequestException as e:
        return {'error': f"Error: {e}"}
