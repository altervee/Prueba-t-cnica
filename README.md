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



