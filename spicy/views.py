from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import questionnaire
from .forms import QuestionnaireForm
from django-tables2 import SingleTableView
from .tables import ItemTable

# Create your views here.
def index(request):
      return TemplateResponse(request, 'index.html')


def kimetsu1(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        is_valid = form.is_valid()    
        if form.is_valid():
            form.save()         
        data=questionnaire.objects.order_by("id")
        print(data)
        
        return TemplateResponse(request, 'index.html',
                                {'form': form,
                                'data':data})
    else:            
        form = QuestionnaireForm()
    

    return TemplateResponse(request, 'kimetsu1.html',
                                {'form':form})

def kimetsu2(request):
        data=questionnaire.objects.order_by("id")
        print(data)
        
        return TemplateResponse(request, 'kimetsu2.html',
                                {'data':data})


# djangoのクラスベースビューしよう（引数はtables2の組込関数？）
class DetailView(SingleTableView):
      table_class = ItemTable
      # nameでの表記可能？
      template_name = 'kimetsu2.html'

      def get_queryset(self):
            return Item.objects.all()


