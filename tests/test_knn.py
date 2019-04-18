import numpy as np
from code import KNearestNeighbor, load_json_data
from code import accuracy
import os


def test_k_nearest_neighbor():
    datasets = [
        os.path.join('data', x)
        for x in os.listdir('data')
        if os.path.splitext(x)[-1] == '.json' 
    ]
    for data_path in datasets:
        features, targets = load_json_data(data_path)
        model = KNearestNeighbor(1)
        model.fit(features, targets)
        labels = model.predict(features)
        acc = accuracy(targets, labels)
        assert (acc > .99)


def test_aggregators():
    _features = np.array([
        [-1, 1],
        [-1, 1],
        [-1, 1],
        [-1, 1],
        [-1, 1]
    ])
    _targets = np.array([
        [1, 1, 3, 4, 5]
    ])
    aggregators = ['mean', 'mode', 'median']
    answers = [np.mean(_targets), 1, np.median(_targets)]
    _est = []
    for a in aggregators:
        x = KNearestNeighbor(5, aggregator=a)
        x.fit(_features, _targets)
        y = x.predict(np.expand_dims(_features[0], 0))
        _est.append(y)
    assert (np.allclose(_est, answers))
