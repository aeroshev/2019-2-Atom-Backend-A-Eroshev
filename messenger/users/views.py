from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse


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
