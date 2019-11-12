from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest


def get_message(request, message_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_method=['GET'])

    return JsonResponse({
        "text": "Hello, world!",
        "time_send": 124332,
    })


def get_attach(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_method=['GET'])

    id_msg = request.GET.get('msg', -1)

    try:
        id_msg = int(id_msg)
    except ValueError:
        return HttpResponseBadRequest("Bad request")

    if id_msg <= 0:
        return HttpResponseBadRequest("Bad request")

    return JsonResponse({
        "type": "image",
        "source": "http://myChat/user/22/storage/myimage.jpg",
        "owner": "JP22",
        "id_msg": id_msg
    })
