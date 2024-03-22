import importlib
import yaml
import os
from test_data.yaml_data import YamlData

def load_yaml(exe_path):
    file_name = exe_path.replace('test_case.', "")
    file_name = os.path.join('.', 'test_data', f'{file_name}.yml')
    with open(file_name, 'r') as file:
        test_data = yaml.safe_load(file)
        return YamlData(test_data)

# exe_paths = [
# 'test_case.test_login',
# 'test_case.test_logout',
# 'test_case.test_signup'
# ]
exe_paths = ['test_case.test_signup']
for exe_path in exe_paths:
    print(f'---- {exe_path} -----')
    test_case = importlib.import_module(exe_path)
    test_data = load_yaml(exe_path)
    test_case.test_act(test_data)
