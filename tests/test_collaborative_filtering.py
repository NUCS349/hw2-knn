import numpy as np 
from code import KNearestNeighbor, load_movielens_data

def test_collaborative_filtering():
    user_ratings = np.array([
        [1, 2, 0, 3, 2],
        [0, 2, 1, 3, 2],
        [1, 0, 1, 3, 2],
        [1, 2, 1, 0, 2],
        [1, 2, 1, 3, 0]
    ])
    real_ratings = np.array([
        [1, 2, 1, 3, 2],
        [1, 2, 1, 3, 2],
        [1, 2, 1, 3, 2],
        [1, 2, 1, 3, 2],
        [1, 2, 1, 3, 2]
    ])
    x = KNearestNeighbor(
            n_neighbors=5, 
            distance_measure='euclidean',
            aggregator='mode'
        )
    x.fit(user_ratings)
    predictions = x.predict(user_ratings)
    assert (np.allclose(real_ratings, predictions))