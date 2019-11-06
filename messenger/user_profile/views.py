from django.http import JsonResponse, HttpResponseNotAllowed


def profile(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_methods=['GET'], status=405)

    return JsonResponse({
                            "user": "user_1",
                            "first_name": "Jack",
                            "last_name": "Westner",
                            "date_of_birthday": 32234312,
                            "avatar": "image.png"
                        })
