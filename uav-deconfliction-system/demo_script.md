# UAV Strategic Deconfliction System – Video Script

## [0:00–0:30] Introduction
"Hello, this is a demonstration of my internship project: a UAV Strategic Deconfliction System. It ensures a drone's planned mission is safe to fly in shared airspace by checking spatial and temporal conflicts against other drones."

## [0:30–1:30] Code Overview
"Here's the codebase. It includes modules for:
- Mission parsing
- Spatial conflict detection
- Temporal conflict checking
- 3D visualization of missions
- A main script to run everything."

## [1:30–2:30] Running the System
"We load a primary drone mission and multiple simulated drone schedules.
The program checks:
- If any other drone comes too close spatially.
- If their times overlap dangerously.

Here’s the output showing a detected conflict, including the location, time, and the drone ID causing it."

## [2:30–3:30] Visualization
"Now, we visualize the simulation in 3D:
- The blue line is the primary drone's mission.
- Dotted lines show other drones.
- Red points highlight where and when conflicts happen."

## [3:30–4:00] Wrap-up
"This system provides a simple, modular and scalable way to validate UAV missions before takeoff.

Extra credit can be earned by extending this to a 4D simulation — showing movement in 3D space over time. Thank you!"
