from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('home/',views.home, name='home'),
    path('index/', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('marksheet/', views.Stumarks, name='marksheet'),

    path('admin_login/', views.Admin_Login, name='admin_login'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('delete-student/<int:id>/', views.delete_student, name='delete-student'),
    path('edit-student/<int:id>/', views.edit_student, name='edit-student'),
    path('edit-confirm/<int:id>/', views.edit_confirm, name='edit-confirm'),
    # path('logout/', views.admin_logout, name='admin-logout'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_confirm/', views.add_confirm, name='add_confirm'),
    path('search',views.search),
    # path('showallsemresult',views.showallsemresult,name="showallsemresult"),
    #--------------Atendance----------------------
    path('attendance/',views.attendance,name='attendance'),
    path('add_attendance/', views.add_attendance, name='add_attendance'),
    path('add_attendconfirm/', views.add_attendconfirm, name='add_attendconfirm'),
    path('delete-stuattend/<int:id>/', views.delete_stuattend, name='delete-stuattend'),
    path('attendancecheck',views.attendancecheck,name="attendancecheck"),
  #solve
    path('sturegister',views.Signup,name="sturegister"),
    path('',views.Login,name="login"),
    path('logout/',views.Logout, name="logout"),
    path('profile/', views.profile, name='profile'),
    path('edit_profile', views.Edit_profile, name='edit_profile'),
    #admit card
    path('admitcard/',views.Admitcard,name="admitcard"),
    path('add_admit/', views.add_admitcard, name='add_admit'),
    path('add_admitcardconfirm/', views.add_admitcardconfirm, name='add_admitcardconfirm'),
    path('admitcheck/',views.admitcheck,name="admitcheck"),

    #course register
    path('courseregister/',views.courseregis,name="courseregister"),
    path('add_courseregistration/',views.add_courseregistration,name="add_courseregistration"),
    path('add_courseconform/', views.add_courseconform, name='add_courseconform'),
    path('coursecheck/',views.coursecheck,name="coursecheck"),
    #feedback
    path('view_feedback/', views.View_feedback, name='view_feedback'),
    path('stu_feedback/(?P<pid>[0-9]+)/', views.stuFeedback, name='stu_feedback'),
    path('send_feedback/',views.stuFeedbacksave, name='send_feedback'),   
    path('view_user',views.View_user,name="view_user"),
    path('delete_user(?P<int:pid>)/', views.delete_user, name='delete_user'),
    path('delete_feedback(?P<int:pid>)', views.delete_feedback, name='delete_feedback'),
    path('complaint/', views.Complaint, name="complaint"),
    path('view_complaint/', views.View_complaint, name='view_complaint'),
    path('delete_complaints(?P<int:pid>)', views.delete_compalaint, name='delete_complaints'),



    #change pass
    path('change_password', views.Change_Password, name="change_password"),

    #aboutus
    path('about/',views.About,name='about'),

    #contact
    path('contact/',views.Contact,name='contact'),

    #passreset
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='passwordreset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='passwordresetdone.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='passwordresetconform.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='passwordresetcomplete.html'),name='password_reset_complete'),


    path('manage_incomingvehicle',views.manage_incomingvehicle,name='manage_incomingvehicle'),


    path('view_incomingdetail/<int:pid>/',views.view_incomingdetail,name='view_incomingdetail'),
    path('manage_outgoingvehicle/',views.manage_outgoingvehicle,name='manage_outgoingvehicle'),
    path('view_outgoingdetail/<int:pid>/',views.view_outgoingdetail,name='view_outgoingdetail'),
    path('print/<int:pid>',views.print_detail,name='print'),

     #-----------------timetable----------------
    path('add_timetable',views.add_timetable,name='add_timetable'),
    path('add_timetableconform',views.add_timetableconform, name='add_timetableconform'),
    path('timetable',views.timetable,name='timetable'),
    path('timetacheck/',views.timetacheck,name="timetacheck"),


    path('fepayment/',views.fepayment,name='fepayment'),
    path('adfepayment',views.adfepayment,name='adfepayment'),
    path('add_fepaymentconform/', views.add_fepaymentconform, name='add_fepaymentconform'),

    path('feecheck/',views.feecheck,name='feecheck'),
    path('successpayment',views.successpay,name='successpayment'),

    #feepay
    path('stfepayment/',views.stfepayment,name='stfepayment'),
    path('stadfepayment',views.adfepayment,name='stadfepayment'),
    # path('add_fepaymentconform/', views.add_fepaymentconform, name='add_fepaymentconform'),

    path('feecheck/',views.feecheck,name='feecheck'),

#fe
    path('upload_notes', views.upload_notes, name='upload_notes'),
    
    path('view_mynotes', views.view_mynotes, name='view_mynotes'),

    path('pending_notes', views.pending_notes, name='pending_notes'),
    path('accepted_notes', views.accepted_notes, name='accepted_notes'),
    path('rejected_notes', views.rejected_notes, name='rejected_notes'),
    path('all_notes', views.all_notes, name='all_notes'),
    path('assign_status/<int:pid>', views.assign_status, name='assign_status'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)