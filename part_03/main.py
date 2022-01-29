import yaml
import time

YAML_FILE = "config.yaml"


if __name__ == '__main__':
    with open(YAML_FILE, "r") as f:
        content = yaml.safe_load(f)
    print(content)
    for table in content['tables']:
        print(f"New table: {table}")

    i = 1
    while True:
        print(i)
        i += 1
        time.sleep(10)
