from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, HttpResponseBadRequest


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


def get_contact(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_method=['GET'])

    id_usr = request.GET.get('usr', -1)

    try:
        id_usr = int(id_usr)
    except ValueError:
        return HttpResponseBadRequest("Bad request")

    if id_usr <= 0:
        return HttpResponseBadRequest("Bad request")

    return JsonResponse({
            "usr_list": ["1", "45", "12"]
    })
