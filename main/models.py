from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta

# Create your models here.
class Student(models.Model):
    sem=models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100,null=True)
    roll_no = models.IntegerField()
    hindi = models.IntegerField(default=0)
    english = models.IntegerField(default=0)
    maths = models.IntegerField(default=0)
    science = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    perecent = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.name

class StudentUnit1(models.Model):
    u1name=models.CharField(max_length=100)
    u1roll_no=models.IntegerField()
    u1hindi=models.IntegerField(default=0)
    u1english=models.IntegerField(default=0)
    u1math=models.IntegerField(default=0)
    u1science=models.IntegerField(default=0)
    u1total=models.IntegerField()
    u1percent=models.DecimalField(max_digits=5,decimal_places=2)

    def __def__(self):
        return self.u1name

class Attendance(models.Model):
    aname=models.CharField(max_length=100)
    arollno=models.CharField(max_length=100)
    total=models.IntegerField()

    def __def__(self):
        return self.aname

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dob = models.DateField(null=True)
    city = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=10, null=True)
    image = models.FileField(null=True,default="")
    en=models.CharField(max_length=90, null=True)
    date = models.CharField(max_length=30, null=True)
    branc=models.CharField(max_length=90, null=True)
    


    

    def __str__(self):
        return self.user.username

class Fee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    stufe=models.IntegerField(null=True)
    upiid=models.IntegerField(null=True)

class AdmitCard(models.Model):
    
    admit=models.CharField(max_length=50, null=True)
    enroll=models.CharField(max_length=50,null=True)
    stname=models.CharField(max_length=50,null=True)
    f_name=models.CharField(max_length=90,null=True)
    add=models.CharField(max_length=100,null=True)
    course=models.CharField(max_length=50,null=True)
    dob=models.DateField(null=True)
    gender=models.CharField(max_length=40,null=True)
    exvenue=models.CharField(max_length=100,null=True)
    sno=models.CharField(max_length=50,null=True)
    sub=models.CharField(max_length=50,null=True)
    exdate=models.DateField(null=True)

    def __str__(self):
        return self.enroll

class CourseRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    studname=models.CharField(max_length=50, null=True)
    fathername=models.CharField(max_length=50, null=True)
    enrollmentno=models.CharField(max_length=50, null=True)
    datob=models.DateField(null=True)
    rollno=models.CharField(max_length=50, null=True)
    branch=models.CharField(max_length=50, null=True)
    semes=models.CharField(max_length=50, null=True)
    pc1=models.CharField(max_length=50,null=True)
    pc1=models.CharField(max_length=50,null=True)
    pc2=models.CharField(max_length=50,null=True)
    pc3=models.CharField(max_length=50,null=True)
    pc4=models.CharField(max_length=50,null=True)
    pc5=models.CharField(max_length=50,null=True)
    pc6=models.CharField(max_length=50,null=True)
    pc7=models.CharField(max_length=50,null=True)
    pc8=models.CharField(max_length=50,null=True)
    pc9=models.CharField(max_length=50,null=True)
    pc10=models.CharField(max_length=50,null=True)
    pc11=models.CharField(max_length=50, null=True)
    pc12=models.CharField(max_length=50,null=True)
    pc13=models.CharField(max_length=50,null=True)
    pc14=models.CharField(max_length=50,null=True)
    pc15=models.CharField(max_length=50,null=True)
    pt1=models.CharField(max_length=50,null=True)
    pt2=models.CharField(max_length=50,null=True)
    pt3=models.CharField(max_length=50,null=True)
    pt4=models.CharField(max_length=50,null=True)
    pt5=models.CharField(max_length=50,null=True)
    pt6=models.CharField(max_length=50,null=True)
    pt7=models.CharField(max_length=50,null=True)
    pt8=models.CharField(max_length=50,null=True)
    pt9=models.CharField(max_length=50,null=True)
    pt10=models.CharField(max_length=50,null=True)
    pt11=models.CharField(max_length=50,null=True)
    pt12=models.CharField(max_length=50,null=True)
    pt13=models.CharField(max_length=50,null=True)
    pt14=models.CharField(max_length=50,null=True)
    pt15=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self .studname


