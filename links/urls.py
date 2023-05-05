from django.urls import path
from .views import link_list_view, create_link, update_link



urlpatterns = [
    path('', link_list_view),
    path('create/', create_link),
    path('<int:id>/update/', update_link),
]
