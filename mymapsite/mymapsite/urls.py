from django.contrib import admin
from django.urls import include, path #include追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gmap/', include('gmap.urls')), #追加
]
