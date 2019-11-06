from django.http import JsonResponse, HttpResponseNotAllowed


def chat_page(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_methods=['GET'], status=405)

    return JsonResponse({
                            "chat_id": 1,
                            "message_id": 1,
                            "owner": "user_1",
                            "message": "Something",
                            "time": 213412414,
                            "status": "send"
                        })


