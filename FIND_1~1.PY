from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
webpage_html_document = response.text
soup = BeautifulSoup(webpage_html_document, "html.parser")

# Use the specific score ID to find the corresponding upvote element.
score_id = 'score_39530203'

# Find the upvote span using its ID.
article_upvote_tag = soup.find('span', id=score_id)

# Check if the upvote tag was found to prevent AttributeError.
if article_upvote_tag:
    article_upvotes = article_upvote_tag.text
    # Navigate to the parent of the parent (tr -> td -> span) to find the article's title and link.
    article_row = article_upvote_tag.find_parent('tr').find_previous_sibling('tr')
    article_title_tag = article_row.find('a', class_='titlelink')

    # Check if the article title tag was found to prevent AttributeError.
    if article_title_tag:
        article_title = article_title_tag.text
        article_url = article_title_tag['href']
    else:
        article_title = "Article title not found"
        article_url = "URL not found"
else:
    article_upvotes = "Upvotes not found"
    article_title = "Article title not found"
    article_url = "URL not found"

print(f"Article Title: {article_title}")
print(f"Article URL: {article_url}")
print(f"Article Upvotes: {article_upvotes}")
