"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home.views import *
from django.urls import include
# from student import views as S

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('h/',views.hello),
    # # path('w/',views.wel)
    # path('w/<int:age>',views.wel),
    path('reg/',Empreg),
    # path('sta/',views.mystatic),
    path('hh/',myhome),
    path('list/',emp_list),
    # path('del/<int:pki>',views.emp_del),
    # path('upd/<int:pke>',views.emp_edit),
    # path('update/<int:pke>',views.emp_update),
    path('studReg/',stud_reg),

    path('student_list/',student_list,name='student_list'),
    

    path('student/add',StudentCreateView.as_view(),name='student-add'),
    path('student/',StudentListView.as_view(),name='student-list'),
    path('students/delete/<int:pk>/',StudentDeleteView.as_view(),name='student-delete'),
    path('students/update/<int:pk>/',StudentUpdateView.as_view(),name='student-update'),

    path('login/', user_login, name='login'), 
    path('logout/', logouts, name='logouts'),   
    

    # path('stud/',S.mystud),
    path('SS/', include('student.urls')),
    path('TT/', include('Teacher.urls')),
    path('set_session/',set_session, name='set_session'),
    path('get_session/',get_session, name='get_session'),
    path('delete_session/',delete_session, name='delete_session'),
    path('shhs/',shhs, name='shhs'),
    path('set_cookie/',set_cookieee, name='set_cookie'),
    path('get_cookie/',get_cookee, name='get_cookie'),
    path('upload/',upload_file, name='upload_files'),
    path('view_docs/',list_files, name='view_docs'),
    path('mail/',send_eml, name='mail'),


    
]


if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
