from django.urls import path
from . import views

app_name = 'portfolio_balance'
urlpatterns = [
    ### Baseline path for initial request
    path('', views.index, name='index'),
    ### notice the change when adding the next
    path('<int:question_id>/', # This sets up index from previous item
         views.detail, # This adds the detail function as a subfolder
         name = 'detail'),
    path('<int:question_id>/results/', views.results, name = 'results'),
    path('<int:question_id>/vote/', views.vote, name = 'vote')
]