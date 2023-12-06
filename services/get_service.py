from .git import GitService
from .log import LogService
from .open import OpenService
from .work_with import WorkWith

def get_service(service_name):
    if service_name == "git":
        return GitService()
    if service_name == "log":
        return LogService()
    if service_name == "code":
        return OpenService()
    if service_name == "ww":
        return WorkWith()
    else:
        raise ValueError(f"Servicio no reconocido: {service_name}")
