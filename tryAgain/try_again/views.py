from django.shortcuts import render,redirect
from django .http import HttpResponse
# from django.contrib.auth.models import user
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout
from .models import Blog



# Create your views here.
def index(request):
    blog=Blog.objects.all()
    context={'blogs': blog}
    return render(request,'home.html',context)

    return render(request,'home.html')
    # return HttpResponse("its me home page")

def about(request):
    # return render(request,'about.html')
    return HttpResponse("its me about pagee")
    
def services(request):
    return render(request,'services.html')
    # return HttpResponse("its me service page")

def contact(request):
    return render(request,'contact.html')
    # return HttpResponse("contact me")        

def user_registration(request):
    if  request.method=='POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        password = request.POST.get('pass2')
        print(fname,lname,uname,email)
        if password!=password :
            messages.warning(request,'password does not match')
            return redirect('register')
        elif User.objects.filter(username=uname).exists():
            messages.warning(request,'username already user')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'email already user')
            return redirect('register')  
        else:   
                user = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=password,) 
                user.save()
                messages.success(request,'user has been registerd successfully')
                return redirect('login')
                # print(fname,lname,uname,email,password,cpassword)
    return render(request,'registration.html')
    return HttpResponse("register page")
   
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =  authenticate(request,username='username', password='password')
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.warning(request,'invalid credencials')
            return redirect('register')
    
    return render(request,'login.html')
    return HttpResponse("login page")  

def user_logout(request): 
    logout(request)
    return redirect('/')

def post_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        blog = Blog(title=title, description=description,user_id=request.user)
        blog.save()
        messages.success(request,'post has been submitted successfully')
        return redirect('post_blog')
    return render(request,'blog_post.html')   

def blog_detail(request,id): 
    blog = Blog.objects.get(id=id)  
    context = {'blog':blog} 
    return render(request,'blog_detail.html',context)




  