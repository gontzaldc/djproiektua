from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.post_pop, name='blog_post_pop'),
    url(r'blog/register$', views.post_register, name='blog_register'),
    url(r'^post/new/$', views.post_new, name ='blog_post_new')
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
