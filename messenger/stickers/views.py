from django.http import JsonResponse, HttpResponseNotAllowed


def get_sticker(request, chat_id, sticker_id):
    if request.method != "GET":
        return HttpResponseNotAllowed(permitted_method=['GET'])

    return JsonResponse({
        "name_sticker": "funny",
        "sticker_package": "standard",
        "emoji": "funny",
        "autor": "JP22"
    })
