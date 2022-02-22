from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import UserSerializer, CompanySerializer, OfficeSerializer, ServiceSerializer
from .models import Company, Office, Service

######### User
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

######### Company
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Company.objects.all()
        companyName = self.request.query_params.get('companyName', None)
        if companyName is not None:
            queryset = queryset.filter(companyName__icontains=companyName)  # 「__icontains」を追加で部分一致
        return queryset

class CompanyRetrieveView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (AllowAny,)

######### Office
class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = (AllowAny,)

class OfficeListView(generics.ListAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = (AllowAny,)

class OfficeCompanyListView(generics.ListAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Office.objects.all()
        company = self.request.query_params.get('company', None)
        if company is not None:
            queryset = queryset.filter(company=company)
        return queryset

class OfficeRetrieveView(generics.RetrieveAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = (AllowAny,)

######### Service
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (AllowAny,)

class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (AllowAny,)

class SeriviceOfficeListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Service.objects.all()
        office = self.request.query_params.get('office', None)
        if office is not None:
            queryset = queryset.filter(office=office)
        return queryset

class ServiceRetrieveView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (AllowAny,)