from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, HttpResponseBadRequest
from .models import User
from .helper import to_json
from json import dumps


def get_profile(request, user_id):
    if request.method == 'GET':

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse(dumps({'response': 'Failed'}), status=400, safe=False)

        return JsonResponse(to_json(user), safe=False)

    return HttpResponseNotAllowed(permitted_method=['GET'])


def create_profile(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_method=['GET'])

    return HttpResponse("Login new user")


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

            return JsonResponse({'response': 'no have matched users'}, status=400)

    return HttpResponseBadRequest("Bad request")

