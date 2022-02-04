import os
import yaml
import argparse




def create_dir(path):
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        raise e


def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content

def config_data():
    """
    :return: Dict type with config details
    """
    return config_content

#saving data from config file
args = argparse.ArgumentParser()
args.add_argument("--config", "-c", default="configs/config.yaml")
parsed_args = args.parse_args()
config_path = parsed_args.config
config_content = read_yaml(config_path)