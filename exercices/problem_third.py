from jarvis_client import JarvisClient
from collections import deque

WEATHER_PENALTIES = {
    "Viento en contra": 1.5,
    "Lluvia": 0.2,
    "Tormenta": 2.0
}

BASE_FUEL_CONSUMPTION = 10.0
START_FUEL = 100.0
MIN_REQUIRED_FUEL = 30.0

def get_weather_penalty(weather: str) -> float:
    return WEATHER_PENALTIES.get(weather, 0.0)

def find_path(satellites, start, end):
    # Build mappings
    id_map = {sat["id"]: sat for sat in satellites}
    loc_to_id = {sat["location"]: sat["id"] for sat in satellites}
    id_to_loc = {sat["id"]: sat["location"] for sat in satellites}

    start_id = loc_to_id[start]
    end_id = loc_to_id[end]

    # calculate the short path using BFS
    queue = deque([[start_id]])
    visited = set()

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == end_id:
            return [id_to_loc[i] for i in path]

        visited.add(current)
        for neighbor in id_map[current]["nearest_sats"]:
            if neighbor not in visited and neighbor not in path:
                queue.append(path + [neighbor])

    return []

def calculate_fuel(path, satellites):
    loc_to_sat = {sat["location"]: sat for sat in satellites}
    fuel = START_FUEL

    for i in range(1, len(path)):
        loc = path[i]
        weather = loc_to_sat[loc]["weather"]
        penalty = get_weather_penalty(weather)
        fuel -= (BASE_FUEL_CONSUMPTION + penalty)

    return fuel

def main():
    jarvis = JarvisClient()

    # problem = jarvis.get_problem(3)
    # mocked problem for testing
    problem={"problem":3, "satellites":[{ "id": 1, "location": "New York", "weather": "Despejado", "nearest_sats": [2,6,13] }, { "id": 2, "location": "Washington", "weather": "Despejado", "nearest_sats": [1,6] }, { "id": 3, "location": "London", "weather": "Tormenta", "nearest_sats": [4,7,11] }, { "id": 4, "location": "Barcelona", "weather": "Despejado", "nearest_sats": [3,5,7,12] }, { "id": 5, "location": "Madrid", "weather": "Despejado", "nearest_sats": [4,6] }, { "id": 6, "location": "Atlantic", "weather": "Lluvia", "nearest_sats": [1,2,5] }, { "id": 7, "location": "Edimburg", "weather": "Viento en contra", "nearest_sats": [3,4] }, { "id": 8, "location": "Tokyo", "weather": "Lluvia", "nearest_sats": [9,14,19] }, { "id": 9, "location": "Beijin", "weather": "Lluvia", "nearest_sats": [8,14,19] }, { "id": 10, "location": "Moscow", "weather": "Despejado", "nearest_sats": [17,20] }, { "id": 11, "location": "Paris", "weather": "Despejado", "nearest_sats": [3,12,20] }, { "id": 12, "location": "Roma", "weather": "Despejado", "nearest_sats": [4,11] }, { "id": 13, "location": "Austin", "weather": "Despejado", "nearest_sats": [1,15] }, { "id": 14, "location": "Pacific", "weather": "Tormenta", "nearest_sats": [8,9,15] }, { "id": 15, "location": "California", "weather": "Despejado", "nearest_sats": [13,14] }, { "id": 16, "location": "Iran", "weather": "Despejado", "nearest_sats": [18,17] }, { "id": 17, "location": "Kazajistan", "weather": "Despejado", "nearest_sats": [10,16] }, { "id": 18, "location": "Pakistan", "weather": "Despejado", "nearest_sats": [16,19] }, { "id": 19, "location": "India", "weather": "Despejado", "nearest_sats": [8,9,18] }, { "id": 20, "location": "Berlin", "weather": "Despejado", "nearest_sats": [10,11] }]}
    satellites = problem["satellites"]

    # ironman_location = jarvis.get("/where_is_ironman")["ironman_location"]
    ironman_location = "Berlin"  # Mocked location for testing
    print("Ironman is in:", ironman_location)

    path = find_path(satellites, "New York", ironman_location)

    if not path:
        print("No valid path found.")
        return

    print("Calculated path:", " -> ".join(path))

    final_fuel = round(calculate_fuel(path, satellites), 2)
    print("Remaining fuel:", final_fuel)

    solution = {
        "solution": path,
        "final_fuel": final_fuel
    }

    # response = jarvis.post_solution(3, solution)
    print("Server response:", solution)

if __name__ == "__main__":
    main()
