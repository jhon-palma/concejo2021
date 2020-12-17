from django.shortcuts import render, get_object_or_404
from .models import Noticias

def noticia_list(request):
    noticias = Noticias.published.all()
    return render(request,'concejo/noticias/list.html',{'noticias': noticias})

def noticia_detail(request, year, month, day, post):
    post = get_object_or_404(Noticias, slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day)
    return render(request,'concejo/noticias/detail.html',{'noticia': post})
