from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from .forms import AddMessageForm, ReadMessageForm
from .helper import message_list
from json import dumps


# ---POST---
def add_message(request):
    if request.method == 'POST':

        # validate_get_require-------------------------------------------
        id_usr = request.GET.get('usr', -1)

        try:
            id_usr = int(id_usr)
        except ValueError:
            return HttpResponseBadRequest("Bad request")

        if id_usr <= 0:
            return HttpResponseBadRequest("Bad request")
        # --------------------------------------------------------------

        form = AddMessageForm(request.POST, request.FILES, id_usr)

        if form.is_valid():
            message = form.save()
            if message:
                return JsonResponse(dumps({'response': 'ok'}))

            return JsonResponse(dumps({'response': 'Failed'}), status=400)

        return JsonResponse(dumps({'error': form.errors}), status=400)

    return HttpResponseNotAllowed(permitted_method=['POST'])


# ---POST---
def read_message(request):
    if request.method == 'POST':

        # validate_get_require-------------------------------------------
        id_usr = request.GET.get('usr', -1)

        try:
            id_usr = int(id_usr)
        except ValueError:
            return HttpResponseBadRequest("Bad request")

        if id_usr <= 0:
            return HttpResponseBadRequest("Bad request")
        # --------------------------------------------------------------

        form = ReadMessageForm(request.POST, id_usr)

        if form.is_valid():
            status = form.save()
            return JsonResponse(dumps({'response': 'OK' if status else 'Failed'}))

        return JsonResponse(dumps({'response': form.errors}), status=400)

    return HttpResponseNotAllowed(permitted_method=['POST'])


def get_list_messages(request):
    if request.method == 'GET':

        # validate_get_require-------------------------------------------
        id_usr = request.GET.get('usr', -1)
        id_chat = request.GET.get('chat', -1)

        try:
            id_usr = int(id_usr)
            id_chat = int(id_chat)
        except ValueError:
            return HttpResponseBadRequest("Bad request")

        if id_usr <= 0 or id_chat <= 0:
            return HttpResponseBadRequest("Bad request")
        # --------------------------------------------------------------
        messages_list = message_list(id_chat, id_usr)

        if messages_list:
            return JsonResponse(dumps({'response': messages_list}))

        return JsonResponse(dumps({'response': 'empty'}))

    return HttpResponseNotAllowed(permitted_method=['GET'])
