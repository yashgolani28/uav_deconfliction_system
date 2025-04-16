# UAV Strategic Deconfliction System – Reflection & Justification

## Design Decisions

The system is designed in modular Python scripts, with a clear separation of concerns:
- `mission_parser.py` handles input loading.
- `spatial_check.py` manages spatial deconfliction using Euclidean distance.
- `temporal_check.py` detects overlaps in both time and location.
- `visualizer.py` provides a 3D plot of drone paths and highlights conflicts.
- `main.py` integrates all modules and defines a simple query interface.

This structure ensures clarity, reusability, and ease of testing.

## Spatial & Temporal Check Logic

### Spatial
- Conflicts are flagged if the Euclidean distance between any two waypoints (from different drones) falls below a safety buffer (default: 10 meters).

### Temporal
- Time windows are compared.
- Conflicts are flagged when waypoints from different drones are close in both space and time.

## AI Integration (Optional for Extra Credit)

Although not included in this version, the system can be extended with:
- AI trajectory prediction based on past flight behavior.
- Machine learning classification to predict future conflicts.

## Testing Strategy

Test scenarios include:
- Conflict-free routes
- Conflicts in space only
- Conflicts in time only
- Combined spatial-temporal overlaps

Edge cases:
- Waypoints exactly on the boundary of the safety buffer.
- Overlapping time windows with no spatial proximity.
- Multiple drones causing simultaneous conflicts.

## Scalability for Real-World Use

To handle real-world deployments with thousands of drones:

### Architectural Enhancements
- **Distributed Processing**: Use Apache Kafka + Spark for real-time trajectory streaming and parallel conflict checking.
- **Scalable Storage**: Store trajectories in a spatial-temporal database like PostGIS or TimescaleDB.
- **Fast Search**: Use spatial indexing (R-Trees) to reduce lookup time.
- **Fault Tolerance**: Microservice architecture with retry and fallback logic.

With these, the system can support airspace coordination for urban drone networks or commercial delivery swarms.

---
