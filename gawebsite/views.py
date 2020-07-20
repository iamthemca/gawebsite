
from django.http import HttpResponse
from django.shortcuts import render,redirect
def home_page(request):
    #return HttpResponse('<h1>Hello World</h1>')
    #context={'title':'Growth Art'}
    context={'title':'Growth Art'}
    # if request.user.is_authenticated:
    #     context={'title':'Growth Art', 'my_list':[1,2,3,4,5]}
    return render(request, 'index.html',context )