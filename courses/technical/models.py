# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Education(models.Model):
    education = models.CharField(max_length = 50)

    def __str__(self):
        return self.education

class Course(models.Model):
    name = models.CharField(max_length = 50)
    amount = models.IntegerField(default = '')
    details = models.TextField(default = '0')
    batch = models.CharField(max_length = 50, default = '')

    def __str__(self):
        name =self.name
        return name

class Student(models.Model):
    id  = models.CharField(primary_key = True, max_length = 50, blank=True,)
    name = models.CharField(max_length = 100)
    education = models.ForeignKey(Education, null =True)
    grades = models.CharField(max_length = 10)

    def save(self, *args, **kwargs):

        if self.__class__.objects.all().count() == 0:

            letter =  'A'
            number = 1

            self.id = '{0}{1:03d}'.format(letter,number)  # 'A001' this time
        else:

            last_id = self.__class__.objects.all().order_by("-id")[0].id
            a = last_id.encode('utf-8')

            letter = a[0]
            number = int(a[1:])
            number = number + 1
            if number >= 1000:
                letter = chr(ord(a[0]+1))
                number = 1
                print("number:", number)
                self.id = '{0}{1:03d}'.format(letter,number)
            self.id = '{0}{1:03d}'.format(letter,number)

        super(self.__class__, self).save(*args, **kwargs)


    def __str__(self):
        return self.name


class BankDetails(models.Model):
    bank_detials_id = models.CharField(primary_key = True, max_length = 50, blank =True)
    account_name = models.CharField(max_length = 100, null = False, blank = False, default = '')
    isn_number = models.CharField(max_length = 50, null = False)
    bank_name = models.CharField(max_length = 100, null = False)
    credit_card_number = models.IntegerField(null = False, default = '')#, validators = [validate_credit_card_number])

    def save(self, *args, **kwargs):

        if self.__class__.objects.all().count() == 0:

            letter =  'BANK_ID_'
            number = 1


            self.bank_detials_id = '{0}{1:04d}'.format(letter,number)  # 'A001' this time

        else:
            last_id = self.__class__.objects.all().order_by("-bank_detials_id")[0].bank_detials_id
            a = last_id.encode('utf-8')

            letter = a[0:9]
            number = int(a[10:])
            number = number + 1
            if number >= 10000:
                #letter = chr(ord(a[0]+1))
                number = 1
                print("number:", number)
                self.bank_detials_id = '{0}{1:04d}'.format(letter,number)
            self.bank_detials_id = '{0}{1:04d}'.format(letter,number)

        super(self.__class__, self).save(*args, **kwargs)

    def __str__(self):
        return self.isn_number

# class BuyCourseDetails(models.Model):
#     student_id = models.ManyToManyField(Student, related_name = 'buycourse_studentname')
#     course_name = models.ManyToManyField(Course,  related_name = 'buycourse_coursename')
#
#     class Meta:
#         abstract = True

class BuyCourse(models.Model):
    id = models.CharField(primary_key = True, max_length = 50, blank=True)
    student_id = models.ManyToManyField(Student, related_name = 'buycourse_studentname')
    course_name = models.ManyToManyField(Course,  related_name = 'buycourse_coursename')
    # bank_details = models.ForeignKey(BankDetails, related_name = 'buycourse_bankdetails')

    #amount = models.ForeignKey(Course, null = False, blank = False, default = '0')
    date = datetime.now()

    def save(self, *args, **kwargs):

        if self.__class__.objects.all().count() == 0:

            letter =  'TRANSACT'
            number = 1

            self.id = '{0}{1:04d}'.format(letter,number)  # 'A001' this time

        else:
            last_id = self.__class__.objects.all().order_by("-id")[0].id
            a = last_id.encode('utf-8')

            letter = a[0:8]
            number = int(a[9:])
            number = number + 1
            if number >= 10000:
                #letter = chr(ord(a[0]+1))
                number = 1
                print("number:", number)
                self.id = '{0}{1:04d}'.format(letter,number)
            self.id = '{0}{1:04d}'.format(letter,number)

        super(self.__class__, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.course_name.name)

class Trascat(models.Model):
    transact_with = models.ForeignKey(Student, default='')
    date = datetime.now()

    def __str__(self):
        return self.transact_with.name

class StockPredict(models.Model):
    stock = models.CharField(max_length = 100)
    input_price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField()


    def __str__(self):
        return self.stock

class StockPredictSell(models.Model):
    stock = models.CharField(max_length = 100)
    sell_price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.stock
