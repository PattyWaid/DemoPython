# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from technical.models import Student, Education, BuyCourse, Course, BankDetails, StockPredict, StockPredictSell

# Register your models here.
admin.site.register(Student)
admin.site.register(Education)
admin.site.register(BuyCourse)
admin.site.register(Course)
admin.site.register(BankDetails)
admin.site.register(StockPredict)
admin.site.register(StockPredictSell)
#admin.site.register(CourseFees)

class BuyCourseAdmin(admin.ModelAdmin):
    fields = ('id', 'student_name', 'course_name', 'amount')
