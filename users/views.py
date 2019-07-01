"""Users views."""

from django.contrib.auth import authenticate, login
from django.shortcuts import render


# Create your views here.
def login_view(request):
	"""Login view."""
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
	return render(request, 'users/login.html')