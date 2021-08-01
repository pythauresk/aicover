import os
import configparser


# ---------------------------------------------------
# ACCESS CONFIG FILES
def get_config_value(config_file_path, variable, param):
    """Extract value in .config file"""
    config = configparser.ConfigParser()
    config.read(config_file_path)
    return config[variable][param]


def get_config_file_path(config_file_path, variable, param):
    """Extract file path from config file"""
    return os.path.join(os.getcwd(), get_config_value(config_file_path, variable, param))


if __name__ == '__main__':
    pass
