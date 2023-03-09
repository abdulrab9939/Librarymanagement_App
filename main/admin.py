from django.contrib import admin
from .models import Student
from .models import StudentUnit1
from .models import Attendance
from .models import Profile
from .models import AdmitCard
from .models import CourseRegistration
from .models import Student_Feedback
from .models import Complane
from .models import dfcom
from .models import Marksheet
from .models import Vehicle
from .models import mark
from .models import TimeTable
from .models import Fepayment
from .models import Feepay
from .models import Notes
from .models import Fee






# Register your models here.

admin.site.register(Student)
admin.site.register(Marksheet)
admin.site.register(mark)

admin.site.register(StudentUnit1)
admin.site.register(Attendance)
admin.site.register(Profile)
admin.site.register(AdmitCard)
admin.site.register(CourseRegistration)
admin.site.register(Student_Feedback)
admin.site.register(Complane)
admin.site.register(dfcom)
admin.site.register(Vehicle)
admin.site.register(TimeTable)
admin.site.register(Fepayment)
admin.site.register(Feepay)
admin.site.register(Notes)
admin.site.register(Fee)






