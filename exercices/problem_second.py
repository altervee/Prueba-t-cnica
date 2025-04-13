from exercices.jarvis_client import JarvisClient

def get_avengers_solution():
    solution = [
        """SELECT l.name 
           FROM average a
           JOIN location l ON a.current_location_id = l.Id""",
        """SELECT l.name 
           FROM average_location_log all
           JOIN location l ON all.location_id = l.Id
           GROUP BY all.average_id, l.name
           HAVING COUNT(*) > 3""",
        
        """UPDATE start_satellite ss
           SET in_maintenance = TRUE
           WHERE ss.location_id IN (
               SELECT DISTINCT a.current_location_id 
               FROM average a
           )
           AND RAND() < 0.5"""
    ]
    return solution

def main():
    jarvis = JarvisClient()
    
    try:
        problem = jarvis.get_problem(2)
        print("Problem data received")
        
        solution = get_avengers_solution()
        
        response = jarvis.post_solution(2, solution)
        print("Server response:", response)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()