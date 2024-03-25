from django.http import Http404
from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions,status
from rest_framework.response import Response
from .models import CustomUser,StudentProfile
from .serializers import (UserSerializer,
                          UserGETSerializer ,
                          StdProfileGETSerializer,
                          UniSuperGETSerializer,
                          CompanyGETSerializer,
                          CompanySuperGETSerializer,
                          )

from rest_framework.permissions import AllowAny

class CustomUserListCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



class RetrieveUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserGETSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        user = UserGETSerializer(user)

        return Response(user.data, status=status.HTTP_200_OK)
    
# class PrrofieListCreateAPIView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]



class RetrieveStudentProfileView(generics.RetrieveAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StdProfileGETSerializer
    permission_classes = [AllowAny]


class RetrieveUniSuperProfileView(generics.RetrieveAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class =UniSuperGETSerializer
    permission_classes = [AllowAny]

class RetrieveCompanyProfileView(generics.RetrieveAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class =CompanyGETSerializer
    permission_classes = [AllowAny]

class RetrieveCompanySuperProfileView(generics.RetrieveAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class =CompanySuperGETSerializer
    permission_classes = [AllowAny]