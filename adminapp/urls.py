from django.urls import path
from .views import home_page, kunlik_monitoring_page, \
    xaftalik_monitoring_page, oylik_monitoring_page, yillik_monitoring_page, \
    shaharlar, malumot_kiritish, success, login_page, logout_page, \
    person_info_page, error_page, export_xls

urlpatterns = [
    path('', home_page, name='home_page'),

    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),

    path('monitoring/kunlik/', kunlik_monitoring_page, name='kunlik_monitoring_page'),
    path('monitoring/xaftalik/', xaftalik_monitoring_page, name='xaftalik_monitoring_page'),
    path('monitoring/oylik/', oylik_monitoring_page, name='oylik_monitoring_page'),
    path('monitoring/yillik/', yillik_monitoring_page, name='yillik_monitoring_page'),
    path('malumot-kiritish/', malumot_kiritish, name='malumot_kiritish_page'),
    path('success/', success, name='success_page'),
    path('hudud/<str:pk>/', shaharlar, name='shaharlar'),
    path('person/<str:pk>/', person_info_page, name='person_info_page'),

    path('error/', error_page, name='error_page'),
]