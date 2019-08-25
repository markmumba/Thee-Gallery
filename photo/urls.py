from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.Location,name ='location' ),
    url(r'^australia/'views.australia,name ='australia'),
    url(r'^hongkong/'views.hongkong,name = 'honkong'),
    url(r'^africa/' views.africa, name = 'africa'),
    url(r'^search/',views.search_results,name = 'search_results')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
