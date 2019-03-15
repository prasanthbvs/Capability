# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import question_topic, question_type, question_choices, question_complexity, app_question
from rest_framework import viewsets, generics, permissions, status
from .serializers import Question_topicSerializer,  Question_typeSerializer, Question_complexSerializer, Add_questionSerializer, Choice_questionSerializer ,Add_questionSerializertwo
from rest_framework.decorators import api_view

# -------------------Question_Type Api------------------------------------------------------
# creating view function for post and get method through serializers
@api_view(['GET','POST'])
def question_typeList(request):
    if request.method == 'GET':
        queryset = question_type.objects.all() #query for getting all set of data
        serializer_class = Question_typeSerializer(queryset, many=True) #passing data to serializer to convert it to json
        return Response(serializer_class.data)
        
    elif request.method == 'POST':
        serializer = Question_typeSerializer(data=request.data) #getting json data 
        if serializer.is_valid():
            serializer.save()                                  # saving it to database
            return Response(serializer.data,status.HTTP_201_CREATED) #success response 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #failure response

# creating function for update get and delete for this required perticular id object
@api_view(['GET','PUT','DELETE'])
def question_typeUpdate(request,pk):
    try:
        questiontyp = question_type.objects.get(id=pk) #getting the obj of perticular id
    
        if request.method == 'GET':
            serializer=Question_typeSerializer(questiontyp) # passing query for the serializer
            return Response(serializer.data) #gives the json formate of the query
        elif request.method == 'PUT':
            serializer=Question_typeSerializer(questiontyp, data=request.data) #passing query and data to serializer to covrt json to dict
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data) # success response
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #failure response
        # elif request.method == 'DELETE':
        #     questiontyp.delete()
        #     return Response(status=status.HTTP_204_NO_CONTENT)
    except question_type.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# -------------------------------Question TopicList Api-----------------------------------------------------
@api_view(['GET','POST'])
def question_topicList(request):
    if request.method == 'GET':
        queryset = question_topic.objects.all()
        serializer_class = Question_topicSerializer(queryset, many=True)
        return Response(serializer_class.data)
    elif request.method == 'POST':
        serializer = Question_topicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def question_topicUpdate(request,pk):
    try:
        questiontyp = question_topic.objects.get(id=pk)
    
        if request.method == 'GET':
            serializer=Question_topicSerializer(questiontyp)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer=Question_topicSerializer(questiontyp, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # elif request.method == 'DELETE':
        #     questiontyp.delete()
        #     return Response(status=status.HTTP_204_NO_CONTENT)
    except question_topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# ------------------------Question Complexity Api-------------------------------------------------------
@api_view(['POST','GET'])
def question_complexList(request):
    if request.method == 'GET':
        queryset = question_complexity.objects.all()
        serializer_class = Question_complexSerializer(queryset, many=True)
        return Response(serializer_class.data)

    elif request.method == 'POST':
        serializer = Question_complexSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def question_complexUpdate(request,pk):
    try:
        questiontyp = question_complexity.objects.get(id=pk)
    
        if request.method == 'GET':
            serializer=Question_complexSerializer(questiontyp)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer=Question_complexSerializer(questiontyp, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # elif request.method == 'DELETE':
        #     questiontyp.delete()
        #     return Response(status=status.HTTP_204_NO_CONTENT)
    except question_complexity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

# -----------------------Adding Question Api-------------------------------------------------------
@api_view(['GET','POST'])
def add_questionList(request):
    if request.method == 'GET':
        queryset = app_question.objects.all()
        serializer = Add_questionSerializer(queryset,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # print "m in post"
        # questiontype_name = get_object_or_404(question_type,acronym=request.data.get('questiontype_name'))
        # questiontype_name = question_type.objects.get(acronym=request.data.get('questiontype_name'))
        # print questiontype_name
        # questioncomplexity_name = get_object_or_404(question_complexity,acronym=request.data.get('questioncomplexity_name'))
        # questiontopic_name = get_object_or_404(question_topic,name=request.data.get('questiontopic_name'))
        serializer = Add_questionSerializertwo(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save(questiontype_name=questiontype_name, questioncomplexity_name=questioncomplexity_name,questiontopic_name=questiontopic_name)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','PUT','DELETE'])
def add_questionUpdate(request,pk):

    try:
        addquestions = app_question.objects.get(id=pk)
    
        if request.method == 'GET':
            serializer=Add_questionSerializer(addquestions)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer=Add_questionSerializer(addquestions, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # elif request.method == 'DELETE':
        #     addquestions.delete()
        #     return Response(status=status.HTTP_204_NO_CONTENT)
    except question_complexity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

# ---------------------------------Getting question type---------------------------------
# @api_view(['GET','POST'])
# def getchoice_id(request):
#     if request.method == 'POST':


# -----------------------------------Adding choices------------------------------------------
# @api_view(['GET','POST'])
# def add_choices(request):
#     if request.method == 'GET':
#         queryset = question_choices.objects.all()
#         serializer = Choice_questionSerializer(queryset,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer_choice = Choice_questionSerializer(data=request.data)
#         if serializer_choice.is_valid() :
#             serializer_choice.save()
#             return Response(serializer_choice.data,status.HTTP_201_CREATED)
#         return Response(serializer_choice.errors, status=status.HTTP_400_BAD_REQUEST)