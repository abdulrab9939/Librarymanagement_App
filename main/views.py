from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Student
from .models import Attendance
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from .models import AdmitCard
from .models import Send_Feedback
from .models import Student_Feedback
from .models import CourseRegistration
from .models import Complane
from .models import TimeTable
from .models import Fepayment
import socket
from .models import Fepayment
from .models import *

socket.getaddrinfo('localhost', 25)

from django.contrib.auth import authenticate, logout, login
from datetime import date


# Create your views here.

#index
def index(request):
    return render(request, 'index.html')


# Result show 
def result(request):
   
    if request.method == 'POST':
        rollNo = int(request.POST['roll_no'])
        Sem=request.POST['sem']
        student = Student.objects.get(roll_no=rollNo,sem=Sem)
        hindi = student.hindi
        english = student.english
        maths = student.maths
        science = student.science
        total = hindi+english+maths+science
        percent = total/400*100
        if(percent<33):
            status = 'Fail'
        else:
            status = 'Pass'
        params = {
            'sem':   Sem,
            'roll_no': rollNo,
            'name': student.name,
            'hindi': hindi,
            'english': english,
            'maths': maths,
            'science': science,
            'total': total,
            'percent': percent,
            'status': status
        }
        # print('get method', student.name)
        return render(request, 'result.html', params)
    else:
        print('get method')
    return render(request, 'result.html')

#show all sem result
# def showallsemresult(request):
#     return render(request,'showallsemresult.html')

#admin login
def Admin_Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "yes"
            else:
                error = "not"
        except:
            error = "not"
    d = {'error': error}
    return render(request, 'loginadmin.html', d)
#admin-pannal
def admin_panel(request):
    if 'user' in request.session:
        students = Student.objects.all()
        attend=Attendance.objects.all()
        admitc=AdmitCard.objects.all()
        coursean=CourseRegistration.objects.all()
        timetab=TimeTable.objects.all()
        fepay=Fepayment.objects.all()

        params = {'students': students,'attend':attend,'admitc':admitc,'coursean':coursean,'timetab':timetab,'fepay':fepay}
        return render(request, 'admin_panel.html',params)
    else:
        if request.method == 'POST':
            user_name = request.POST['uname']
            pass_word = request.POST['pwd']
            if user_name == 'asad' and pass_word == 'asad9939':
                request.session['user'] = user_name
                students = Student.objects.all()
                attend=Attendance.objects.all()
                admit=AdmitCard.objects.all()
                coursean=CourseRegistration.objects.all()
                timetab=TimeTable.objects.all()
                fepay=Fepayment.objects.all()



                params = {'students': students,'attend':attend,'admit':admit,'coursean':coursean,'timetab':timetab,
                'fepay':fepay}
                return render(request, 'admin_panel.html', params)
            else:
                return render(request, 'loginadmin.html')
        else:
            return render(request, 'loginadmin.html')



#delete student
def delete_student(request, id):
    get_stu = Student.objects.get(id=id)
    get_stu.delete()
    return redirect('/admin_panel')

