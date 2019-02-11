"""website URL Configuration

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

from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path
from django.conf import settings
# from rest_framework.documentation import include_docs_urls
# from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title='Sales API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sms.urls')),  

    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout',
         kwargs={'next_page': settings.LOGOUT_REDIRECT_URL}),
#     path('sales/api/', include('sales.api.urls', namespace='sales-api')),
    
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('swagger-docs/', schema_view),
# path('docs/', include_docs_urls(title='Sales API')),

]
