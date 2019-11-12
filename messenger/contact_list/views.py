from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest


def get_list(request):
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