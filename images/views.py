from django.http import HttpResponse
from docker import APIClient
import docker
import json

def index(request):
    return HttpResponse("Hello, world. You're at the containers index.")

def list(request):
    client = docker.APIClient(base_url='unix://var/run/docker.sock')
    client_env = docker.from_env()
    images = client_env.images.list()
    result = {}
    for index, image in enumerate(images):
        result[index] = image.labels
    print(result)
    return HttpResponse(json.dumps(result))
