from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from dataset.models import Dataset
from django.contrib.auth.decorators import login_required




@login_required(redirect_field_name='next')
def index(request):
	if request.user.is_authenticated:
		return render(request, 'chat/index.html', {})



@login_required(redirect_field_name='next')
def room(request, room_name):
	get_object_or_404(Dataset, title=room_name)
	return render(request, 'chat/room.html', {
		'room_name': room_name,
		'username': request.user.username
	})
