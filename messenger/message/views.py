from django.http import JsonResponse
from  django.views.decorators.http import require_http_methods
from .forms import AddMessageForm, ReadMessageForm
from .models import Message, Attachment


@require_http_methods(['POST'])
def add_message(request):
    # POST-------------------------------
    id_usr = request.GET.get('usr')
    if not id_usr.isdigit():
        return JsonResponse({'response': 'incorrect POST request'}, status=400)
    # POST-------------------------------

    form = AddMessageForm(request.POST, request.FILES, id_usr)

    if form.is_valid():
        message = form.save()
        if message:
            return JsonResponse({'response': 'ok'})
        return JsonResponse({'response': 'Failed'}, status=400)
    return JsonResponse({'error': form.errors}, status=400)


@require_http_methods(['POST'])
def read_message(request):
    # POST-------------------------------
    id_usr = request.GET.get('usr')
    if not id_usr.isdigit():
        return JsonResponse({'response': 'incorrect POST request'}, status=400)
    # POST-------------------------------

    form = ReadMessageForm(request.POST, id_usr)

    if form.is_valid():
        status = form.save()
        return JsonResponse({'response': 'OK' if status else 'Failed'})

    return JsonResponse({'response': form.errors}, status=400)


@require_http_methods(['GET'])
def get_list_messages(request):
    id_usr = request.GET.get('usr')
    id_chat = request.GET.get('chat')
    if not id_usr.isdigit() or not id_chat.isdigit():
        return JsonResponse({'response': []}, status=400)

    message_list = Message.objects.filter(chat=id_chat, user=id_usr)
    attachment_list = Attachment.objects.filter(chat=id_chat, user=id_usr)
    return JsonResponse({'response': [[message.to_json(), attachment.to_json()]
                                      for message, attachment in zip(message_list, attachment_list)]})


