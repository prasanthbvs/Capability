# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import LoginSerializer
# Create your views here.

class Login_Api(generics.GenericAPIView):
    print "In api view"
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        print "I am in post"
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user":LoginSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)
        })
