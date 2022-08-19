
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),


    # API URL 

    path('api/user/', include('User.api.urls'))
]
