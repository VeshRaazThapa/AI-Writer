from django.shortcuts import render
import openai
from dotenv import load_dotenv
import os
#python manage.py runserver

def home(request):
    return render(request, 'pages/home.html')

def essay_writing(request):
    if request.method == 'POST':
        prompt = request.POST['question']
        language = request.POST['language']
        prompt = "Write an essay in "+language+" about "+prompt
        print(prompt)
        load_dotenv()
        openai.api_key = os.environ.get("GPT3_KEY")
        # openai.api_key = "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"
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            max_tokens=1000,
        )
        answer = response['choices'][0]['text']
        print(answer)
    else:
        answer = None
        prompt = None
    return render(request, 'pages/essay_writing.html', {'answer': answer,'prompt':prompt})

def paraphrase(request):
    if request.method == 'POST':
        prompt = request.POST['question']
        language = request.POST['language']
        prompt = "Paraphrase in "+language+" this "+prompt
        print(prompt)
        load_dotenv()
        openai.api_key = os.environ.get("GPT3_KEY")
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            max_tokens=200,
        )
        answer = response['choices'][0]['text']
        print(answer)
    else:
        answer = None
    return render(request, 'pages/paraphrase.html', {'answer': answer})
def generate_images(request):
    if request.method == 'POST':
        prompt = request.POST['question']
        # language = request.POST['language']
        print(prompt)
        load_dotenv()
        openai.api_key = os.environ.get("GPT3_KEY")
        response = openai.Image.create(
            prompt=prompt,
            n=2,
            size='512x512',
            # max_tokens=200,
        )
        image_url = response['data'][0]['url']
        print(image_url)
    else:
        image_url = None
        prompt = None
    return render(request, 'pages/image_generation.html', {'image_url': image_url,'prompt':prompt})


def about(request):
    return render(request, 'pages/about.html')
