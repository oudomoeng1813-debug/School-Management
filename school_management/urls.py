from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from app_school import views

urlpatterns = [
    path('', views.home, name='home'),  # 👈 This makes / the home page
    path('admin/', admin.site.urls),
    path('students/', include('app_school.urls')),
]

