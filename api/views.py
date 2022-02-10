from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import UserSerializer, CompanyDetailSerializer, OfficeChildSerializer
from .models import Company, Office

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Company.objects.all()
        companyName = self.request.query_params.get('companyName', None)
        if companyName is not None:
            queryset = queryset.filter(companyName__icontains=companyName)  # 「__icontains」を追加する
        return queryset

class CompanyRetrieveView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer
    permission_classes = (AllowAny,)

class CompanyDetailAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer
    lookup_field = 'pk'

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer

class OfficeListView(generics.ListAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeChildSerializer
    permission_classes = (AllowAny,)

class OfficeRetrieveView(generics.RetrieveAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeChildSerializer
    permission_classes = (AllowAny,)

class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeChildSerializer

