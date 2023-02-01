from django.shortcuts import render,redirect
from .forms import BlogForm
import openai
from dotenv import load_dotenv
import os
from django.http import JsonResponse
from .models import Blog
#python manage.py runserver

def home(request):
    form = BlogForm()
    return render(request, 'pages/home.html', {'blog_form': form,'blogs':Blog.objects.all()})

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            referer_url = request.META.get('HTTP_REFERER', '/')
            return HttpResponseRedirect(referer_url)
            # return redirect('blogs')
    else:
        form = BlogForm()
    return render(request, 'pages/create_blog.html', {'form': form})

def essay_writing(request):
    if request.method == 'POST':
        prompt = request.POST['question']
        language = request.POST['language']
        prompt = "Write an essay in "+language+" about "+prompt
        print(prompt)
        load_dotenv()
        openai.api_key = os.environ.get("GPT3_KEY")
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
    # return render(request, 'pages/essay_writing.html', {'answer': answer,'prompt':prompt})
    return JsonResponse({'answer': answer,'prompt':prompt})

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
        prompt = None
    return JsonResponse({'answer': answer, 'prompt': prompt})

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
    # return JsonResponse({'answer': image_url,'prompt':prompt})
    return render(request, 'pages/image_generation.html', {'image_url': image_url,'prompt':prompt})


def about(request):
    return render(request, 'pages/about.html')

