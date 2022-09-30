from django.urls import path

from study_buddy.base.views import login_page, home, room, create_room, update_room, delete_room, logout_view, \
    register_user, delete_message, user_profile, update_user, topics_page, activities_page

urlpatterns = (
    path('login/', login_page, name="login"),
    path('register/', register_user, name="register"),
    path('logout/', logout_view, name="logout"),

    path("", home, name="home"),
    path("room/<str:pk>/", room, name="room"),
    path('profile/<str:pk>/', user_profile, name='user-profile'),

    path("create_room/", create_room, name="create-room"),
    path("update_room/<str:pk>/", update_room, name="update-room"),
    path("delete_room/<str:pk>/", delete_room, name="delete-room"),
    path("delete_message/<str:pk>/", delete_message, name="delete-message"),

    path("update_user/", update_user, name="update-user"),
    path("topics/", topics_page, name="topics_page"),
    path("activities/", activities_page, name="activities_page"),
)
