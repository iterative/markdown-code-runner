
import docker
import re
import string

_client = None
_containers = {}

def get_client():
    global _client
    if _client is None:
        _client = docker.from_env()
    return _client

def get_container(image_name: str):
    global _containers
    if image_name not in _containers:
        client = get_client()
        _containers[image_name] = client.containers.run(image=image_name, detach=True, tty=True)
    return _containers[image_name]

def _merge_command_lines(command: str):
    "Merges command lines split by \\"
    return command.replace("\\\n", "")

def _fix_initial_dollar(command: str):
    command = re.sub(r"^[$]\s+", "", command)
    return command

def run_in_container(image_name: str, command: str, fix_initial_dollar=True):
    container = get_container(image_name)
    command = _merge_command_lines(command)
    if fix_initial_dollar:
        command = _fix_initial_dollar(command)
    print(f"Running: {command}")
    (exit_code, output) = container.exec_run(cmd=command)
    return (exit_code, output)

