from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import catelog,product
from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.
def allprodcat(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug!=None:
        c_page=get_object_or_404(catelog,slug=c_slug)
        products_list=product.objects.all().filter(category=c_page,available=True)
    else:
        products_list=product.objects.all().filter(available=True)
    paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        Product=paginator.page(page)
    except (InvalidPage,EmptyPage):
        Product=paginator.page(paginator.num_pages)
    return render(request,'category.html',{'category':c_page,'Product':Product})

def prodet(request,c_slug,p_slug):
    try:
        Product=product.objects.get(category__slug=c_slug,slug=p_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'Product':Product})