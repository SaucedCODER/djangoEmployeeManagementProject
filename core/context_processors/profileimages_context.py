from employees.models import UserProfile 

def profile_image(request):
    profile_image = None

    if request.user.is_authenticated:
        try:
            user_profile = request.user.userprofile
            if user_profile.avatar and hasattr(user_profile.avatar, 'url'):
                profile_image = user_profile.avatar.url
        except UserProfile.DoesNotExist:
            pass

    return {'zprofile_image': profile_image}