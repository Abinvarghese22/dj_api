from django.shortcuts import render

# Create your views here.
def myteacher(req):
    return render(req,'hometeach.html')