#edit student
def edit_student(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    get_stu = Student.objects.get(id=id)
    params = {'student': get_stu}
    return render(request, 'edit.html', params)

#edit conform
def edit_confirm(request, id):
    if request.method == 'POST':
        get_stu = Student.objects.get(id=id)
        get_stu.name = request.POST['sname']
        get_stu.roll_no = request.POST['roll-no']
        get_stu.hindi = request.POST['hindi']
        get_stu.english = request.POST['english']
        get_stu.maths = request.POST['maths']
        get_stu.science = request.POST['science']
        total = int(request.POST['hindi'])+int(request.POST['english'])+int(request.POST['maths'])+int(request.POST['science'])
        get_stu.total = total
        get_stu.perecent = total/4
        get_stu.save()
        return redirect('/admin_panel')
    else:
        return redirect('/admin_login')

#admin logout
# def admin_logout(request):
#     del request.session['user']
#     return redirect('/')

#add student
def add_student(request):
    return render(request, 'add_student.html')

#add conform

def add_confirm(request):
    if request.method == 'POST':
        seme=request.POST['sem']
        sname = request.POST['sname']
        roll_no = request.POST['roll-no']
        hindi = int(request.POST['hindi'])
        english = int(request.POST['english'])
        maths = int(request.POST['maths'])
        science = int(request.POST['science'])
        total = hindi+english+maths+science
        percent = total/400*100
        add_student = Student.objects.create(sem=seme,name=sname,roll_no=roll_no,
                        hindi=hindi,english=english,maths=maths,science=science,
                        total=total,perecent=percent)
        add_student.save()
        return redirect('/admin_panel')
    else:
        return redirect('/admin_panel')

#attendance

def attendance(request):
   
    if request.method == 'POST':
        arollNo = request.POST['arollno']

        attendance = Attendance.objects.get(arollno=arollNo)
        atotal =attendance.total
        if(atotal<33):
            status = 'Fail'
        else:
            status = 'Pass'
        contaxt = {
            'arollno': arollNo,
            'aname': attendance.aname,
            'atotal': atotal,
            'status': status
        }
        return render(request, 'stuattendaces.html',contaxt)
    else:
        print('get method')
    return render(request,'stuattendaces.html')


def add_attendance(request):
    return render(request, 'add_attendance.html')

def add_attendconfirm(request):
    if request.method == 'POST':
        atname = request.POST['stname']
        atroll_no = request.POST['stroll_no']
        attotal=request.POST['ttotal']
        add_attend = Attendance.objects.create(aname=atname,arollno=atroll_no,
                        total=attotal)
        add_attend.save()
        return redirect('/admin_panel')
    else:
        return redirect('/admin_panel')

#delete student
def delete_stuattend(request, id):
    get_stuattend = Attendance.objects.get(id=id)
    get_stuattend.delete()
    return redirect('/admin_panel')

#search by admin
def search(request):
    given_name=request.POST['name']
    students=Student.objects.filter(name__iexact=given_name)
    return render(request,'admin_panel.html',{'students':students})



def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'home.html')
    
def attendancecheck(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'attendancecheck.html')

def sturegister(request):
    return render(request,'sturegister.html')
#signup student
def Signup(request):
    error = False
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        p = request.POST['pwd']
        d = request.POST['date']
        c = request.POST['city']
        ad = request.POST['add']
        e = request.POST['email']
        i = request.FILES['image']
        con = request.POST['contact']
        et=request.POST['enrollmen']
        br=request.POST['bra']
        user = User.objects.create_user(username=u, email=e, password=p, first_name=f, last_name=l)
        Profile.objects.create(user=user, dob=d, city=c, address=ad, contact=con, image=i,en=et,branc=br)
        send_mail(
            'WEL COME TO IUMS',
            f'Hi ! {f} ,your account has been successfully registered in IUMS now you can login your \naccount  \n \n your username is:- {u} \n \nPassword is:- {p}\n \n Thankyou\n' ,
            'abdulrab4546@gmail.com',
            [e,],  
            fail_silently=False,
            )
        error = True
    d = {'error': error}
    return render(request, 'sturegister.html', d)

def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = "yes"
            else:
                error = "not"
        except:
            error = "not"
    d = {'error': error}
    return render(request, 'login.html', d)
    
def Logout(request):
    logout(request)
    return redirect('home')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    pro = Profile.objects.get(user=user)
    d = {'pro': pro, 'user': user}
    return render(request, 'profile.html', d)



def Edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = False
    user = User.objects.get(id=request.user.id)
    pro = Profile.objects.get(user=user)
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        c = request.POST['city']
        ad = request.POST['add']
        e = request.POST['email']
        con = request.POST['contact']
        d = request.POST['date']

        try:
            i = request.FILES['img']
            pro.image = i
            pro.save()

        except:
            pass

        if d:
            try:
                pro.dob = d
                pro.save()
            except:
                pass
        else:
            pass

        pro.user.username = u
        pro.user.first_name = f
        pro.user.last_name = l
        pro.user.email = e
        pro.contact = con
        pro.city = c
        pro.address = ad
        pro.save()
        error = True
    d = {'error': error, 'pro': pro}
    return render(request,'editprofile.html',d)

def Admitcard(request):
    if request.method == 'POST':
        Enrol = request.POST['enroll']
        admitcar = AdmitCard.objects.get(enroll=Enrol)
        st=admitcar.stname
        ad=admitcar.admit
        fn=admitcar.f_name
        ad=admitcar.add
        cr=admitcar.course
        bi=admitcar.dob
        ev=admitcar.exvenue
        sn=admitcar.sno
        sb=admitcar.sub
        edate=admitcar.exdate
        sex=admitcar.gender
        params = {
            'enroll':   Enrol,
            'admit': ad,
            'f_name': fn,
            'stname':st,
            'add': ad,
            'course': cr,
            'dob': bi,
            'exvenue': ev,
            'gender':sex,
            'sno': sn,
            'sub': sb,
            'exdate': edate
        }
        return render(request, 'stuadmitcard.html',params)
    else:
        print('get method')
    return render(request,'stuadmitcard.html')


