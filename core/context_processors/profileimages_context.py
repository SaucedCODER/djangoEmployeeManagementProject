from employees.models import UserProfile 

def profile_image(request):
    profile_image = None

    if request.user.is_authenticated:
        try:
            profile_image = request.user.userprofile.avatar.url
        except UserProfile.DoesNotExist:
            pass

    return {'zprofile_image': profile_image}