from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout , login

# id is harry and password for user is codewithharry@123

# Create your views here.
def home(request) :
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request ,'index.html')
    # return HttpResponse("hello world")

def calc(request) :
    try :
        c = ''
        data = {}
        if request.method == "POST" :
            if request.POST.get('variable1') == ""  or request.POST.get('variable2') == "" :
                return render(request ,"calculator.html" ,{'error' : True})
            val_1 = eval(request.POST.get('variable1'))
            val_2 = eval(request.POST.get('variable2'))
            opt   = request.POST.get('select')
            if opt == "+" :
                c = val_1+val_2
            elif opt == "-" :
                c = val_1-val_2
            elif opt == "*" :
                c = val_1*val_2
            elif opt == "/" :
                c = val_1/val_2
            else :
                c = "error"
            data = {
                'value1' : val_1,
                'value2' : val_2 ,
                'op' : opt ,
                'ans' : c
            }
    except : 
        return HttpResponse("Error")
    return render(request , 'calculator.html' , data)

def my_projects(request) :
    return render(request , 'my_projects.html')

def loginUser(request) :
    if request.method == "POST":
        username =  request.POST.get('username')
        password = request.POST.get('password')
        # chect if user has correct credentials
        user = authenticate(username=username, password=password)
        if user is not None  :
            login(request,user)
            return redirect("/")
        else:
            return render(request , 'login.html')

    return render(request , 'login.html')

# sign_up
def sign_up(request) :
    data = {}
    if request.method == "POST" :
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        email = request.POST.get('email')
        if password_1 != password_2 :
            data["Re_password"] = True
        if password_1 == "" or password_2 == "":
            data["password"] = True
        if first_name == "" or last_name=="":
            data["first_name"] = True
        if username == "":
            data["Username"] = True
        if email == "":
            data["email"] = True
        elif "@gmail.com" not in email :
            data["email_invalid"] = True
        if first_name != "" and last_name != "" and username != "" and password_1 != "" and password_2 != "" :
            user = User.objects.create_user(username, email, password_1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect("/login")
        return render(request, "sign_up.html" , data)
    return render(request , 'sign_up.html' , data)

def logoutUser(request) :
    logout(request)
    return redirect("/login")

def forgot_password(request) : 
    return render(request,"forgot_password")