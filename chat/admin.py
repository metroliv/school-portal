from django.contrib import admin
from .models import Group, GroupMessage
from .models import Message
from .models import VideoCall, VideoCallParticipant
# Register your models here.
 
class GroupMessageInline(admin.TabularInline):
    model = GroupMessage
    extra = 1  # Number of empty forms to display

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('members',)
    inlines = [GroupMessageInline]

class GroupMessageAdmin(admin.ModelAdmin):
    list_display = ('group', 'sender', 'content', 'timestamp')
    list_filter = ('group', 'sender', 'timestamp')
    search_fields = ('content',)

admin.site.register(Group, GroupAdmin)
admin.site.register(GroupMessage, GroupMessageAdmin)
admin.site.register(Message)

class VideoCallAdmin(admin.ModelAdmin):
    list_display = ('call_id', 'created_by', 'start_time', 'active')
    search_fields = ('call_id', 'created_by__username')

class VideoCallParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'call', 'is_admin', 'is_muted', 'is_removed')
    search_fields = ('user__username', 'call__call_id')
    list_filter = ('is_admin', 'is_muted', 'is_removed')

admin.site.register(VideoCall, VideoCallAdmin)
admin.site.register(VideoCallParticipant, VideoCallParticipantAdmin)