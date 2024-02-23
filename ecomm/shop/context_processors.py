from . models import catelog
def menu_links(request):
    links=catelog.objects.all()
    return dict(links=links)