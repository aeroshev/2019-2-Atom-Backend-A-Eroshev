from django.shortcuts import render, Http404, HttpResponseNotAllowed


def start(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_methods=['GET'], status=405)

    try:
        return render(request, 'index.html')
    except:
        raise Http404
