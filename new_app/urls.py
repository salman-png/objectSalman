from django.contrib import admin
from django.urls import path
from new_app import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.intro,name='home'),
    # path('login/',views.signin),
    path('home/', views.home,name='home'),
    # path('logout/',views.signout),
    path('predict',views.predict),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)