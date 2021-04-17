"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from myapp.views import ShowHelloWorld
from srs_api.views import user_api, poll_api, question_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/signup', user_api.sign_up),
    path('api/user/login', user_api.log_in),
    path('api/poll', poll_api.poll_main),
    path('api/poll/<uuid:pk>/qa', poll_api.qa_main),
    path('api/question/<uuid:pk>/reply', question_api.reply),
    path('^', ShowHelloWorld.as_view()),
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
