import importlib


def get_class_instance_by_name(module_name, class_name):
    module = importlib.import_module(module_name)
    clazz = getattr(module, class_name)
    return clazz()
