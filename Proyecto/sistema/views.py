from django.shortcuts import render_to_response
from models import Membership

def latest_developer(request):
    developer_list = Membership
    return render_to_response('latest_developer.html', {'developer_list':developer_list})
