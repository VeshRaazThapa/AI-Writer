from django.shortcuts import render, redirect
from .forms import BlogForm
import openai
from dotenv import load_dotenv
import os
from django.http import JsonResponse
from .models import Blog
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
import requests
import uuid
# python manage.py runserver

def home(request):
    form = BlogForm()
    return render(request, 'pages/home.html', {'blog_form': form, 'blogs': Blog.objects.all().order_by('-created_at')})


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
    return render(request, 'pages/create_blog.html', {'form': form })

class BlogDetailPlaneView(DetailView):
    model = Blog
    template_name = 'pages/blog_detail_plane.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_form'] = BlogForm(instance=self.object)
        context['update'] = True
        return context
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'pages/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_form'] = BlogForm(instance=self.object)
        context['update'] = True
        context['blogs']= Blog.objects.all().order_by('-created_at')
        return context

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'pages/create_blog.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_form'] = BlogForm(instance=self.object)
        context['update'] = True
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        print(self.request.path)
        return redirect(self.request.path.replace('/edit',''))

def essay_writing(request):
    if request.method == 'POST':
        prompt = request.POST['question']
        # language = request.POST['language']
        language = 'English'
        prompt = "Write a long essay " + "about " + prompt
        # print(prompt)
        load_dotenv()
        openai.api_key = os.environ.get("GPT3_KEY")
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            max_tokens=2048,
        )
        answer = response['choices'][0]['text']
        print(answer)
    else:
        answer = None
        prompt = None
    return JsonResponse({'answer': answer, 'prompt': prompt})


def paraphrase(request):
    if request.method == 'POST':
        prompt = request.POST['question']
        # language = request.POST['language']
        language = 'English'
        prompt = "Paraphrase the following content: \n" + prompt
        # print(prompt)
        load_dotenv()
        openai.api_key = os.environ.get("GPT3_KEY")
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            max_tokens=2048,
        )
        answer = response['choices'][0]['text']
        print(answer)
    else:
        answer = None
        prompt = None
    return JsonResponse({'answer': answer, 'prompt': prompt})

def text_completion(request):
    if request.method == 'POST':
        prompt = request.POST['question']
        # language = request.POST['language']
        prompt = 'Write a long blog about ' + prompt
        # print(prompt)
        load_dotenv()
        openai.api_key = os.environ.get("GPT3_KEY")
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            max_tokens=2048,
            # temperature= 1,
        )
        answer = response['choices'][0]['text']
        # print(answer)
    else:
        answer = None
        prompt = None
    return JsonResponse({'answer': answer, 'prompt': prompt})

# saving data to the database
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
        print(response['data'],'---------')
        image_url = response['data'][0]['url']
        image_name = 'media/generated_image/'+str(uuid.uuid4()) + '.jpg'
        response = requests.get(image_url)

        with open(image_name , 'wb') as f:
            f.write(response.content)
    else:
        image_name = None
        prompt = None
    return render(request, 'pages/image_generation.html', {'image_url': image_name, 'prompt': prompt})


def about(request):
    return render(request, 'pages/about.html')


