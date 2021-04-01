
import docker

_client = None
_containers = {}

def get_client():
    global _client
    if _client is None:
        _client = docker.from_env()
    return _client

def get_container(image_name):
    global _containers
    if image_name not in _containers:
        client = get_client()
        _containers[image_name] = client.containers.run(image=image_name, detach=True, tty=True)
    return _containers[image_name]

def run_in_container(image_name, command):
    container = get_container(image_name)
    (exit_code, output) = container.exec_run(cmd=command)
    return (exit_code, output)

