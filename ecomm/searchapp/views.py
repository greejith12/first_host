from shop.models import product
from django.db.models import Q
from django.shortcuts import render

def searchresult(request):
    Prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        Prod=product.objects.all().filter(Q(name__contains=query)  | Q(desc__contains=query))
    return render(request,'search.html',{'query':query,'Prod': Prod})
