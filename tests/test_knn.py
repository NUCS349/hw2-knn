import numpy as np
from code import KNearestNeighbor, load_json_data
from code import accuracy
import os

datasets = [
    os.path.join('data', x)
    for x in os.listdir('data')
    if os.path.splitext(x)[-1] == '.json' 
]

def xp_dataset_name(key):
    dataset = [d for d in datasets if key in d]
    if not dataset:
        raise ValueError('Dataset ' + key + ' cannot be found')
    return dataset[0]

def test_k_nearest_neighbor():
    accuracies = {}
    print(datasets)
    for data_path in datasets:
        features, targets = load_json_data(data_path)
        model = KNearestNeighbor(1)
        model.fit(features, targets)
        labels = model.predict(features)
        acc = accuracy(targets, labels)
        assert (acc > .99)