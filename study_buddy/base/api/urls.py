from django.urls import path

from study_buddy.base.api.views import get_routs, get_rooms, get_room

urlpatterns = [
    path('', get_routs),
    path('rooms/', get_rooms),
    path('rooms/<str:pk>', get_room),
]