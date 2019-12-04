from django.http import JsonResponse
from .forms import AddMessageForm, ReadMessageForm
from .helper import message_list


# ---POST---
def add_message(request):
    if request.method == 'POST':

        # validate_get_require-------------------------------------------
        id_usr = request.GET.get('usr', -1)

        try:
            id_usr = int(id_usr)
        except ValueError:
            return JsonResponse({'response': 'incorrect POST request'}, status=400)

        if id_usr <= 0:
            return JsonResponse({'response': 'incorrect POST request'}, status=400)
        # --------------------------------------------------------------

        form = AddMessageForm(request.POST, request.FILES, id_usr)

        if form.is_valid():
            message = form.save()
            if message:
                return JsonResponse({'response': 'ok'})

            return JsonResponse({'response': 'Failed'}, status=400)

        return JsonResponse({'error': form.errors}, status=400)

    return JsonResponse({'response': 'permitted method POST'}, status=403)


# ---POST---
def read_message(request):
    if request.method == 'POST':

        # validate_get_require-------------------------------------------
        id_usr = request.GET.get('usr', -1)

        try:
            id_usr = int(id_usr)
        except ValueError:
            return JsonResponse({'response': 'incorrect POST request'}, status=400)

        if id_usr <= 0:
            return JsonResponse({'response': 'incorrect POST request'}, status=400)
        # --------------------------------------------------------------

        form = ReadMessageForm(request.POST, id_usr)

        if form.is_valid():
            status = form.save()
            return JsonResponse({'response': 'OK' if status else 'Failed'})

        return JsonResponse({'response': form.errors}, status=400)

    return JsonResponse({'response': 'permitted method POST'}, status=403)


# ---GET---
def get_list_messages(request):
    if request.method == 'GET':

        # validate_get_require-------------------------------------------
        id_usr = request.GET.get('usr', -1)
        id_chat = request.GET.get('chat', -1)

        try:
            id_usr = int(id_usr)
            id_chat = int(id_chat)
        except ValueError:
            return JsonResponse({'response': 'incorrect GET request'}, status=400)

        if id_usr <= 0 or id_chat <= 0:
            return JsonResponse({'response': 'incorrect GET request'}, status=400)
        # --------------------------------------------------------------
        messages_list = message_list(id_chat, id_usr)

        if messages_list:
            return JsonResponse({'response': messages_list})

        return JsonResponse({'response': 'empty'})

    return JsonResponse({'response': 'permitted method GET'}, status=403)
