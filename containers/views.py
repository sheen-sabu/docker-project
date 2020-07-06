from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from docker import APIClient
import docker
import json

from .forms import ContainerForm

def index(request):
    return HttpResponse("Hello, world. You're at the containers index.")

def list(request):
    client = docker.APIClient(base_url='unix://var/run/docker.sock')
    client_env = docker.from_env()
    tagname = 'dockerphpnginx'
    version = 'latest'
    version = client.version()
    print(version)
    return HttpResponse(json.dumps(version))
    return HttpResponse("Hello, world. You're at the containers index.")

def _form_view(request, template_name='basic.html', form_class=ContainerForm):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            tagname = data.get('tagname')
            version = 'latest'
            docker_manager = DockerManager('/Users/ajeeshv486/Downloads/testdjangoapp/dockermanager/containers/resources/docker-php-nginx')
            docker_manager.docker_build(tagname)
            container = docker_manager.docker_create_container(tagname, version)
            context = {'id': container.id}
            return JsonResponse(context)
    else:
        form = form_class()
    return render(request, template_name, {'form': form})

def create(request):
    return _form_view(request, template_name='create_container.html')

class DockerManager:
    def __init__(self, dockerfile_path):
        self.dockerfile_path = dockerfile_path
        # change the socket file path based on your server. If you are running on a specific linux flavour, you may need to find the 
        # flavour programmatically and then do something like below:
        # { 
        #   "ubuntu": "unix://var/run/docker.sock",
        #   "fedora": "unix://var/run/docker/docker.sock"
        # }
        self.client = docker.APIClient(base_url='unix://var/run/docker.sock')
        self.client_env = docker.from_env()

    def docker_build(self, tagname):
            response = [line for line in self.client.build(path=self.dockerfile_path, rm=True, tag=tagname)]    
            return(response)

    def docker_create_container(self, tagname, version):
        container = self.client_env.containers.run(tagname + ':' + version, detach=True,ports={8090:8090})
        return container