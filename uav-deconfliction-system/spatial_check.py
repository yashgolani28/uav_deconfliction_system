from math import sqrt

def euclidean(p1, p2):
    return sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def check_spatial_conflicts(primary, others, buffer=10):
    conflicts = []
    primary_path = primary['waypoints']
    for drone in others:
        for i, wp1 in enumerate(primary_path):
            for j, wp2 in enumerate(drone['waypoints']):
                if euclidean(wp1[:3], wp2[:3]) <= buffer:
                    conflicts.append({
                        'type': 'spatial',
                        'location': wp1[:3],
                        'conflict_with': drone['id'],
                        'step': (i, j)
                    })
    return conflicts
