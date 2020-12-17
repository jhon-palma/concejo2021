from django.urls import path
from . import views

app_name = 'appconcejo'

urlpatterns = [
    # post views
    path('', views.noticia_list, name='noticia_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.noticia_detail,name='noticia_detail'),

]
