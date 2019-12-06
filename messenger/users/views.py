from django.http import JsonResponse
from  django.views.decorators.http import require_http_methods
from .models import User


@require_http_methods(['GET'])
def get_profile(request, user_id):
    user = User.objects.filter(id=user_id)
    return JsonResponse(user.to_json())


@require_http_methods(['GET'])
def create_profile(request):
    return JsonResponse({'response': 'ok'})


@require_http_methods(['GET'])
def search(request):
    nick = request.GET.get('nick')
    if nick is None:
        return JsonResponse({'response': []}, status=400)

    users = User.objects.filter(username__icontains=nick)
    return JsonResponse({'response': [user.to_json() for user in users]})

