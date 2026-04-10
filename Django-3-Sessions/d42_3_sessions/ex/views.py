from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import MyCustomUser, ModelTip
from .forms import MyUserForm, TipForm
import time
import random
# Create your views here.

def home(request):

    saved_time = time.time()
    users = settings.ANYONYM_USERS
    if not request.session.get('random_user'):
        random_user = random.choice(users)
        request.session['random_user'] = random_user
        request.session['timestamp'] = saved_time
    else:
        current_time = time.time()
        time_saved = request.session.get('timestamp')
        if current_time - time_saved >= 42:
            random_user = random.choice(users)
            request.session['random_user'] = random_user
            request.session['timestamp'] = current_time
        if current_time - time_saved <= 42:
            pass
    if request.method == 'POST':

        form = TipForm(request.POST)
        if form.is_valid():
            tip = form.save(commit=False)
            tip.author = request.user
            tip.save()
            return redirect('/ex/')
        
    else:
        form = TipForm()
    data_tip = ModelTip.objects.all()
    return render(request, 'ex/display.html', {
        'tipform': form,
        'data_tip': data_tip,
    })

def Votes(request, tip_id):
    
    user = request.user
    tips = get_object_or_404(ModelTip, id=tip_id)
    upvotes_exists = tips.upvotes.filter(id=user.id).exists()
    downvotes_exists = tips.downvotes.filter(id=user.id).exists()
    # is_upvotes = False
    if not upvotes_exists and not downvotes_exists :

        tips.upvotes.add(user)
        # is_upvotes = True
    
    elif not downvotes_exists and not upvotes_exists:

        tips.downvotes.add(user)
        # is_upvotes = False
    elif upvotes_exists and not downvotes_exists:
        tips.upvotes.remove(user)
        tips.downvotes.add(user)
    elif not upvotes_exists and downvotes_exists:
        tips.upvotes.add(user)
        tips.downvotes.remove(user)
    return redirect("home")

def RemoveTip(request, tip_id):
    tips = ModelTip.objects.get(id=tip_id)
    tips.delete()
    return redirect("home")

class Registration(CreateView):
    
    model = MyCustomUser
    form_class = MyUserForm
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"
# There is 3 States:
# State 0: Neutral no upvote no downvote
# State 1: Upvote 
# State 2: Downvote
# Cases :
# Case-1: The user can not do both at once Upvote and Downvote
# Case-2-1: The user can upvote or downvote just once means he can not 
#   upvote or downvote the same tip in endless time
# Case2-2: If the user click on either upvote or downvote twice
#    the action must be canceled so we must return to the previous state
# Case3: If the user upvotes a tip they had previously downvotes
#   the downvotes is replaced by upvote and vice-versa. 
#
#
#
#
#
#
#
