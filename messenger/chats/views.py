from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .forms import ChatForm
from .models import Member


@require_http_methods(['GET'])
def chat_list(request):
    id_usr = request.GET.get('usr')
    if not id_usr.isdigit():
        return JsonResponse({'response': []}, status=400)

    consists_in_chats = Member.objects.filter(user=id_usr).select_related('chat')
    return JsonResponse({'response': [user.chat.to_json() for user in consists_in_chats]})


@require_http_methods(['POST'])
def create_chat(request):
    # POST-------------------------------
    id_usr = request.GET.get('usr')
    if not id_usr.isdigit():
        return JsonResponse({'response': []}, status=400)
    # POST-------------------------------

    form = ChatForm(request.GET, id_usr)
    if form.is_valid():
        chat = form.save()
        return JsonResponse({'response': chat.to_json()})
    return JsonResponse({'error': form.errors}, status=400)
