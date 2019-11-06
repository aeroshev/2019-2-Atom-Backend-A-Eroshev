from django.http import JsonResponse, HttpResponseNotAllowed


def contact_list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_methods=['GET'], status=405)

    return JsonResponse({
                            "user": "user_1",
                            "key": "dialogID",
                            "contact_list": ["user_2", "user_3"]
                        })
