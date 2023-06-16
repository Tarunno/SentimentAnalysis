from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]


handler404 = 'utils.handler404.error_404'
handler500 = 'utils.handler500.error_500'