def add_admitcard(request):
    return render(request,'addadmitcard.html')

def admitcheck(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request,'admitcarform.html')

def add_admitcardconfirm(request):
    if request.method == 'POST':
        enr = request.POST['enrolno']
        stuname = request.POST['st_name']
        fa_namee=request.POST['faname']
        address=request.POST['add']
        do=request.POST['course']
        daof=request.POST['dob']
        gen=request.POST['gender']
        exam=request.POST['exvenue']
        subj=request.POST['sub']
        examdate=request.POST['asd']
        sirialno=request.POST['sno']
        add_admit = AdmitCard.objects.create(enroll=enr,stname=stuname,
        f_name=fa_namee,add=address,course=do,dob=daof,gender=gen,exvenue=exam,sub=subj,exdate=examdate,sno=sirialno)
        add_admit.save()
        return redirect('/admin_panel')
    else:
        return redirect('/admin_panel')

#course
def courseregis(request):
    if request.method == 'POST':
        enrole = request.POST['enrollmentno']
        branc=request.POST['branch']
        semest=request.POST['semes']
        coursereges = CourseRegistration.objects.get(enrollmentno=enrole,branch=branc,semes=semest)
        st = coursereges.studname
        fanam = coursereges.fathername
        dat = coursereges.datob
        rol=coursereges.rollno
        pco1=coursereges.pc1
        pco2=coursereges.pc2
        pco3=coursereges.pc3
        pco4=coursereges.pc4
        pco5=coursereges.pc5
        pco6=coursereges.pc6
        pco7=coursereges.pc7
        pco8=coursereges.pc8
        pco9=coursereges.pc9
        pco10=coursereges.pc10
        pco11=coursereges.pc11
        pco12=coursereges.pc12
        pco13=coursereges.pc13
        pco14=coursereges.pc14
        pco15=coursereges.pc15
        pts1=coursereges.pt1
        pts2=coursereges.pt2
        pts3=coursereges.pt3
        pts4=coursereges.pt4
        pts5=coursereges.pt5
        pts6=coursereges.pt6
        pts7=coursereges.pt7
        pts8=coursereges.pt8
        pts9=coursereges.pt9
        pts10=coursereges.pt10
        pts11=coursereges.pt11
        pts12=coursereges.pt12
        pts13=coursereges.pt13
        pts14=coursereges.pt14
        pts15=coursereges.pt15

        params = {
            'enrollmentno':   enrole,
            'branch': branc,
            'semes': semest,
            'studname': st,
            'fathername': fanam,
            'datob': dat,
            'rollno':rol,
            'pc1':pco1,
            'pc2':pco2,
            'pc3':pco3,
            'pc4':pco4,
            'pc5':pco5,
            'pc6':pco6,
            'pc7':pco7,
            'pc8':pco8,
            'pc9':pco9,
            'pc10':pco10,
            'pc11':pco11,
            'pc12':pco12,
            'pc13':pco13,
            'pc14':pco14,
            'pc15':pco15,
            'pt1':pts1,
            'pt2':pts2,
            'pt3':pts3,
            'pt4':pts4,
            'pt5':pts5,
            'pt6':pts6,
            'pt7':pts7,
            'pt8':pts8,
            'pt9':pts9,
            'pt10':pts10,
            'pt11':pts11,
            'pt12':pts12,
            'pt13':pts13,
            'pt14':pts14,
            'pt15':pts15,


        }
        # print('get method', student.name)
        return render(request, 'coursereg.html', params)
    else:
        print('get method')
    return render(request, 'coursereg.html')

def add_courseregistration(request):
    return render(request, 'add_courseregistration.html')

