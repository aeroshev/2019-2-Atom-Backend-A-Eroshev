from django.http import JsonResponse, HttpResponseNotAllowed


def get_message(request, chat_id, message_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_method=['GET'])

    return JsonResponse({
        "text": "Hello, world!",
        "time_send": 124332,
    })
