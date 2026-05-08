from django.urls import path
from cards import views

urlpatterns = [
    path('cards/', views.card_list, name='card_list'),
    path('cards/<int:card_id>/', views.get_card, name='get_card'),
]