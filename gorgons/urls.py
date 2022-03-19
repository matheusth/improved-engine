from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def my_view(_):
    return HttpResponse("Hello World!")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
]
