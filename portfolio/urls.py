from django.urls import path
from .views import portfolio, contac, download

app_name = 'portfolio'

urlpatterns = [
    path('portfolio/', portfolio, name='portfolio'),
    path('contac/', contac, name='contac'),
    path('download/', download, name='download'),
]
