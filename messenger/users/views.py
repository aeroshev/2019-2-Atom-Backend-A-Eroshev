from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, HttpResponseBadRequest
from .models import User
from .helper import to_json
from json import dumps


def get_profile(request, user_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_method=['GET'])

    return JsonResponse({
                            "first_name": "John",
                            "last_name": "Pitt",
                            "date_of_birthday": 223453,
                            "nickname": "JP22"
    })


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
            else:
                return JsonResponse({'response': 'no have matched users'})

    return HttpResponseBadRequest("Bad request")

