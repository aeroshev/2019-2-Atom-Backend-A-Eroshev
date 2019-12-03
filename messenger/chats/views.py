from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from .forms import ChatForm
from .helper import to_json
from .models import Member
from json import dumps


def chat_list(request):
    if request.method == 'GET':

        # validate_get_require-------------------------------------------
        id_usr = request.GET.get('usr', -1)

        try:
            id_usr = int(id_usr)
        except ValueError:
            return HttpResponseBadRequest("Bad request")

        if id_usr <= 0:
            return HttpResponseBadRequest("Bad request")
        # --------------------------------------------------------------

        consists_of_chats = Member.objects.filter(user=id_usr)

        chats = []
        for member_in_chat in consists_of_chats:
            chats.append(to_json(member_in_chat.chat, id_usr))

        return JsonResponse(dumps({'response': chats}))

    return HttpResponseNotAllowed(permitted_method=['GET'])


def create_chat(request):
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

        form = ChatForm(request.GET, id_usr)

        if form.is_valid():
            chat = form.save()
            return JsonResponse(dumps({'response': to_json(chat, id_usr)}))

        return JsonResponse(dumps({'error': form.errors}), status=400)

    return HttpResponseNotAllowed(permitted_method=['POST'])
