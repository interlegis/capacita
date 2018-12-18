from capacitaApp.models import Profile

def include_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Exception as e:
        profile = []
    return {'profile': profile}
