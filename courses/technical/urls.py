from django.conf.urls import url,include
from technical import views
from technical.views import MyViewSet, BuyCourseViewSet, BankDetailsViewSet, TrascatViewSet, StockPredictViewSet, StockPredictSellViewSet
from rest_framework import routers


router = routers.DefaultRouter()

router.register(
    r'technical', MyViewSet, base_name='transact_list'
)
router.register(
    r'buy_course', BuyCourseViewSet, base_name='buy_course_list'
)
router.register(
    r'bank_details', BankDetailsViewSet, base_name='bank_details_list'
)
router.register(
    r'transact_details', TrascatViewSet, base_name='transact_details_list'
)

router.register(
    r'predict_buy', StockPredictViewSet, base_name='predict_details_list_buy'
)

router.register(
    r'predict_sell', StockPredictSellViewSet, base_name='predict_details_list_sell'
)



urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]
