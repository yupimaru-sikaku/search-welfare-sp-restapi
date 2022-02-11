from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import OfficeViewSet, CreateUserView, CompanyViewSet, CompanyRetrieveView, OfficeListView, \
    OfficeRetrieveView, CompanyListView, OfficeCompanyListView

router = routers.DefaultRouter()
router.register('offices', OfficeViewSet, basename='offices')
router.register('companies', CompanyViewSet, basename='companies')


urlpatterns = [
    path('list-company/', CompanyListView.as_view(), name='list-company'),
    path('detail-company/<int:pk>/', CompanyRetrieveView.as_view(), name='detail-company'),
    path('list-office/', OfficeListView.as_view(), name='list-office'),
    path('detail-office-company/', OfficeCompanyListView.as_view(), name='detail-office-company'),
    path('detail-office/<str:pk>/', OfficeRetrieveView.as_view(), name='detail-office'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]