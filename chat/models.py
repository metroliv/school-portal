from django.db import models
from django.contrib.auth.models import User
from  datetime import datetime
# Import model from the other app

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __QuerySet__(self):
        return f"{self.sender} to {self.receiver}: {self.content[:20]}"

class Group(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='chat_groups')

    def __QuerySet__(self):
        return self.name



class GroupMessage(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

class VideoCall(models.Model):
    call_id = models.CharField(max_length=255, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_calls')
    start_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __QuerySet__(self):
        return f"Call {self.call_id} by {self.created_by.username}"

class VideoCallParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    call = models.ForeignKey(VideoCall, on_delete=models.CASCADE, related_name='participants')
    is_admin = models.BooleanField(default=False)
    is_muted = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)

    def __QuerySet__(self):
        return f"{self.user.username} in call {self.call.call_id}"