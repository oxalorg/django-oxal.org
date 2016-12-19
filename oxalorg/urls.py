"""oxalorg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views import generic
from . import settings

urlpatterns = [
    url(r'^wiki/', include('doxwiki.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', generic.TemplateView.as_view(template_name='oxalorg/index.html')),
    url(r'^about/$', generic.TemplateView.as_view(template_name='oxalorg/about.html')),
    url(r'^view2/', generic.TemplateView.as_view(template_name='oxalorg/view2.html')),
    url(r'^$', generic.TemplateView.as_view(template_name='oxalorg/view1.html')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
