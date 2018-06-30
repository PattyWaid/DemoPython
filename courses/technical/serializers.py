from rest_framework import serializers
import string
import json
import math
from technical.encryption import do_encryption
from technical.predictions_buy import start_prediction_buy
from technical.predictions_sell import start_prediction_sell
from technical.models import Student, BuyCourse, BankDetails, Trascat, StockPredict, StockPredictSell


class StudentSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()
    education = serializers.StringRelatedField()


    class Meta:
        model = Student
        fields = ['id','name','education','grades']

class BankDetailsSerializer(serializers.ModelSerializer):

    student_id = serializers.SerializerMethodField()
    bank_detials_id = serializers.ReadOnlyField()

    class Meta:
        model = BankDetails
        fields = ['bank_detials_id','account_name', 'isn_number', 'bank_name', 'credit_card_number', 'student_id']

    def get_student_id(self, obj):
        name =  obj.account_name.split(' ')[0]
        i = 0
        Present = Student.objects.all().values('name','id')
        while(Present):
            if name == Present[i]['name']:
                return Present[i]['id']
            i = i + 1
        return name



    def validate_credit_card_number(self, credit_card_number):
        #print(BankDetails.objects.filter().values('credit_card_number'))
        Present= BankDetails.objects.filter(credit_card_number = credit_card_number)

        if Present:
            raise serializers.ValidationError("Already Present")
        return credit_card_number


class BuyCourseSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    bank_details = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()
    token = serializers.SerializerMethodField()

    #transact = serializers.SerializerMethodField()

    class Meta:
        model = BuyCourse
        fields = ['id','student_id', 'course_name','amount', 'token', 'bank_details', 'date']

    def get_amount(self, obj):
        return obj.course_name.all().values('amount')

    def get_token(self,obj):
        return  do_encryption((obj.student_id.all().values('name')[0]['name']+obj.id.encode('utf-8')).encode('utf-8'))
        #return query[0]['name']+obj.id.encode('utf-8')


    def get_bank_details(self, obj):
        name =  obj.student_id.all().values('name')[0]['name']
        i=0
        Present = BankDetails.objects.all().values('account_name', 'bank_name')
        while(Present):
            if name == Present[i]['account_name'].split(' ')[0]:
                return Present[i]['bank_name']
            else:
                i=i+1
                continue;
            return 0

    def validate_token(self, token):
        exclude_token = self.context.get("exclude_token", [])
        if token in exclude_token:
            raise ValidationError("Token already exists")


class TrascatSerializer(BuyCourseSerializer):

    from_user = serializers.SerializerMethodField()

    class Meta:
        model = Trascat
        fields = [ 'from_user','transact_with', 'date']


    def get_from_user(self, obj):
        name = Student.objects.all().values('name')
        print(name)
        return name

# This is to generate a range of the limits
value_sell = list()
value_buy = list()
value_range_buy = list()
value_range_sell = list()

def frange(start,stop, step=1.0):
    while start < stop:
        yield start
        start +=step

def check_avail_sell(i):
    print("I:",i)
    print("Inside Check sell:",value_buy)
    k=0
    value_range_buy = []
    for y in frange(i-2,i,0.1):
        value_sell_gen = [round(y,2)]
        value_range_buy.extend(value_sell_gen)
    j=0
    print(value_range_buy)
    while(j<len(value_range_buy)):
        if value_range_buy[j] in value_buy:
            return "The stock with value " + str(value_buy) + " is available to sell"
        j=j+1
    return "There is no buyer available"

def check_avail_buy(i):
    print("I:",i)
    print("Inside Check buy:",value_sell)
    k=0
    value_range_sell = []
    for x in frange(i,i+2,0.1):
        value_buy_gen = [round(x,2)]
        value_range_sell.extend(value_buy_gen)
    j=0
    while(j<len(value_range_sell)):
        if value_range_sell[j] in value_sell:
            print("True")
            return "The stock with value " + str(value_sell) + " is available to buy"
        j=j+1
    return "There is no seller available"

class StockPredictSerializer(serializers.ModelSerializer):

    prediction = serializers.SerializerMethodField()

    class Meta:
        model = StockPredict
        fields = ['id','stock', 'input_price', 'quantity', 'prediction']


    def get_prediction(self, obj):
        for i in start_prediction_buy():
            predicted_buy = [round(i,2)]
            value_buy.extend(predicted_buy)
            del predicted_buy[:]
        check_buy = list()

        for i in value_buy:
            i = round(i,2)
            check_buy_avail = [check_avail_buy(i)]
            check_buy.extend(check_buy_avail)
            del check_buy_avail[:]
            return check_buy


class StockPredictSellSerializer(serializers.ModelSerializer):

    prediction = serializers.SerializerMethodField()

    class Meta:
        model  = StockPredictSell
        fields = ['id','stock', 'sell_price', 'quantity','prediction']

    def get_prediction(self, obj):
        check_sell = list()
        for i in start_prediction_sell():
            print("Predicted :", i)
            predicted_sell = [round(i,2)]
            value_sell.extend(predicted_sell)
            del predicted_sell[:]
            # print(predicted_sell)
        # value_sell.extend(StockPredictSell.objects.all().values('sell_price'))
        for i in value_sell:
            i=round(i,2)
            check_sell_avail = [check_avail_sell(i)]
            print(check_avail_sell(i))
            check_sell.extend(check_sell_avail)
            del check_sell_avail[:]
            return check_sell
        # del check_sell[:]
            # return check_avail(i)
