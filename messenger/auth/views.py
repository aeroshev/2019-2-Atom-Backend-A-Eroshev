from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    # return render(request, 'registration/home.html')
    return redirect('https://aeroshev.github.io/2019-2-Atom-Frontend-A-Eroshev/')
