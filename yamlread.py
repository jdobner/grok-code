import yaml
from pprint import pprint as pr


def read_and_print(file="yamlread2.yaml") -> {}:
    with open(file, 'r') as fp:
        d = yaml.load(fp, Loader=yaml.FullLoader)
        pr(d)
        print("\n\n\n")
        return d

def doit():
    read_and_print("yamlread.yaml")
    read_and_print('yamlread2.yaml')

