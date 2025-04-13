from jarvis_client import JarvisClient
from typing import List

def find_gems(matrix: List[List[str]]) -> List[str]:
    valid_gems = {"SPACE", "MIND", "REALITY", "TIME", "POWER", "SOUL"}
    found = set()
    rows = len(matrix)
    if rows == 0:
        return []
    cols = len(matrix[0])

    for row in matrix:
        row_str = ''.join(row)
        for gem in valid_gems:
            if gem in row_str:
                found.add(gem)

    for col in range(cols):
        col_str = ''.join(matrix[row][col] for row in range(rows))
        for gem in valid_gems:
            if gem in col_str:
                found.add(gem)

    return sorted(found)

def main():
    jarvis = JarvisClient()
    """
    I have to comment this part because the server is not available.
    I will use a mock problem instead.
    """
    # try:
    #     problem = jarvis.get_problem(1)
    #     for row in problem["matrix"]:
    #         print(' '.join(row))
    # except Exception as e:
    #     print(f"Error getting problem: {e}")
    #     return
    problem = {
        "problem": 1,
        "size": 8,
        "matrix": [ ["L","R","D","S","M","V","E","R","V"], ["P","W","K","O","P","O","W","E","R"], ["S","A","B","U","A","E","M","T","V"], ["P","L","S","L","A","A","R","F","K"], ["A","I","N","F","L","P","C","W","F"], ["C","T","S","M","M","T","K","P","H"], ["E","G","M","I","T","I","M","E","P"], ["A","E","R","N","K","R","U","D","Z"], ["Q","C","P","D","F","B","G","W","N"], ]
        }
    solution = find_gems(problem["matrix"])
    print("Found gems:", solution)
    if solution:
        try:
            response = jarvis.post_solution(1, solution)
            print("Server response:", response)
        except Exception as e:
            print(f"Error posting solution: {e}")
    else:
        print("No gems found")
if __name__ == "__main__":
    main()