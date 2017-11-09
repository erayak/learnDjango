from django.conf.urls import url
from FirstApplication import views

urlpatterns = [
    url(r'^$',views.AnasayfaSayfaGorunumu.as_view()),
]