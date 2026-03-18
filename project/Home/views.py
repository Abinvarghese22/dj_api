from django.shortcuts import get_object_or_404,redirect,render
from django.http import HttpResponse
from .forms import EmpForm,DocumentForm
from .models import Employee,User,Student,StudentProfile,Document
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout


from django.core.mail import send_mail
from django.conf import settings

# from django.contrib.auth import User    #default user model(i.e without customisation)


# Create your views here.
def hello(req):
    hai="<h1>Welcome to Django</h1>"
    return HttpResponse(hai)


def wel(req,age):
    name=input("Enter your name: ")
    time=10
    print("my age is",age)
    return render(req,'welcome.html',{'details':name,'t':time,'a':age})

def Empreg(req):
    if req.method=="POST":
        form=EmpForm(req.POST)
        if form.is_valid():
            form.save()
            print("..........................")
            return HttpResponse("Success")
        else:
            return HttpResponse("Error Occured")

    
    else:
        print("/////////////////////////////////////")
        frm=EmpForm()
        return render(req,'regEmp.html',{'form':frm})
    
def mystatic(req):
    return render(req,'mystatic.html')

def myhome(req):
    return render(req,'home.html')


def emp_list(req):
    emp=Employee.objects.all()

    
    return render(req,'listemp.html',{'data':emp})

def emp_del(req,pki):
    emp=Employee.objects.get(id=pki)
    emp.delete()
    # return HttpResponse("Employee Deleted! ")
    return redirect('/list')

def emp_edit(req,pke):
    data=get_object_or_404(Employee,pk=pke)
    frm=EmpForm(instance=data)
    return render(req,'edit_emp.html',{'form':frm})

def emp_update(req,pke):
    data=get_object_or_404(Employee,pk=pke)
    if req.method=="POST":
        frm=EmpForm(req.POST,instance=data)
        if frm.is_valid():
            frm.save()
            return redirect('/list')


def stud_reg(req):
    if req.method=="POST":
        uname=req.POST.get('user')
        pa=req.POST.get('pass')
        em=req.POST.get('email')
        first=req.POST.get('fname')
        last=req.POST.get('lname')
        phno=req.POST.get('ph')
        add=req.POST.get('address')


        User.objects.create_user(username=uname,password=pa,email=em,first_name=first,
                         last_name=last,phone=phno,address=add,
                         is_staff=False,is_active=True,is_superuser=False)
        return HttpResponse("User Registered Successfully! ")
    return render(req,'stud_reg.html')


def user_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(username=uname, password=pwd)
        if user is not None:
            if user.is_superuser == False and user.is_staff == False: #student login
                login(request, user)
                return redirect('/SS/sh/')
            elif user.is_superuser==True and user.is_staff==True: #teacher login
                login(request, user)
                # return HttpResponse("Admin Login Successful")
                return redirect('/TT/tt/')

        else:
            return HttpResponse("Invalid Credentials, try again")
        
    return render(request, 'login.html')


class StudentCreateView(CreateView):
    model=Student
    fields=['name','email','age']
    template_name='student_form.html'
    success_url='/students'

class StudentListView(ListView):
    model=Student
    template_name='student_list.html'
    context_object_name='stud'
    
class StudentDeleteView(DeleteView):
    model=Student
    template_name='student_delete.html'
    success_url=reverse_lazy('student-list')
    
class StudentUpdateView(UpdateView):
    model=Student
    fields=['name','email','age']
    template_name='student_form_edit.html'
    success_url=reverse_lazy('student-list')


def logouts(request):
    logout(request)
    return redirect('/login/')

def student_list(request):
    student_list=StudentProfile.objects.select_related('user')
    return render(request,'reg_student_list.html',{'students':student_list})



#sessions

def set_session(request):
    if request.method=="POST":
        request.session['username']=request.POST.get('uname')
        request.session['password']=request.POST.get('pass')
        return HttpResponse("session is set")
    return render(request,'set_SS.html')

def get_session(request):
    username=request.session['username']
    password=request.session['password']
    return HttpResponse(f"username is {username} and password is {password}")

def shhs(request):
    print("hello session......",request.session['username'])
    return HttpResponse("hello Session")


def delete_session(request):
    if request.session.exists('username'):
        print("session Exists")
    try:
        del request.session['username']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("session is deleted")

def set_cookieee(request):
    response=HttpResponse("Cookie is set")
    response.set_cookie('name','ammu',max_age=3600)
    # response.set_cookie('age',22)
    response.set_cookie('place','kochi')
    return response

def get_cookee(request):
    name=request.COOKIES['name']
    # age=request.COOKIES['age']
    # place=request.COOKIES['place']
    place=request.COOKIES.get('place','not found!')
    return HttpResponse(f"name:{name}  place:{place}")

# file upload
def upload_file(request):
    if request.method=="POST":
        form=DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        
    else:
        form=DocumentForm()
    return render(request,'upload.html',{'form':form})


def list_files(request):
    files=Document.objects.all()
    return render(request,'listdata.html',{'data':files})


def send_eml(request):
    send_mail(subject="Welcome to Dual Nova!",message="My first message",
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=['abincvarghese2002@gmail.com'],
              fail_silently=False)
    
    return HttpResponse('Mail send')
    