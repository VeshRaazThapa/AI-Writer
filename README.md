# AI Writer

AI Writer is a website that utilizes GPT-3 technology to generate high-quality essays and articles on a variety of topics. It is designed to make the writing process faster and more efficient for students, writers, and professionals.
![image](./static/image1.png)

## Features

- Essay writing: The website provides a form where users can enter a topic and receive a written essay on the topic.
- Paraphrasing: The website also has a form where users can input a paragraph and receive a paraphrased version of the paragraph.


## Getting Started

To run the website locally, clone the repository and run the following commands in your terminal:

`pip install -r requirements.txt`

`export GPT3_KEY="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"`

`python manage.py makemigrations`

`mkdir media`

`mkdir media/generated_image`

`python manage.py runserver`

The website will then be available at http://127.0.0.1:8000/

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [OpenAI GPT-3](https://openai.com/gpt-3/) - The AI model used
