from django.http import JsonResponse
from .models import User
from .helper import to_json


def get_profile(request, user_id):
    if request.method == 'GET':

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'response': 'Not found user with this id'}, status=400)

        return JsonResponse(to_json(user))

    return JsonResponse({'response': 'permitted method GET'}, status=403)


def create_profile(request):
    if request.method == 'GET':
        return JsonResponse({'response': 'ok'})

    return JsonResponse({'response': 'permitted method GET'}, status=403)


def search(request):
    if request.method == 'GET':

        nick = request.GET.get('nick')

        if nick:
            users = list(User.objects.filter(username__icontains=nick))

            if users:
                matched_users = []

                for user in users:
                    matched_users.append(to_json(user))

                return JsonResponse({'response': matched_users})

            return JsonResponse({'response': 'no have matched users'})

        return JsonResponse({'response': 'incorrect nick'}, status=400)

    return JsonResponse({'response': 'permitted method GET'}, status=403)

