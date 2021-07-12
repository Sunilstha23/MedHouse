from django.shortcuts import render
from django.http import HttpResponse
import pickle
from django.http import JsonResponse
from .chatapp import ChatApp as ca

# Create your views here.


def chatbotResponse(request):
    if request.method == 'POST':
        the_question = request.form['question']
        response = ca.chatbot_response(the_question)
        return JsonResponse({"response": response })
