from django.contrib import admin
from django.urls import path,include
from journal import urls as journal_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(journal_urls))
]
