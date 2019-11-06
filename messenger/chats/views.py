from django.http import JsonResponse, HttpResponseNotAllowed


def chat_list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_methods=['GET'], status=405)

    return JsonResponse({
                            "owner": "user_1",
                            "chat_id": 1,
                            "chat_name": "some",
                            "last_message": "Hello",
                            "time_last_message": 4242434,
                            "avatar": "avatar.png",
                            "status": "read"
                        })

