from django.core.mail import send_mail
from projects33 import settings as se
from django.shortcuts import render, redirect
from app33.models import students,feedbackmodel,uploadnotificationmodel
from app33.models import faculty,otp

def showindex(request):
    return render(request,"index.html")
def Aboutschool(request):
    return render(request,"ABOUT.html")
def preprimary(request):
    return render(request,"preprimary.html")
def home(request):
    return render(request,"index.html")
def primary(request):
    return render(request,"primary.html")
def highschool(request):
    return render(request,"highschool.html")


def studentslife(request):
    return render(request,"stundents.html")


def facilities(request):
    return render(request,"facilities.html")


def achievements(request):
    return render(request,"achievements.html")


def schoolgalary(request):
    return render(request,"gallery.html")


def admin(request):
    return render(request,"adminlogin.html")


def adminlogin(request):
        uname = request.POST.get("uname")
        passw = request.POST.get("passw")
        if uname == 'pallavi' and passw == 'pallavi':
          request.session["uname"] = uname
          return redirect("open")
        else:
         message = "please enter the correct username and password"
         return render(request, "adminlogin.html", {"message": message})


def addfaculty(request):
    res = request.session.get("uname")
    if res:
        return render(request, "addfaculty.html")
    else:
        return redirect("add")



def addstudents(request):
    res = request.session.get("uname")
    if res:
        return render(request, "addstudents.html")
    else:
        return redirect("add")


def savestudentsdata(request):
    regno=request.POST.get("regno")
    name=request.POST.get("name")
    father=request.POST.get("father")
    gender=request.POST.get("ra")
    address=request.POST.get("add")
    dob=request.POST.get("dob")
    doj=request.POST.get("doj")
    stand=request.POST.get("std")
    photo=request.FILES['photo']
    en=request.POST.get("e1")
    ka=request.POST.get("k1")
    hi=request.POST.get("h1")
    sc=request.POST.get("s1")
    sos=request.POST.get("ss1")
    mat=request.POST.get("m1")
    tot=request.POST.get("t1")
    per=request.POST.get("p1")
    s=students(english=en,kannad=ka,hindi=hi,science=sc,social_science=sos,mathematics=mat,totalmarks=tot,percentage=per,standards=stand,name=name,Regno=regno,father=father,gender=gender,address=address,dob=dob,doj=doj,image=photo)
    s.save()
    return render(request,"studentsaddforms.html",{'message':'save'})


def savefacultydata(request):
    regno = request.POST.get("regno")
    name = request.POST.get("name")
    subject=request.POST.get("sub")
    exp=request.POST.get("exp")
    gender = request.POST.get("ra")
    address = request.POST.get("add")
    dob = request.POST.get("dob")
    doj = request.POST.get("doj")
    quali=request.POST.get("qual")
    photo = request.FILES['photo']
    j = faculty(quali=quali,subject=subject, experience=exp, name=name, Regno=regno, gender=gender, address=address, dob=dob,
                 doj=doj, image=photo,pasword=name)
    j.save()
    return render(request,"addfaculty.html",{"message":"save"})


def showstudentsdata(request):
    res = request.session.get("uname")
    if res:
        all = students.objects.all()
        return render(request, "showstudents.html", {"data": all})
    else:
        return redirect("add")



def showfacultydata(request):
    res = request.session.get("uname")
    if res:
        all = faculty.objects.all()
        return render(request, "showfaculty.html", {"data": all})
    else:
        return redirect("add")




def updatestudentsdata(request):
    regno = request.GET.get("regno")
    a = students.objects.get(Regno=regno)
    return render(request,"update.html",{"data":a})

def deleterecords(request):
    regno = request.GET.get("regno")
    students.objects.filter(Regno=regno).delete()
    all = students.objects.all()
    return render(request,"showstudents.html",{"data":all})


def updatesave(request):
    regno=request.POST.get("regno")
    name=request.POST.get("name")
    father=request.POST.get("father")
    gender=request.POST.get("ra")
    address=request.POST.get("add")
    dob=request.POST.get("dob")
    doj=request.POST.get("doj")
    stand=request.POST.get("std")
    photo=request.FILES['photo']
    en=request.POST.get("e1")
    ka=request.POST.get("k1")
    hi=request.POST.get("h1")
    sc=request.POST.get("s1")
    sos=request.POST.get("ss1")
    mat=request.POST.get("m1")
    tot=request.POST.get("t1")
    per=request.POST.get("p1")
    s=students(totalmarks=tot,percentage=per,english=en,kannad=ka,hindi=hi,science=sc,social_science=sos,mathematics=mat,standards=stand,name=name,Regno=regno,father=father,gender=gender,address=address,dob=dob,doj=doj,image=photo)
    s.save()
    all=students.objects.all()
    return render(request,"showstudents.html",{"data":all})


