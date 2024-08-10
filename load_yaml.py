import yaml

with open("test.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file)

print(config['model']['type'])  # Outputs: RandomForest