import random
def knn_distance(arr, q, k):
    """Compute the kth nearest point and the distance to it."""
    # TODO: Implement the knn_distance function
    distances = []
    for x in arr:
        distances.append((abs(x - q), x))
    distances.sort()
    return distances[k-1]
