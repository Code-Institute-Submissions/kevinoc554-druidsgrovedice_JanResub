from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def profile(request):
    """
    A view to return the user's profile page
    """
    userprofile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'
    context = {
        'profile': userprofile,
    }

    return render(request, template, context)
