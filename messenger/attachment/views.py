from django.http import JsonResponse, HttpResponseNotAllowed


def get_attach(request, chat_id, message_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_method=['GET'])

    return JsonResponse({
        "type": "image",
        "source": "http://myChat/user/22/storage/myimage.jpg",
        "owner": "JP22"
    })
