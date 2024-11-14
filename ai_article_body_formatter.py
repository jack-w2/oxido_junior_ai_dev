import os
from openai import OpenAI
from dotenv import load_dotenv
from markdown_it import MarkdownIt

def get_article_text(article_file_path):
    """Read article text from given path."""
    with open(article_file_path, 'r') as article_file:
        article_text = article_file.read()
    return article_text

def extract_html(message_content):
    """Find HTML code block in the given message and extract its contents."""
    md = MarkdownIt()
    parsed = md.parse(message_content)
    extracted_html = ''
    for token in parsed:
        if token.type == 'fence' and token.info == 'html':
            extracted_html = token.content.strip()
            break
    if extracted_html:
        return extracted_html
    else:
        raise ValueError('No HTML code block found in the response.')

def main():
    load_dotenv()

    unformatted_article_text = get_article_text('artykul.txt')

    client = OpenAI(
        api_key=os.environ.get('API_KEY'),
        organization=os.environ.get('ORGANIZATION'),
        project=os.environ.get('PROJECT')
    )

    completion = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {
                "role": "system",
                "content": "You are a skilled web development assistant. Generate clean, well-structured HTML code with proper indentation, comments, and semantic tags when appropriate. Explain your code briefly if requested, and follow best practices for web accessibility and responsiveness."
            },
            {
                "role": "system",
                "content": f"Please format this HTML code with the rules mentioned in the previous prompt. Return only the text inside the <body> tag without the tag itself. Here is the code:```{unformatted_article_text}```"
            }
        ]
    )

    message = completion.choices[0].message
    formatted_article_text = extract_html(message.content)

    with open('artykul.html', 'w') as article_file:
        article_file.write(formatted_article_text)
