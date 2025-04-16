def check_temporal_conflicts(primary, others, buffer=10):
    conflicts = []
    T_start, T_end = primary['time_window']
    for drone in others:
        d_start, d_end = drone['time_window']
        if not (T_end < d_start or T_start > d_end):  # time windows overlap
            for wp1 in primary['waypoints']:
                for wp2 in drone['waypoints']:
                    if abs(wp1[3] - wp2[3]) < buffer:  # time conflict within buffer
                        spatial_dist = sum((a - b) ** 2 for a, b in zip(wp1[:3], wp2[:3])) ** 0.5
                        if spatial_dist <= buffer:
                            conflicts.append({
                                'type': 'temporal',
                                'location': wp1[:3],
                                'time': wp1[3],
                                'conflict_with': drone['id']
                            })
    return conflicts
