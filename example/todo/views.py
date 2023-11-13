import uuid

from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView
from requests import post

from .models import *
from .forms import TaskForm, PostForm, RegisterUserform, LoginUserForm
from .utils import DataMixin
from PIL import Image as PILImage


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #commit=False
            #task = form.task
            #task.save()
            return redirect('home')
        else:
            error = 'Форма неверная'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'todo/create.html', context)


def home_view(request):
    tasks = Task.objects.order_by('id')
    post = Post.objects.order_by('-id')
    user = request.user
    categories = Tags.objects.all()
    print(user, user)
    context = {
        'tasks': tasks,
        'user': user,
        'post': post,
        'categories': categories,
   }
    return render(request, 'todo/about.html', context)

def category_posts(request, cat_id):
    catall = Post.objects.all()
    # print(catall)
    category = Tags.objects.get(pk=cat_id)
    print(category)
    catfilter = Post.objects.filter(tags=category)
    print(catfilter)

    context = {
        'catfilter' : catfilter,
    }

    return render(request, 'todo/category.html', context)

def delete_task_view(request, task_id): #удалить задание
    task = get_object_or_404(Task, pk = task_id)
    print('Task_for_delete: ', task)
    task.delete()
    return redirect('home')

def to_about(request):
    return render(request, 'todo/about.html')

def post_create(request): #создание поста
    filename=''
    error=''
    user=request.user

    if request.method=='POST':
        form = PostForm(request.POST, request.user)

        if form.is_valid():
            post = form.save(commit=False)
            post.author=user

            post.save()

            image_files = request.FILES.getlist('image')
            for image_file in image_files:
                print(image_file)
                PILImage.open(image_file)
                fs = FileSystemStorage()
                unique_filename = f"{uuid.uuid4()}_{slugify(image_file.name)}"
                #сохранение файлa на сервере
                filename = fs.save(unique_filename, image_file)

                image_path = fs.url(filename)

                #создание файла
                image = Image.objects.create(
                    post=post,
                    image=image_path,
                )

                    # print(image_file)


            # post.image=filename
            # print(image_files)
            print(f"Создан пост: {post} Ссылка на картинку: {filename}")

            return redirect('home')

        else:
            error='Поля заполнены не верно'
            print(form.errors)

    else:
        form=PostForm()

    context={
        'form' : form,
        'error' : error,
    }

    return render(request, 'todo/create.html', context)


def post_show(request):  # выводит пост на гл.страницу
    posts = Post.objects.order_by('number')

    context = {
        'post': posts,
    }

    return render(request, 'todo/about.html', context)



class RegisterUser(DataMixin, CreateView):
    form_class=RegisterUserform
    template_name='todo/register.html'
    succes_url=reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        user = form.save()
        login(self.request, user)
        return redirect('home')

    def form_invalid(self, form):

        print(form.errors)
        return super(RegisterUser,self).form_invalid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return render(request, 'todo/login.html')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'todo/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

