import os
import yaml

def create_dir(path):
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        raise e

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content