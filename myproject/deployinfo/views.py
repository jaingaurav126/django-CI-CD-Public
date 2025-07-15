from django.shortcuts import render
from datetime import datetime

def deploy_view(request):
    return render(request, 'deploy.html', {'year': datetime.now().year})
