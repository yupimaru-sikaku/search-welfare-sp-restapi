from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import OfficeViewSet, CreateUserView, CompanyViewSet, CompanyRetrieveView, OfficeListView, \
    OfficeRetrieveView, CompanyListView, OfficeCompanyListView, ServiceListView, ServiceViewSet, ServiceRetrieveView, \
    SeriviceOfficeListView

router = routers.DefaultRouter()
router.register('offices', OfficeViewSet, basename='offices')
router.register('companies', CompanyViewSet, basename='companies')
router.register('services', ServiceViewSet, basename='services')


urlpatterns = [
    ######### Company
    path('list-company/', CompanyListView.as_view(), name='list-company'),
    path('detail-company/<int:pk>/', CompanyRetrieveView.as_view(), name='detail-company'),
    ######### Office
    path('list-office/', OfficeListView.as_view(), name='list-office'),
    path('detail-office/<str:pk>/', OfficeRetrieveView.as_view(), name='detail-office'),
    path('detail-office-company/', OfficeCompanyListView.as_view(), name='detail-office-company'),
    ######### Service
    path('list-service/', ServiceListView.as_view(), name='list-service'),
    path('detail-service/<int:pk>/', ServiceRetrieveView.as_view(), name='detail-service'),
    path('detail-service-office/', SeriviceOfficeListView.as_view(), name='detail-service-office'),
    ######### その他
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]