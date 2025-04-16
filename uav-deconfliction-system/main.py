# main.py
from mission_parser import load_missions
from spatial_check import check_spatial_conflicts
from temporal_check import check_temporal_conflicts
from visualizer import visualize_missions


def check_deconfliction(primary_mission, other_missions, buffer=10):
    spatial_conflicts = check_spatial_conflicts(primary_mission, other_missions, buffer)
    temporal_conflicts = check_temporal_conflicts(primary_mission, other_missions, buffer)
    
    conflicts = spatial_conflicts + temporal_conflicts
    if conflicts:
        return "conflict detected", conflicts
    return "clear", []


if __name__ == "__main__":
    primary, others = load_missions("./test_cases/primary_mission.json", "./test_cases/other_drones.json")
    status, conflicts = check_deconfliction(primary, others)
    print("Status:", status)
    for conflict in conflicts:
        print(conflict)

    visualize_missions(primary, others, conflicts)
