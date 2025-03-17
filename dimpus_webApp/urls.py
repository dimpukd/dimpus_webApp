"""
URL configuration for dimpus_webApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from MainPage import views

urlpatterns = [
    path ('', include('MainPage.urls')),
    path('admin/', admin.site.urls),
    path('order/<str:type>/<int:id>/', include('order.urls')),
    path('accounts/', include('accounts.urls')),
    path("contact/submit/", views.contact_submit, name="contact_submit"),
    path("submit_order", views.submit_order, name='submit_order'),
]


urlpatterns = urlpatterns +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)