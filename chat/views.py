from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message, Group, GroupMessage
from .forms import GroupForm, GroupMessageForm
from django.urls import reverse
from .models import VideoCall
from .models import  VideoCallParticipant
import uuid

@login_required
def chat_room(request, username):
    recipient = get_object_or_404(User, username=username)
    messages = (Message.objects.filter(sender=request.user, receiver=recipient) |
                Message.objects.filter(sender=recipient, receiver=request.user)).order_by('timestamp')

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(sender=request.user, receiver=recipient, content=content)
        return redirect('chat_room', username=username)

    return render(request, 'chat/chat_room.html', {'recipient': recipient, 'messages': messages})

@login_required
def chat_list(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat/chat_list.html', {'users': users})

@login_required
def group_list(request):
    groups = Group.objects.filter(members=request.user)
    return render(request, 'chat/group_list.html', {'groups': groups})

@login_required
def group_chat(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.user not in group.members.all():
        return redirect('group_list')

    messages = group.groupmessage_set.order_by('timestamp')  # Adjusted to use related name
    if request.method == 'POST':
        form = GroupMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.group = group
            message.save()
            return redirect('group_chat', group_id=group.id)
    else:
        form = GroupMessageForm()

    return render(request, 'chat/group_chat.html', {'group': group, 'messages': messages, 'form': form})

@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            group.members.add(request.user)
            group.save()
            return redirect('group_chat', group_id=group.id)
    else:
        form = GroupForm()

    return render(request, 'chat/create_group.html', {'form': form})

@login_required
def start_video_call(request):
    call_id = str(uuid.uuid4())
    call = VideoCall.objects.create(call_id=call_id, created_by=request.user)
    VideoCallParticipant.objects.create(user=request.user, call=call, is_admin=True)
    return redirect(reverse('join_video_call', args=[call_id]))

@login_required
def join_video_call(request, call_id):
    call = get_object_or_404(VideoCall, call_id=call_id, active=True)
    participant, created = VideoCallParticipant.objects.get_or_create(user=request.user, call=call)
    if participant.is_removed:
        return render(request, 'call_removed.html')
    context = {
        'call': call,
        'is_admin': participant.is_admin,
        'participants': call.participants.all()
    }
    return render(request, 'join_call.html', context)