def add_courseconform(request):
    if request.method == 'POST':
        stn=request.POST['stud']
        enro = request.POST['enrollm']
        fathname = request.POST['fname']
        janm = request.POST['dateofb']
        bran = request.POST['bra']
        semester = request.POST['semest']
        rno = request.POST['rol']
        pcode1=request.POST['pac1']
        pcode2=request.POST['pac2']
        pcode3=request.POST['pac3']
        pcode4=request.POST['pac4']
        pcode5=request.POST['pac5']
        pcode6=request.POST['pac6']
        pcode7=request.POST['pac7']
        pcode8=request.POST['pac8']
        pcode9=request.POST['pac9']
        pcode10=request.POST['pac10']
        pcode11=request.POST['pac11']
        pcode12=request.POST['pac12']
        pcode13=request.POST['pac13']
        pcode14=request.POST['pac14']
        pcode15=request.POST['pac15']
        papt1=request.POST['pat1']
        papt2=request.POST['pat2']
        papt3=request.POST['pat3']
        papt4=request.POST['pat4']
        papt5=request.POST['pat5']
        papt6=request.POST['pat6']
        papt7=request.POST['pat7']
        papt8=request.POST['pat8']
        papt9=request.POST['pat9']
        papt10=request.POST['pat10']
        papt11=request.POST['pat11']
        papt12=request.POST['pat12']
        papt13=request.POST['pat13']
        papt14=request.POST['pat14']
        papt15=request.POST['pat15']
       


        


        add_course = CourseRegistration.objects.create(studname=stn,fathername=fathname,enrollmentno=enro,
                        datob=janm,rollno=rno,branch=bran,semes=semester,pc1=pcode1,pc2=pcode2,pc3=pcode3,pc4=pcode4,pc5=pcode5,pc6=pcode6,pc7=pcode7,pc8=pcode8,pc9=pcode9,pc10=pcode10,pc11=pcode11,pc12=pcode12,pc13=pcode13,pc14=pcode14,pc15=pcode15,
                        pt1=papt1,pt2=papt2,pt3=papt3,pt4=papt4,pt5=papt5,pt6=papt6,pt7=papt7,pt8=papt8,pt9=papt9,pt10=papt10,pt11=papt11,pt12=papt12,pt13=papt13,pt14=papt14,pt15=papt15)
        add_course.save()
        return redirect('/admin_panel')
    else:
        return redirect('/admin_panel')

def coursecheck(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'coursecheckform.html')


