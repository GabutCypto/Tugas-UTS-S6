from django.urls import path, include

urlpatterns = [
    path('api/tokohp/', include('tokohp.urls')),
]
