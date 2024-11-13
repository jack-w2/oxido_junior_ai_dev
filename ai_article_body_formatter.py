import os
from openai import OpenAI
from dotenv import load_dotenv

def get_article_text(article_file_path):
    with open(article_file_path, 'r') as article_file:
        article_text = article_file.read()
    return article_text

load_dotenv()

client = OpenAI(
    api_key=os.environ.get('API_KEY'),
    organization=os.environ.get('ORGANIZATION'),
    project=os.environ.get('PROJECT')
)

completion = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {"role": "system", "content": "You are a skilled web development assistant. Generate clean, well-structured HTML code with proper indentation, comments, and semantic tags when appropriate. Explain your code briefly if requested, and follow best practices for web accessibility and responsiveness."}
    ]
)

print(completion.choices[0].message)
