from django.shortcuts import render
from Home.models import User,StudentProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def mystud(req):
    return render(req,'student/home.html')


@login_required
def edit_profile(req):
    if req.method=='POST':
        course=req.POST.get('course')
        duration=req.POST.get('duration')

        
    # return render(req,'student/edit_profile.html')

        StudentProfile.objects.create(
            user=req.user,
            course=course,
            duration=duration

        )
        return render(req,'student/home.html')
    else:
        return render(req,'student/edit_profile.html')
    


