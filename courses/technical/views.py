# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from technical.models import Education, Student, BuyCourse, BankDetails, Trascat, StockPredict, StockPredictSell
from rest_framework import viewsets
from technical.serializers import StudentSerializer, BuyCourseSerializer, BankDetailsSerializer, TrascatSerializer, StockPredictSerializer, StockPredictSellSerializer
from django.db import transaction
from technical import predictions_buy, predictions_sell
from rest_framework.throttling import UserRateThrottle
# Create your views here.

class MyViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    throttle_classes = (UserRateThrottle,)

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)

    # @transaction.atomic()
    # #def get_queryset(self):
    # def get(self, request, *args, **kwrgs):
    #     sid  = transaction.savepoint();
    #     obj = query_set.save()
    #
    #     if obj == null:
    #         transaction.savepoint_rollback(s)
    #     else:
    #         try:
    #             transaction.savepoint_commit(s)
    #         except IntegrityError:
    #             transaction.savepoint_rollback(s)

class BankDetailsViewSet(viewsets.ModelViewSet):

    queryset = BankDetails.objects.all()
    serializer_class = BankDetailsSerializer

    def perform_create(self, serializers):
        serializers.save()

    # def get_serializer_context(self):
    #     context = super(BankDetailsViewSet, self).get_serializer_context()
    #     context.update({
    #         "exclude_credit_card_number": BankDetails.objects.all().values('credit_card_number')
    #         # extra data
    #     })
    #     return context

class BuyCourseViewSet(viewsets.ModelViewSet):

    queryset = BuyCourse.objects.all()
    serializer_class = BuyCourseSerializer
class StockPredictViewSet(viewsets.ModelViewSet):

    queryset = StockPredict.objects.all()
    serializer_class = StockPredictSerializer


    def perform_create(self, serializers):
        serializers.save()
    def perform_create(self, serializers):
        serializers.save()

class TrascatViewSet(viewsets.ModelViewSet):

    queryset = Trascat.objects.all()
    serializer_class = TrascatSerializer

    def perform_create(self, serializers):
        serializers.save()

class StockPredictViewSet(viewsets.ModelViewSet):

    queryset = StockPredict.objects.all()
    serializer_class = StockPredictSerializer


    def perform_create(self, serializers):
        serializers.save()

class StockPredictSellViewSet(viewsets.ModelViewSet):

    queryset = StockPredictSell.objects.all()
    serializer_class = StockPredictSellSerializer


    def perform_create(self, serializers):
        serializers.save()
