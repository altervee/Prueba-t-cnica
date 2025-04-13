# Python_technical_test

This repository contains the solutions to a Python technical test.

---

## Exercise 1 – Gem Finder

This is the result of the first exercise, where we scan a matrix for hidden "Infinity Stones" (gems):

![Exercise 1 Result](image.png)

---

## Exercise 2 – SQL Queries

These are the SQL queries used in the second exercise:

### 1. Get Current Locations of Averages

```sql
SELECT l.name 
FROM average a
JOIN location l ON a.current_location_id = l.Id;
2. Get Locations with More Than 3 Logs per Average
sql
Copiar
Editar
SELECT l.name 
FROM average_location_log all
JOIN location l ON all.location_id = l.Id
GROUP BY all.average_id, l.name
HAVING COUNT(*) > 3;
3. Update Satellites to Maintenance Status
sql
Copiar
Editar
UPDATE start_satellite ss
SET in_maintenance = TRUE
WHERE ss.location_id IN (
    SELECT DISTINCT a.current_location_id 
    FROM average a
)
AND RAND() < 0.5;
sql
Copiar
Editar

Feel free to copy and paste this into your `README.md` file! Let me know if you need any more tweaks or additions.
Exercise 3 – Fuel-Efficient Path to Ironman
This exercise involves calculating the most fuel-efficient route for a satellite to reach Ironman, considering dynamic weather penalties on each path.

### Goals
Start from New York

Find Ironman’s location (e.g. "Berlin")

Traverse via satellite links

Minimize fuel consumption

Ensure remaining fuel ≥ 30 units

### Fuel Rules
Start Fuel: 100 units

Base Consumption per Jump: 10 units

Weather Penalties:

"Viento en contra" → +1.5

"Lluvia" → +0.2

"Tormenta" → +2.0

### Solution Summary
Used Dijkstra’s algorithm to calculate the path with least fuel consumption, not just shortest hops.

Evaluated weather impact per satellite connection.

Ensured mission success based on final fuel.

### Sample Output
bash
Copiar
Editar
Ironman is in: Berlin
Calculated path: New York -> Washington -> Atlantic -> Madrid -> Barcelona -> Roma -> Paris -> Berlin
Remaining fuel: 34.3
Mission can succeed with enough fuel.