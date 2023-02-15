from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import First,Second,Third,Fourth,Fifth,Sixth,Seventh,Eighth,Odai,Content
from .forms import OdaiForm,ContentForm,LoginForm,SignupForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect

def index(request):
    return render(request,'book/index.html')

def osaindex(request):
    return render(request,'book/osaindex.html')

def first(request):
    data = First.objects.all().order_by("?")[:1]

    pa = {
        'data' : data,
    }
    return render(request,'book/First.html',pa)

def second(request):
    data = Second.objects.all().order_by("?")[:1]

    pa = {
        'data' : data,
    }
    return render(request,'book/Second.html',pa)

def third(request):
    data = Third.objects.all().order_by("?")[:1]

    pa = {
        'data' : data,
    }
    return render(request,'book/third.html',pa)

def ee(request):
    data = Fourth.objects.all().order_by("?")[:1]

    pa = {
        'data' : data,
    }
    return render(request,'book/ee.html',pa)

def eein(request):
    return render(request,'book/eein.html')

def eenext(request):
    data = Fifth.objects.all().order_by("?")[:1]

    pa = {
        'data' : data,
    }
    return render(request,'book/eenext.html',pa)

def eeenext(request):
    data = Sixth.objects.all().order_by("?")[:1]

    pa = {
        'data' : data,
    }
    return render(request,'book/eeenext.html',pa)

def osake(request):
    data = Seventh.objects.all().order_by("?")[:1]

    pa = {
        'data' : data,
    }
    return render(request,'book/osake.html',pa)

def osakein(request):
    pa = {
        'osake' :'説明' ,
    }
    return render(request,'book/osakein.html',pa)

def osaket(request):
    data = Eighth.objects.all().order_by("?")[:1]

    pa = {
        'data' : data,
    }
    return render(request,'book/osaket.html',pa)

def signup_view(request):
    if request.method == 'POST':

        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='/book/login')

    else:
        form = SignupForm()
    
    param = {
        'form': form
    }

    return render(request, 'book/signup.html', param)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                return redirect(to='/book/user')

    else:
        form = LoginForm()

    param = {
        'form': form,
    }

    return render(request, 'book/login.html', param)


@login_required(login_url='/admin/login/')
def user(request):
    return render(request,'book/user.html')

@login_required(login_url='/admin/login/')
def new(request):
    if (request.method == 'POST'):
        od = Odai()
        form = OdaiForm(request.POST,instance=od)
        odai = form.save(commit=False)
        odai.user = request.user
        odai.save()
        return redirect('choice')

    pa = {
        'form' : OdaiForm(), 
    }
    return render(request,'book/new.html',pa)

@login_required(login_url='/admin/login/')
def choice(request):
    data = Odai.objects.filter(user=request.user).last()

    pa = {
        'data' : data
    }

    return render(request,'book/choice.html',pa)

@login_required(login_url='/admin/login/')
def content(request,num):
    post = Odai.objects.get(id=num)
    data = Odai.objects.all().get(id=num)

    if (request.method == 'POST'):
        co = Content()
        form = ContentForm(request.POST,instance=co)
        co = form.save(commit=False)
        co.userid = request.user
        co.title = post
        co.save()
        return redirect('content',num=num)

    pa = {
        'form':ContentForm(instance=post),
        'data':data
    }

    return render(request,'book/content.html',pa)

@login_required(login_url='/admin/login/')
def post(request):
    data = Odai.objects.filter(user=request.user)

    pa = {
        'data':data
    }

    return render(request,'book/post.html',pa)

@login_required(login_url='/admin/login/')
def start(request,num):
    fu = Odai.objects.get(id=num)
    data = Content.objects.filter(userid=request.user,title=fu).order_by("?")[:1]

    pa = {
        'data':data
    }

    return render(request,'book/start.html',pa)



#@login_required(login_url='/admin/login/')
#def follow(request):