def View_feedback(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    feed = Student_Feedback.objects.all()
    d = {'feed': feed}
    return render(request, 'view_feedback.html', d)

def View_complaint(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    feed = Complane.objects.all()
    d = {'feed': feed}
    return render(request,'viewcomplaint.html', d)



def stuFeedbacksave(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    date1 = date.today()
    if request.method=='POST':
        fe=Student_Feedback()
        namee=request.POST.get('nam')
        en=request.POST.get('enrolm')
        em=request.POST.get('emailme')
        ms=request.POST.get('desc')
        cont=request.POST.get('conta')
        da=request.POST.get('dat')
        fe.stunamee=namee
        fe.enrollme=en
        fe.emailid=em
        fe.msg=ms
        fe.contact=cont
        fe.date=da
        fe.save()
        return redirect('home')
    pro = Profile.objects.get(user=user)
    d = {'pro': pro, 'user': user,'date1':date1}
    return render(request, 'feedbacksave.html', d)



def stuFeedback(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    error = False
    user1 = User.objects.get(id=request.user.id)
    date1 = date.today()
    user = User.objects.get(id=pid)
    pro = Profile.objects.filter(user=user).first()
    if request.method == "POST":
        d = request.POST['date']
        u = request.POST['uname']
        e = request.POST['email']
        con = request.POST['contact']
        m = request.POST['desc']
        user = User.objects.filter(username=u, email=e).first()
        Send_Feedback.objects.create(profile=pro, date=d, message1=m)
        error = True
    d = {'pro': pro, 'date1': date1,  'error': error}
    return render(request, 'stufeedback.html', d)

def View_user(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    pro = Profile.objects.all()
    d = {'user': pro}
    return render(request, 'view_user.html', d)

def delete_user(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('view_user')

def delete_feedback(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    feed = Student_Feedback.objects.get(id=pid)
    feed.delete()
    return redirect('view_feedback')

def delete_compalaint(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    feed = Complane.objects.get(id=pid)
    feed.delete()
    return redirect('view_complaint')

def Complaint(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    date1 = date.today()
    if request.method=='POST':
        fe=Complane()
        namee=request.POST.get('nam')
        en=request.POST.get('enrolm')
        em=request.POST.get('emailme')
        ms=request.POST.get('desc')
        cont=request.POST.get('conta')
        da=request.POST.get('dat')
        b=request.POST.get('branchess')
        fe.stunameed=namee
        fe.enrollmer=en
        fe.emailidr=em
        fe.msge=ms
        fe.contactr=cont
        fe.dater=da
        fe.brances=b
        fe.save()
        return redirect('home')
    pro = Profile.objects.get(user=user)
    d = {'pro': pro, 'user': user,'date1':date1}
    return render(request, 'stucomp.html', d)

#change password

def Change_Password(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    num1 = 0
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user)
   
    if request.method == "POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "yes"
        else:
            error = "not"
    d = {'error': error, 'num1': num1}
    return render(request, 'change_password.html', d)

#About us
def About(request):
    return render(request, 'about.html')

#contact
def Contact(request):
    return render(request, 'contact.html')

def Stumarks(request):


    if not request.user.is_authenticated:
        return redirect('login')
    user = AdmitCard.objects.get(id=request.user.id)

    pro = AdmitCard.objects.get(user=user)
    d = {'pro': pro, 'user': user}
    return render(request, 'stucomp.html', d)

    # if request.method=="POST":
    #     Enrol = request.POST['enroll']
    #     admitcar = AdmitCard.objects.get(enroll=Enrol)
    #     st=admitcar.stname
    #     ad=admitcar.admit
    #     fn=admitcar.f_name
    #     ad=admitcar.add
    #     cr=admitcar.course
    #     bi=admitcar.dob
    #     ev=admitcar.exvenue
    #     sn=admitcar.sno
    #     sb=admitcar.sub
    #     edate=admitcar.exdate
    #     sex=admitcar.gender
    #     params = {
    #         'enroll':   Enrol,
    #         'admit': ad,
    #         'f_name': fn,
    #         'stname':st,
    #         'add': ad,
    #         'course': cr,
    #         'dob': bi,
    #         'exvenue': ev,
    #         'gender':sex,
    #         'sno': sn,
    #         'sub': sb,
    #         'exdate': edate
    #     }
    #     return render(request, 'studmarksheet.html',params)
    # else:      
    #     print('get method')
    # return render(request,'studmarksheet.html')
#

#---------------------------------------------------------------------print 






def manage_incomingvehicle(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    vehicle = AdmitCard.objects.filter()
    d = {'vehicle':vehicle}
    return render(request, 'manage_incomingvehicle.html', d)

def view_incomingdetail(request,pid):

    vehicle = AdmitCard.objects.get(id=pid)
    if request.method == 'POST':
        rm = request.POST['sub']
    
    d = {'vehicle': vehicle}
    return render(request,'view_incomingdetail.html', d)

def manage_outgoingvehicle(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    vehicle = AdmitCard.objects.filter()
    d = {'vehicle':vehicle}
    return render(request, 'manage_outgoingvehicle.html', d)


def view_outgoingdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    vehicle = AdmitCard.objects.get(id=pid)
    d = {'vehicle': vehicle}
    return render(request,'view_outgoingdetail.html', d)



def print_detail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    vehicle = AdmitCard.objects.get(id=pid)
    d = {'vehicle': vehicle}
    return render(request,'print.html', d)

def add_timetable(request):
    return render(request,'add_stutimetable.html')

def add_timetableconform(request):
    if request.method == 'POST':
        
        cors=request.POST['bran']
        semest = request.POST['semes']
        subje1 = request.POST['subject1']
        subje2 = request.POST['subject2']
        subje3 = request.POST['subject3']
        subje4 = request.POST['subject4']
        subje5 = request.POST['subject5']
        subje6 = request.POST['subject6']
        subje7 = request.POST['subject7']
        subje8 = request.POST['subject8']
        subje9 = request.POST['subject9']
        subje10 = request.POST['subject10']
        weqt1=request.POST['tim1']
        weqt2=request.POST['tim2']
        weqt3=request.POST['tim3']
        weqt4=request.POST['tim4']
        weqt5=request.POST['tim5']
        weqt6=request.POST['tim6']
        weqt7=request.POST['tim7']
        weqt8=request.POST['tim8']
        weqt9=request.POST['tim9']
        weqt10=request.POST['tim10']
    
        add_timetables = TimeTable.objects.create(course=cors,semester=semest,subj1=subje1,
                        subj2=subje2,subj3=subje3,subj4=subje4,subj5=subje5,subj6=subje6,subj7=subje7,subj8=subje8,subj9=subje9,subj10=subje10,time1=weqt1,time2=weqt2,time3=weqt3,time4=weqt4,time5=weqt5,time6=weqt6,time7=weqt7,time8=weqt8,time9=weqt9,time10=weqt10)
        add_timetables.save()
        return redirect('/admin_panel')
    else:
        return redirect('/admin_panel')

def timetable(request):
    if request.method == 'POST':
        cours = request.POST['branch']
        se=request.POST['semeste']
        timet = TimeTable.objects.get(course=cours,semester=se)
        sub1=timet.subj1
        sub2=timet.subj2
        sub3=timet.subj3
        sub4=timet.subj4
        sub5=timet.subj5
        sub6=timet.subj6
        sub7=timet.subj7
        sub8=timet.subj8
        sub9=timet.subj9
        sub10=timet.subj10
        t1=timet.time1
        t2=timet.time2
        t3=timet.time3
        t4=timet.time4
        t5=timet.time5
        t6=timet.time6
        t7=timet.time7
        t8=timet.time8
        t9=timet.time9
        t10=timet.time10

        params = {
            'course':   cours,
            'semester': sub1,
            'subj1': sub1,
            'subj2':sub2,
            'subj3':sub3,
            'subj4':sub4,
            'subj5':sub5,
            'subj6':sub6,
            'subj7':sub7,
            'subj8':sub8,
            'subj9':sub9,
            'subj10':sub10,
            'time1':t1,
            'time2':t2,
            'time3':t3,
            'time4':t4,
            'time5':t5,
            'time6':t6,
            'time7':t7,
            'time8':t8,
            'time9':t9,
            'time10':t10,
        }
        return render(request, 'timetables.html',params)
    else:
        print('get method')
    return render(request,'timetables.html')

def timetacheck(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request,'search_timetable.html')

def adfepayment(request):
    return render(request,'adfeepayment.html')

def add_fepaymentconform(request):
    if request.method == 'POST':
        fdate = request.POST['fedate']
        exdate = request.POST['fexdate']
        total=request.POST['totalfee']
        upii=request.POST['upi']
        add_fee=Fepayment.objects.create(issuedate=fdate,expiredate=exdate,
                        pay=total,upiid=upii)
        add_fee.save()
        return redirect('/admin_panel')
    else:
        return redirect('/admin_panel')

def fepayment(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    pro = Profile.objects.get(user=user)
    fe=Fepayment.objects.all()
    feee=Fee.objects.all()

    d = {'user':user,'pro':pro,'fe':fe,'feee':feee}
    return render(request,'feepayment.html',d)
   
def feecheck(request):
    return render(request,'feecheck.html')
def successpay(request):
    return render(request,'successpay.html')


#fee payment

def stfepayment(request):
    return render(request,'stfepayment.html')


def stadfepayment(request):
    return render(request,'stadfeepayment.html')


#fee
def upload_notes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method=='POST':
        b = request.POST['branch']
        s = request.POST['subject']
        n = request.FILES['notesfile']
        f = request.POST['filetype']
        d = request.POST['description']
        u = User.objects.filter(username=request.user.username).first()

        try:
            Notes.objects.create(user=u,uploadingdate=date.today(),branch=b,subject=s,notesfile=n,
                                 filetype=f,description=d,status='pending')
            error="no"
        except:
            error="yes"
    return render(request,'upload_notes.html', locals())

def view_mynotes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    notes = Notes.objects.filter(user = user)
    pro = Profile.objects.get(user=user)
    d = {'notes':notes,'pro':pro}
    return render(request,'view_mynotes.html',d)


def pending_notes(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.filter(status = "pending")
    d = {'notes':notes}
    return render(request, 'pending_notes.html',d)

def accepted_notes(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.filter(status = "Accept")
    d = {'notes':notes}
    return render(request, 'accepted_notes.html',d)

def rejected_notes(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.filter(status = "Reject")
    d = {'notes':notes}
    return render(request, 'rejected_notes.html',d)

def all_notes(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.all()
    d = {'notes':notes}
    return render(request, 'all_notes.html',d)


def assign_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.get(id=pid)
    error = ""
    if request.method=='POST':
        s = request.POST['status']
        try:
            notes.status = s
            notes.save()
            error="no"
        except:
            error="yes"
    d = {'notes':notes,'error':error}
    return render(request, 'assign_status.html',d)