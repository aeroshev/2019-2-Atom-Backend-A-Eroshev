from django.http import JsonResponse, HttpResponseNotAllowed


def chat_list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_methods=['GET'])

    return JsonResponse({
                            "owner": "JP22",
                            "quantity_chats": 10,
                            "contains": {

                            }
                        })

