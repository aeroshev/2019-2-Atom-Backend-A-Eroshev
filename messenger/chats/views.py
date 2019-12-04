from django.http import JsonResponse
from .forms import ChatForm
from .helper import to_json
from .models import Member


def chat_list(request):
    if request.method == 'GET':

        # validate_get_require-------------------------------------------
        id_usr = request.GET.get('usr', -1)

        try:
            id_usr = int(id_usr)
        except ValueError:
            return JsonResponse({'response': 'incorrect GET request'}, status=400)

        if id_usr <= 0:
            return JsonResponse({'response': 'incorrect GET request'}, status=400)
        # --------------------------------------------------------------

        consists_of_chats = list(Member.objects.filter(user=id_usr))

        chats = []
        for member_in_chat in consists_of_chats:
            chats.append(to_json(member_in_chat.chat))

        return JsonResponse({'response': chats})

    return JsonResponse({'response': 'permitted method GET'}, stattus=403)


def create_chat(request):
    if request.method == 'POST':

        # validate_get_require-------------------------------------------?
        id_usr = request.GET.get('usr', -1)

        try:
            id_usr = int(id_usr)
        except ValueError:
            return JsonResponse({'response': 'incorrect POST request'}, status=400)

        if id_usr <= 0:
            return JsonResponse({'response': 'incorrect POST request'}, status=400)
        # --------------------------------------------------------------

        form = ChatForm(request.GET, id_usr)

        if form.is_valid():
            chat = form.save()
            return JsonResponse({'response': to_json(chat)})

        return JsonResponse({'error': form.errors}, status=400)

    return JsonResponse({'response': 'permitted method POST'}, status=403)
