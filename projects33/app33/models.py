from django.db import models
class students(models.Model):
    Regno=models.CharField(primary_key=True,default=False,max_length=30)
    name=models.CharField(max_length=30)
    father=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    dob=models.DateField()
    doj=models.DateField()
    standards=models.IntegerField()
    image = models.ImageField(upload_to='students/')
    english = models.IntegerField(default=False)
    kannad = models.IntegerField(default=False)
    hindi = models.IntegerField(default=False)
    science = models.IntegerField(default=False)
    social_science = models.IntegerField(default=False)
    mathematics = models.IntegerField(default=False)
    totalmarks = models.IntegerField(default=False)
    percentage = models.DecimalField(max_digits=20, decimal_places=2, default=False)
class faculty(models.Model):
    Regno = models.CharField(primary_key=True,max_length=30,default=False,unique=True)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    experience=models.IntegerField()
    address = models.CharField(max_length=100)
    dob = models.DateField()
    pasword=models.CharField(default=False,max_length=10)
    doj = models.DateField()
    quali=models.CharField(max_length=30)
    image = models.ImageField(upload_to='faculty/')
class feedbackmodel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.CharField(max_length=1000)
class uploadnotificationmodel(models.Model):
    name=models.CharField(max_length=1000)
    file=models.FileField()

class otp(models.Model):
    otp1=models.IntegerField()


