"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path

from home import views

urlpatterns = [
    # register index view
    path('', views.IndexView.as_view(), name='index'),
    # register contact view
    path('contact/', views.ContactView.as_view(),
         name='contact'),
    # register about view
    path('about/', views.AboutView.as_view(), name='about'),
    # register services view
    path('services/', views.ServicesView.as_view(),
         name='services'),
    # register doctors view
    path('doctors/', views.DoctorView.as_view(),
         name='doctors'),
    # register blog view
    path('blog/', views.BlogView.as_view(), name='blog'),
    # register blog single view
    path('blog-single/', views.BlogSingleView.as_view(),
         name='blog-single'),
]

handler404 = 'home.views.error_404_view'
handler500 = 'home.views.error_500_view'
