from django.contrib import admin

from study_buddy.base.models import Room, Topic, Message, User


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class RoomAdmin(admin.ModelAdmin):
    pass
