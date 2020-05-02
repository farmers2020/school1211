"""projects33 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from app33 import views
from django.conf.urls.static import static
from projects33 import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showindex,name='index'),
    path('home/', views.home, name="home"),
    path('about/', views.Aboutschool, name='about'),
    path('faci/', views.facilities, name='faci'),
    path('achiev', views.achievements, name='achiev'),
    path('contactus/',views.contactus,name='contactus'),
    path('gal/', views.schoolgalary, name='gal'),
    path('add/', views.admin, name='add'),
    path('log/', views.adminlogin, name='log'),
    path('facul/', views.addfaculty, name='facul'),
    path('stud/', views.addstudents, name='stud'),
    path('save/',views.savestudentsdata,name='save'),
    path('fsave/',views.savefacultydata,name="fsave"),
    path('s_show/',views.showstudentsdata,name="s_show"),
    path('f_show/',views.showfacultydata,name='f_show'),
    path('update/',views.updatestudentsdata,name='update'),
    path('update1/',views.studentsupdatebyfuc,name='update1'),
    path('delete/',views.deleterecords,name='delete'),
    path('save1/',views.updatesave,name='save1'),
    path('fupdate/',views.updatefaculty,name='fupdate'),
    path('fdelete/',views.deletefaculty,name='fdelete'),
    path('save2/',views.fupdatesave,name='save2'),
    path('flog/',views.facultylogin,name='flog'),
    path('wel/',views.facultywel,name='wel'),
    path('marks/',views.addstudentsmarks,name="marks"),
    path('stlogin/',views.stlogin,name='stlogin'),
    path('conf/',views.conformation,name='conf'),
    path('sadd/',views.addmarks,name="sadd"),
    path('search/',views.searchstudents,name='search'),
    path('find/',views.findstudent,name="find"),
    path('savefed/',views.feedback,name="savefed"),
    path('viewfeed/',views.viewfeedback,name="viewfeed"),
    path('studentsindex/',views.studentsindex,name="studentsindex"),
    path('viewpasslist/',views.viewpasslist,name='viewpasslist'),
    path('getlist/',views.getlists,name='getlist'),
    path('getfailstud/',views.getfailstud,name="getfailstud"),
    path('failstdlist/',views.failstudentslist,name="failstdlist"),
    path('getpasslist/',views.getpasslist,name="getpasslist"),
    path('passstudentslist/',views.passstudentslist,name='passstudentslist'),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('updatepassword/',views.updatepassword,name='updatepassword'),
    path('conformpass/',views.conformationpassword,name="conformpass"),
    path('notification/',views.notification,name="notification"),
    path('uploadnotif/',views.uploadnotification,name='uploadnotif'),
    path('savenotification/',views.savenotification,name='savenotification'),
    path('open/',views.openadmin,name="open"),
    path('logout/',views.adminlogout,name='logout'),
    path('faculwelcome/',views.faculwelcome,name='faculwelcome'),
    path('flogout/',views.falogout,name='flogout'),
    path('stwel/',views.stwelcome,name='stwel'),
    path('slogout/',views.stlogout,name='slogout'),
    path('forgetpassword/',views.forgetpassword,name='forgetpassword'),
    path('sendotp/',views.sendotp,name="sendotp"),
    path('sendmail/',views.sendmail,name='sendmail'),
    path('checkotp/',views.checkotp,name='checkotp'),
    path('updatepass1/',views.updatepass1,name='updatepass1')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