def updatefaculty(request):
    regno = request.GET.get("regno")
    ss = faculty.objects.get(Regno=regno)
    return render(request,"fupdate.html",{"data":ss})


def deletefaculty(request):
    regno = request.GET.get("regno")
    faculty.objects.filter(Regno=regno).delete()
    all = faculty.objects.all()
    return render(request,"showfaculty.html",{"data":all})


def fupdatesave(request):
    regno = request.POST.get("regno")
    name = request.POST.get("name")
    gender = request.POST.get("ra")
    address = request.POST.get("add")
    dob = request.POST.get("dob")
    doj = request.POST.get("doj")
    exp=request.POST.get("exp")
    qualification=request.POST.get("qual")
    subject = request.POST.get("sub")
    photo = request.FILES['photo']
    s = faculty(experience=exp,subject=subject,quali=qualification,name=name, Regno=regno, gender=gender, address=address, dob=dob,
                 doj=doj, image=photo)
    s.save()
    all = faculty.objects.all()
    return render(request,"showfaculty.html",{"data":all})


def facultylogin(request):
     return render(request,"flogin.html")


def facultywel(request):
    try:
        name = request.POST.get("name")
        pas = request.POST.get("pas")
        all = faculty.objects.get(name=name,pasword=pas)
        if name==all.name and pas==all.pasword:
          request.session["uname"] = all.name
          return redirect('faculwelcome')
    except faculty.DoesNotExist:
        message = "please enter the correct username and password"
        return render(request, "flogin.html", {"message": "inavalid"})


def addstudentsmarks(request):
    res = request.session.get("uname")
    if res:
        return render(request, "addmarks.html")
    else:
        return redirect("flog")



def stlogin(request):
    name=request.POST.get("std1")
    regno=request.POST.get("reg")
    all = students.objects.all()
    for x in all:
      if x.name==name and x.Regno==regno:
       return render(request,"stlogin.html",{"data":all,"name":name,"reg":regno})
    return render(request,"addmarks.html",{"message":"invalid students name"})

def conformation(request):
    name=request.POST.get("name")
    reg=request.POST.get("reg")
    return render(request,"confomation.html",{"data":name,"reg":reg})

def addmarks(request):
    all=students.objects.all()
    sname = request.POST.get("std1")
    sreg = request.POST.get("reg")
    for x in all:
        if x.name==sname and x.Regno==sreg:

          en=request.POST.get("e1")
          ka=request.POST.get("k1")
          hi=request.POST.get("h1")
          so=request.POST.get("s1")
          sos=request.POST.get("ss1")
          mat=request.POST.get("m1")
          tot=request.POST.get("t1")
          per=request.POST.get("p1")
          return render(request,"addstudentsmarks.html")


def searchstudents(request):
    return render(request,"serach.html",{"data":all})


def findstudent(request):
    try:
        name = request.POST.get("n1")
        reg = request.POST.get("r1")
        all = students.objects.get(name=name,Regno=reg)
        if name == all.name and reg == all.Regno:
            request.session["uname"] = all.name
            return redirect('stwel')
    except students.DoesNotExist:
        message = "please enter the correct username and password"
        return render(request, "serach.html", {"message": "invalid user name and password"})



def contactus(request):
    return render(request,"contactus.html")


def feedback(request):
    name=request.POST["n1"]
    email=request.POST["e1"]
    message=request.POST["m1"]
    feedbackmodel(name=name,email=email,message=message).save()
    return render(request,"contactus.html")


def viewfeedback(request):
    res = request.session.get("uname")
    if res:
        all = feedbackmodel.objects.all()
        return render(request, "viewfeedback.html", {"data": all})
    else:
        return redirect("add")




def studentsupdatebyfuc(request):
    regno = request.GET.get("regno")
    a = students.objects.get(Regno=regno)
    return render(request, "updatebyfaculty.html", {"data": a})


def studentsindex(request):
    return render(request,"studentsindex.html")


def viewpasslist(request):
    res = request.session.get("uname")
    if res:
        return render(request, "result.html")
    else:
        return redirect("flog")



def getlists(request):
    res = request.session.get("uname")
    if res:
        all = students.objects.all()
        sand = request.POST.get("n1")
        ss = int(sand)
        return render(request, "list.html", {"data": all, "sa": ss})
    else:
        return redirect("flog")



def getfailstud(request):
    res = request.session.get("uname")
    if res:
        return render(request, "faillist.html")
    else:
        return redirect("flog")



def failstudentslist(request):
    res = request.session.get("uname")
    if res:
        all = students.objects.all()
        sand = request.POST.get("n1")
        ss = int(sand)
        return render(request, "failstudentslist.html", {"data": all, "sa": ss})
    else:
        return redirect("flog")



