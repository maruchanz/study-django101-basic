from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import questionnaire
from .forms import QuestionnaireForm

# Create your views here.
def index(request):
      return TemplateResponse(request, 'index.html')


def kimetsu1(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            form.save()         
        data=questionnaire.objects.order_by("id").last()
        x= data.gender_data
       
        return TemplateResponse(request, 'index.html',
                                {'form': form,
                                'data':data})
    else:            
        form = QuestionnaireForm()
    

    return TemplateResponse(request, 'kimetsu1.html',
                                {'form':form})

def kimetsu2(request):
      return TemplateResponse(request, 'kimetsu2.html')