class Student_Feedback(models.Model):
    stunamee=models.CharField(max_length=90, null=True)
    enrollme=models.CharField(max_length=90, null=True)
    emailid=models.CharField(max_length=90, null=True)
    msg=models.TextField(max_length=90, null=True)
    contact=models.BigIntegerField(null=True)
    date = models.CharField(max_length=30, null=True)

    def  __str__(self):
        return self.msg


    
class Send_Feedback(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message1 = models.TextField()
    date = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user.username

    
class Complane(models.Model):
    stu=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    stunameed=models.CharField(max_length=90, null=True)
    enrollmer=models.CharField(max_length=90, null=True)
    emailidr=models.CharField(max_length=90, null=True)
    msge=models.TextField(max_length=90, null=True)
    contactr=models.BigIntegerField(null=True)
    dater = models.CharField(max_length=30, null=True)
    brances=models.CharField(max_length=90, null=True)
    def __str__(self):
        return self.stunameed

class dfcom(models.Model):
    an=models.CharField(max_length=90, null=True)
    asdf=models.CharField(max_length=90, null=True)

class Marksheet(models.Model):
    stunam=models.CharField(max_length=90, null=True)
    fathnm=models.CharField(max_length=90, null=True)
    rno=models.CharField(max_length=90, null=True)
    enrollme=models.CharField(max_length=90, null=True)
    category=models.CharField(max_length=90, null=True)
    br=models.CharField(max_length=90 , null=True)
    semesterrr=models.CharField(max_length=90, null=True)
    sirialno=models.IntegerField(default=0)
    subcode1=models.CharField(max_length=90, null=True)
    subcode2=models.CharField(max_length=90, null=True)
    subcode3=models.CharField(max_length=90, null=True)
    subcode4=models.CharField(max_length=90, null=True)
    subcode5=models.CharField(max_length=90, null=True)
    subcode6=models.CharField(max_length=90, null=True)
    subcode7=models.CharField(max_length=90, null=True)
    subcode8=models.CharField(max_length=90, null=True)
    subcode9=models.CharField(max_length=90, null=True)
    subcode10=models.CharField(max_length=90, null=True)
    subcode11=models.CharField(max_length=90, null=True)
    subcode12=models.CharField(max_length=90, null=True)
    subcode13=models.CharField(max_length=90, null=True)
    subcode14=models.CharField(max_length=90, null=True)
    subcode15=models.CharField(max_length=90, null=True)
    paper1=models.CharField(max_length=90, null=True)
    paper2=models.CharField(max_length=90, null=True)
    paper3=models.CharField(max_length=90, null=True)
    paper4=models.CharField(max_length=90, null=True)
    paper5=models.CharField(max_length=90, null=True)
    paper6=models.CharField(max_length=90, null=True)
    paper7=models.CharField(max_length=90, null=True)
    paper8=models.CharField(max_length=90, null=True)
    paper9=models.CharField(max_length=90, null=True)
    paper10=models.CharField(max_length=90, null=True)
    paper11=models.CharField(max_length=90, null=True)
    paper12=models.CharField(max_length=90, null=True)
    paper13=models.CharField(max_length=90, null=True)
    paper14=models.CharField(max_length=90, null=True)
    paper15=models.CharField(max_length=90, null=True)

    intermark=models.IntegerField(default=0)
    intertot=models.IntegerField(default=0)
    unmarks=models.IntegerField(default=0)
    untot=models.IntegerField(default=0)
    totalinun=models.IntegerField(default=0)
    totalinnummax=models.IntegerField(default=0)
    totalint=models.IntegerField(default=0)
    totalintmax=models.IntegerField(default=0)
    totalun=models.IntegerField(default=0)
    totalunmax=models.IntegerField(default=0)
    totalin=models.IntegerField(default=0)
    totalmaxnu=models.IntegerField(default=0)
    remark=models.CharField(max_length=90, null=True)
    total_per=models.IntegerField(default=0)
    semseexamda=models.CharField(max_length=90, null=True)

    def __str__(self):
        return self.stunam


class Vehicle(models.Model):
    parkingnumber = models.CharField(max_length=20)
    vehiclecompany = models.CharField(max_length=50)
    regno = models.CharField(max_length=10)
    ownername = models.CharField(max_length=50)
    ownercontact = models.CharField(max_length=15)
    pdate = models.DateField()
    intime = models.CharField(max_length=50)
    outtime = models.CharField(max_length=50)
    parkingcharge = models.CharField(max_length=50)
    remark = models.CharField(max_length=500)
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.parkingnumber


class mark(models.Model):
    ro=models.CharField(max_length=90, null=True)
    total=models.CharField(max_length=90, null=True)

class TimeTable(models.Model):
    course=models.CharField(max_length=90, null=True)
    semester=models.CharField(max_length=90, null=True)
    subj1=models.CharField(max_length=90, null=True)
    subj2=models.CharField(max_length=90, null=True)
    subj3=models.CharField(max_length=90, null=True)
    subj4=models.CharField(max_length=90, null=True)
    subj5=models.CharField(max_length=90, null=True)
    subj6=models.CharField(max_length=90, null=True)
    subj7=models.CharField(max_length=90, null=True)
    subj8=models.CharField(max_length=90, null=True)
    subj9=models.CharField(max_length=90, null=True)
    subj10=models.CharField(max_length=90, null=True)
    time1=models.CharField(max_length=90, null=True)
    time2=models.CharField(max_length=90, null=True)
    time3=models.CharField(max_length=90, null=True)
    time4=models.CharField(max_length=90, null=True)
    time5=models.CharField(max_length=90, null=True)
    time6=models.CharField(max_length=90, null=True)
    time7=models.CharField(max_length=90, null=True)
    time8=models.CharField(max_length=90, null=True)
    time9=models.CharField(max_length=90, null=True)
    time10=models.CharField(max_length=90, null=True)

    def __str__(self):
        return self.semester

def get_expiry():
    return datetime.today() + timedelta(days=15)
class Fepayment(models.Model):
    fe=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    prof=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    adm=models.ForeignKey(AdmitCard,on_delete=models.CASCADE,null=True)
    issuedate=models.DateField(auto_now=True)
    expiredate=models.DateField(default=get_expiry)
    pay=models.IntegerField()
    enl=models.CharField(max_length=90, null=True)
    upiid=models.CharField(max_length=90, null=True)
    






class Feepay(models.Model):
    stuname=models.CharField(max_length=90,null=True)
    sten=models.CharField(max_length=90,null=True)
    stemail=models.CharField(max_length=90,null=True)
    stcon=models.IntegerField(null=True)
    stbranch=models.CharField(max_length=90,null=True)
    stdob=models.DateField()
    stfee=models.IntegerField(null=True)
    stfeex=models.IntegerField(null=True)
    sttotalfee=models.IntegerField(null=True)
    # penaltyfee=models.IntegerField(null=True)
    # cardno=models.CharField(max_length=90,null=True)
    # cardname=models.CharField(max_length=90,null=True)
    # dat=models.DateField()
    # month=models.CharField(max_length=90,null=True)
    # cvv=models.CharField(max_digits=90,null=True)

    def __str__(self):
        return self.sten


class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    subject = models.CharField(max_length=30,null=True)
    notesfile = models.FileField(null=True)
    filetype = models.CharField(max_length=30)
    description = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username+" "+self.status


    


class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    regi=models.ForeignKey(Profile,on_delete=models.CASCADE, default=1)
    uploadingdate = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    status = models.CharField(max_length=15)
    fnamee=models.CharField(max_length=90,null=True)
    lasnam=models.CharField(max_length=90,null=True)
    fathnam=models.CharField(max_length=90, null=True)
    mathnamee=models.CharField(max_length=90,null=True)
    gen=models.CharField(max_length=90,null=True)
    cotac=models.IntegerField(null=True)
    em=models.CharField(max_length=90,null=True)
    datob=models.DateField(null=True)
    regist=models.IntegerField( null=True)
    cona=models.IntegerField(null=True)
    cit=models.CharField(max_length=90,null=True)
    fulad=models.CharField(max_length=90,null=True)
    pc=models.IntegerField(null=True)
    adharcard = models.FileField(null=True)
    transc = models.FileField(null=True)
    notesfile = models.FileField(null=True)
    mgc = models.FileField(null=True)
    marksheet = models.FileField(null=True)

    def __str__(self):
        return self.user.username+" "+self.status



    