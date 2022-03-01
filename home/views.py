from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Post
from django.contrib.auth import authenticate, login, logout
from home.models import Post




# Create your views here.


def index(request):
    allposts = Post.objects.all()
    context={'allposts':allposts}
    return render(request,"index.html",context)
    # return HttpResponse("This is Homepage")


def addblog(request):
    if (request.method == 'POST'):
        print('this is the blog.')
        title = request.POST['blog-title']
        data = request.POST.get('blog-data',False)
        author = request.POST.get('blog-authoe',False)
        # print(title,data,author)

        ins = Post(title=title,content=data,author=author)
        ins.save()
        print('data has beeen saved')


    return render(request,"addblog.html")


def contact(request):
    return render(request,"contact.html")

def login(request):
    # if request.method == 'POST' :
    #     username= request.POST['username']
    #     password= request.POST['password']

    #     user= authenticate(username=username,password=password)
    #     if user is not None:
    #         login(request,user)
    #         messages.sucess(request, "successfully login in.")
    #         return redirect('index')
    #     if user is None:
    #         messages.failed(request,"invalid credentials.")
    #         return redirect('error')

    return render(request,"login.html")





def blog(request,slug):
    # posts = Post.object.get(id=pk)
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}

    return render(request, 'blog.html', context)



# def addblog(request):
    
    
    # checks for inputs



    # message display
    


    # else:
    #     return HttpResponse('404 - Not Alowed')
