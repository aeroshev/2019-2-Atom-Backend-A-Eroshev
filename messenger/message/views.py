from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import AddMessageForm, ReadMessageForm
from .models import Message, Attachment


@csrf_exempt
@login_required
@require_http_methods(['POST'])
def add_message(request):
    form = AddMessageForm(request.user, request.POST, request.FILES)
    if form.is_valid():
        message = form.save()
        return JsonResponse({'response': [message[0].to_json(), message[1].to_json()]})
    return JsonResponse({'error': form.errors}, status=400)


@csrf_exempt
@login_required
@require_http_methods(['POST'])
def read_message(request):
    form = ReadMessageForm(request.user, request.POST)
    if form.is_valid():
        reader = form.save()
        return JsonResponse({'response': reader.to_json()})
    return JsonResponse({'response': form.errors}, status=400)


@login_required
@require_http_methods(['GET'])
def get_list_messages(request):
    id_chat = request.GET.get('chat')
    if not id_chat.isdigit():
        return JsonResponse({'response': []}, status=400)

    message_list = Message.objects.filter(chat=id_chat, user=request.user.id)
    attachment_list = Attachment.objects.filter(chat=id_chat, user=request.user.id)
    return JsonResponse({'response': [[message.to_json(), attachment.to_json()]
                                      for message, attachment in zip(message_list, attachment_list)]})


