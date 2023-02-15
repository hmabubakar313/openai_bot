from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
import openai
import requests
from django.http import HttpResponse
from .models import Chat
from django.utils import timezone

# set openai api key
openai.api_key = "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"
# Create your views here.
#get all chat messages from database
# def get_chat(request):
#     msg = Chat.objects.all().values()
#     print(msg)
#     msg_id = msg.values('id')
#     return HttpResponse(msg_id)

@api_view(['GET', 'POST'])
def chat(request):
    # first time prompt is set to Hi
    
    if request.method == 'GET':
        
        prompt = request.GET.get('input')
        print("prompt: ", prompt)
        response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=150)
        
        msg = Chat.objects.all().values()
        # print("message: ", msg)
        Chat.objects.create(msg=prompt,msg_type=0, date_time=timezone.now())
        Chat.objects.create(msg=response.choices[0].text,msg_type=1, date_time=timezone.now())
        
        
    
        
    return render(request, 'bot.html', {'response': response.choices[0].text, 'msg': msg})
    
  

def get_prompt(request):
    return  render(request, 'bot.html')

    



