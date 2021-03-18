from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import questionnaire
from .forms import QuestionnaireForm
from django_tables2 import SingleTableView
from .tables import ItemTable
from  django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import TemplateView, ListView
from .filters import QuestionnaireFilter

# なぜかエラー
# from django_filters.views import FilterView


# ログイン用
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.views import LoginView, LogoutView
# from django.views import generic
# from .forms import LoginForm



# Create your views here.
def index(request):
      return TemplateResponse(request, 'index.html')

def kimetsu1(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST,request.FILES)
      #   is_valid = form.is_valid()    
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()         
        
        return TemplateResponse(request, 'index.html',
                                {'form': form})
    else:            
        form = QuestionnaireForm()
    

    return TemplateResponse(request, 'kimetsu1.html',
                                {'form':form})

# def kimetsu2(request):
#         data=questionnaire.objects.order_by("id")
#         print(data)
        
#         return TemplateResponse(request, 'kimetsu2.html',
#                                 {'data':data})


# djangoのクラスベースビューしよう（引数はtables2の組込関数？）

class DetailView(SingleTableView):
    table_class = ItemTable
    # nameでの表記可能？
    template_name = 'kimetsu2.html'
    model = questionnaire
  
    def get_queryset(self):
        # data=questionnaire.objects.order_by("id")
        # print(data)
        return questionnaire.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        # print(self.request.GET)
        # print(self.get.queryset())
        context['filter'] = QuestionnaireFilter(self.request.GET, queryset = questionnaire.objects.all())
        return context



def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        print(user)
        # name = request.session.get['username']
        # request.session['username'] = name
        if user is not None:
            login(request, user)    
            return render(request, 'index.html', {'context':'loged in',
                                                'user':user
                                                })
        else:
            return render(request, 'login.html', {'context':'not loged in'})

    return render(request, 'login.html', {'context':'get method'})


def logout_view(request):
    logout(request)
    return redirect('login')

# class Mypage(LoginRequiredMixin, TemplateView):
#     template_name = 'templates/mypage.html'

def mypage(request):
    user = request.user
    return render(request, 'mypage.html', {'user':user})
        # user = authenticate(request, username = username, password = password)
        # print(user)
        # # context['staff_list'] = Staff.objects.filter(user=self.request.user).order_by('name')
        # # context['schedule_list'] = Schedule.objects.filter(staff__user=self.request.user, start__gte=timezone.now()).order_by('name')
        # return user

# class FilterListView(SingletableMixin, FilterView):
#       table_class = ItemTable
#       model = questionnaire
#       template_name = 'kimetsu2.html'
#       filterset_class = ItemFiltter


# class Top(generic.TemplateView):
#     template_name = 'register/top.html'


# class Login(LoginView):
#     """ログインページ"""
#     form_class = LoginForm
#     template_name = 'register/login.html'


# class Logout(LogoutView):
#     """ログアウトページ"""
#     template_name = 'register/top.html'