def getpasslist(request):
    res = request.session.get("uname")
    if res:
        return render(request, "getpasslist.html")
    else:
        return redirect("flog")



def passstudentslist(request):
    res = request.session.get("uname")
    if res:
        all = students.objects.all()
        sand = request.POST.get("n1")
        ss = int(sand)
        return render(request, "passstudnets.html", {"data": all, "sa": ss})
    else:
        return redirect("flog")



def changepassword(request):
    return render(request,"changepassword.html")


def updatepassword(request):
    name=request.POST["n1"]
    password=request.POST["n2"]
    all=faculty.objects.all()
    for x in all:
        if name==x.name and password==x.pasword:
            return render(request,"updatepassword.html")
    return render(request, "changepassword.html",{"message":"invalid username and password"})


def conformationpassword(request):
    regno=request.POST["n1"]
    passw=request.POST["n2"]
    con=request.POST["n3"]
    res=faculty.objects.all()
    for x in res:
      if regno==x.Regno and passw==x.pasword:
        res=faculty.objects.filter(Regno=regno)
        res.update(pasword=con)
        return render(request,"updatepassword.html",{"data":"update successfully"})
      else:
          return render(request, "updatepassword.html", {"data1": "plase enter correct regno an password"})


def notification(request):
    res = request.session.get("uname")
    if res:
        ss = uploadnotificationmodel.objects.all()
        return render(request, "notification.html", {"data": ss})
    else:
        return redirect("search")


def uploadnotification(request):
    return render(request,"uploadnotif.html")


def savenotification(request):
    name=request.POST["t1"]
    file=request.POST["t2"]
    uploadnotificationmodel(name=name,file=file).save()
    return render(request,"uploadnotif.html")


def openadmin(request):
    res = request.session.get("uname")
    if res:
        return render(request, "welocome.html")
    else:
        return redirect("add")



def adminlogout(request):
    del request.session["uname"]
    return redirect('log')



def faculwelcome(request):
    res = request.session.get("uname")
    if res:
        all=faculty.objects.get(name=res)
        name=all.name
        pasword=all.pasword
        return render(request, "facultylogin.html",{"data1":faculty.objects.all(),"name":name,"pasword":pasword})
    else:
        return redirect("flog")


def falogout(request):
    del request.session["uname"]
    return redirect('flog')


def stwelcome(request):
    res = request.session.get("uname")
    if res:
        all = students.objects.get(name=res)
        name = all.name
        regno = all.Regno
        return render(request, "find.html", {"data": students.objects.all(), "name": name, "reg": regno})
    else:
        return redirect("search")


def stlogout(request):
    del request.session["uname"]
    return redirect('search')


def forgetpassword(request):
    return render(request,"forgetpassword.html")


def sendotp(request):
    name=request.POST["n1"]
    reg=request.POST["n2"]
    all=faculty.objects.all()
    for x in all:
        if x.name==name and x.Regno==reg:
            return render(request,"userinputpage.html",{"name":name,"reg":reg})
        else:
            return render(request,"forgetpassword.html",{"data":"invalid username and password"})


def sendmail(request):
    name = request.POST["n1"]
    reg = request.POST["n2"]
    email=request.POST["n3"]
    all = faculty.objects.all()
    for x in all:
        if x.name == name and x.Regno == reg:
            import random
            otp2 = random.randint(100000, 999999)
            # otp(otp1=otp2).save()
            k = otp.objects.filter(id=1)
            k.update(otp1=otp2)
            sub = "this is otp"
            mess = "hello word""  " + str(otp2)
            send_mail(sub, mess, se.EMAIL_HOST_USER, [email])
            return render(request, "otpvalidation.html",{"message": "PLAESE ENTER VALID OTP"})
        else:
            return render(request,"userinputpage.html",{"message":"invalid username and password"})


def checkotp(request):
    all = otp.objects.all()
    ss = request.POST["n1"]
    print(type(ss))
    print(ss)
    print(type(ss))
    for x in all:
        if str(x.otp1) == str(ss):
            return render(request, "updateforgetpassword.html", {"data": all})
        else:
            return render(request, 'otpvalidation.html',{"message":"plase enter correct otp"})


def updatepass1(request):
    all = faculty.objects.all()
    name = request.POST["n1"]
    reg = request.POST["n2"]
    password = request.POST["n3"]
    conform = request.POST["n4"]
    for x in all:
        if x.Regno == reg and x.name == name and conform == password:
            res = faculty.objects.filter(Regno=reg)
            res.update(name=name, Regno=reg, pasword=password)
            return render(request, "forgetpassword.html", {"message": "password change successful"})
        else:
            return render(request, "updateforgetpassword.html", {"message": "this user name not avialable"})
