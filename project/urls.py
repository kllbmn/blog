from django.urls import path
from project import views
from project.views import *

app_name = 'project'


urlpatterns = [
    path('', main, name='main'),
    path('project/portfolio_details', portfolio_details, name='portfolio_details'),
    path('project/inner_page', inner_page, name='inner_page'),
]