from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import MyCustomUser, ModelTip
from .forms import MyUserForm, TipForm
import time
import random
# Create your views here.
def home(request):

    user = request.user
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
    users = MyCustomUser.objects.all()
        
    print(f"Fetch some data: {data_tip.count()} for User: {request.user}")
    return render(request, 'ex/display.html', {
        'tipform': form,
        'data_tip': data_tip,
        'user': user,
        'users': users,
    })

# @login_required(login_url="/account/login/")
# def get_users_reputation(request, tip_id):
#     user = request.user
#     tips = get_object_or_404(ModelTip, id=tip_id)
#     upvotes_exist = tips.upvotes.filter(id=user.id).exists()
#     downtes_exist = tips.downvotes.filter(id=user.id).exists()
#     if upvotes_exist or downtes_exist:
#         total_user_reputation = (tips.get_upvote_count() * 5) - (tips.get_downvote_count() * 2)

#         MyCustomUser.objects.create(reputation=total_user_reputation)



@login_required(login_url="/account/login/")
def Upvotes(request, tip_id):
    if request.method == "POST":
        user = request.user
        tips = get_object_or_404(ModelTip, id=tip_id)

        if not tips.upvotes.filter(id=user.id).exists():
            tips.upvotes.add(user)
            if tips.downvotes.filter(id=user.id).exists():
                tips.downvotes.remove(user)
        else:
            tips.upvotes.remove(user)
   
    return redirect("home")

@login_required(login_url="/account/login/")
def Downvotes(request, tip_id):
    user = request.user
    tips = get_object_or_404(ModelTip, id=tip_id)
    if request.method == "POST":
        if user.get_total_reputations >= 15 or tips.author == user or user.has_perm('ex.can_downvote'):
            if not tips.downvotes.filter(id=user.id).exists():
                tips.downvotes.add(user)
                if tips.upvotes.filter(id=user.id).exists():
                    tips.upvotes.remove(user)
            else:
                tips.downvotes.remove(user)
        else:
            messages.error(request, "You can downvote only and only your own tip")
    
    return redirect("home")
# Vivo@_#1234
@login_required
def RemoveTip(request, tip_id):
    user = request.user
    tips = get_object_or_404(ModelTip, id=tip_id)
    if request.method == 'POST':
        if user.get_total_reputations >= 30 or tips.author == request.user or request.user.has_perm('ex.delete_modeltip'):
            tips.delete()
            messages.success(request, f"The tips {tips.content} of author {tips.author} delete successfully.")
            return redirect("home")
        else:
            messages.error(request, "You don't have permissions to delete this tip , ask your ADMIN if you need such action")
            return redirect("home")
    return redirect("home")

class Registration(CreateView):
    model = MyCustomUser
    form_class = MyUserForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")
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
