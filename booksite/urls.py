
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from . import views
# from django.conf.urls import urls




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.homepage),
    path('book/', include('bookapp.urls')),
    path('chat/', include('base.urls'),name="chat"),
    path('news/', include('news_api.urls'),name="news"),
    path('music/', include('music.urls'),name="music"),
    # url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
