from django.shortcuts import render,redirect
from django.contrib import messages
from cars.forms import ImageForm, LoginForm
from . models import Details,Image_det
from django.contrib.auth import logout as logouts

def index(request):
    return render(request,'index.html')

def images(request):
    if request.method=='POST':
        form=ImageForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            photo=form.cleaned_data['Photo']
            name=form.cleaned_data['Name']
            brand=form.cleaned_data['Brand']
            price=form.cleaned_data['Price']
            tab=Image_det(Photo=photo,Name=name,Brand=brand,Price=price)
            tab.save()
            messages.success(request,"Data Saved Successfully")
            return redirect('/')

    else:
        form=ImageForm()
    return render(request,'images.html',{'form':form})


def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')

        user=Details.objects.filter(Email=email).exists()
        if user:
            messages.warning(request,'User Exists with same email')
            return redirect('/signup')
        else:
            tab=Details(Username=username,Email=email,Password=password)
            tab.save()
            return redirect('/images')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            chk=Details.objects.get(Email=email)
            if not chk:
                messages.warning(request,"Email doesn't exist")
                return redirect('/login')
            elif password!=chk.Password:
                messages.warning(request,"Incorrect Password")
                return redirect('/login')
            else:
                messages.success(request,"Login successful")
                return redirect('/home/%s' % chk.id)
    else:
        form=LoginForm()
    return render(request,'login.html',{'data':form})

def home(request,id):
    user=Details.objects.get(id=id)
    return render(request,'home.html',{'user':user})
def gallerys(request):
    allimages=Image_det.objects.all()
    return render(request,'gallerys.html',{'images':allimages})

def logout(request):
    logouts(request)
    messages.success(request,"Logged Out Successfully...")
    return redirect('/')

def detail(request,id):
    det=Image_det.objects.get(id=id)
    return render(request,'detail.html',{'det':det})