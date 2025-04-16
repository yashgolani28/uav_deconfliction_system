import json

def load_missions(primary_file, others_file):
    with open(primary_file, 'r') as f:
        primary = json.load(f)

    with open(others_file, 'r') as f:
        others = json.load(f)

    return primary, others
