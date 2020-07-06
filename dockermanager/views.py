from django.http import HttpResponse
from docker import APIClient
import docker
import json

def index(request):
    return HttpResponse("Hello, world!")

def dockerversion(request):
    client = docker.APIClient(base_url='unix://var/run/docker.sock')
    client_env = docker.from_env()
    tagname = 'dockerphpnginx'
    version = 'latest'
    version = client.version()
    print(version)
    return HttpResponse(json.dumps(version))

