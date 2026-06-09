from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django import views
from django.http import JsonResponse
from django.shortcuts import render, reverse

# Create your views here.

class account_view(views.View):
    
    template_name = 'account/account.html'
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})
 
    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')

        if action == 'login':

            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return JsonResponse({
                    'success': True,
                    'username': user.username
                    }, status=200)
            else:
                return JsonResponse({
                    'success': False,
                    'errors': form.errors.get_json_data()
                }, status=400)

        if action == 'logout':
            if request.user.is_authenticated:
                logout(request)
                return JsonResponse({
                    'success': True,
                }, status=200)
            else:
                return JsonResponse({
                    'success': False,
                    'error': 'User is not logged in.'
                }, status=400)
        return JsonResponse({'success': False, 'error': 'Invalid action!'}, status=400)