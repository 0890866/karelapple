from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static

from apple.views import (recipes, add_apple, add_recipe, index)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^apple/', include('apple.urls')),
    url(r'^recipes/', recipes, name="recipes"),
    url(r'^accounts/login/$', views.login, name="login"),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/index'}),
    url(r'^add_apple/', add_apple.as_view(success_url="/apple"), name='add_apple'),
    url(r'^add_recipe/', add_recipe.as_view(success_url="/recipes"), name="add_recipe"),
    url(r'^index/', index, name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)