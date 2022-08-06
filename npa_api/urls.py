from . import views
from django.urls import path


app_name = 'npa_api'

urlpatterns = [
    # path('markets/', views.market_list, name='markets'),
    path('players/', views.player_list, name='players'),
    path('products/', views.product_list, name='products'),
]