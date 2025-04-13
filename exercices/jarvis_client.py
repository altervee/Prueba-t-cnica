import requests
"""
Just the logic of the client to interact with the Jarvis API.
This is a simple client to interact with the Jarvis API. It has two methods:
"""
class JarvisClient:# class to interact with the Jarvis API
    def __init__(self, candidate_key: str = "xVytsh2d0kRt"):
        self.base_url = "https://jarvis.visiotechsecurity.com"
        self.headers = {
            "candidate-key": "xVytsh2d0kRt" 
            }
        self.timeout = 10 

    def get_problem(self, problem_id: int):
        url = f"{self.base_url}/problem/{problem_id}"
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()  
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
            if response.status_code == 401:
                print("We dont have permission to access this resource.")
            return None
        except Exception as err:
            print(f"Error: {err}")
            return None

    def post_solution(self, problem_id: int, solution: list):
        url = f"{self.base_url}/problem/solution/{problem_id}"  
        try:
            data = {"solution": solution}  
            response = requests.post(
                url, 
                headers=self.headers, 
                json=data,  
                timeout=self.timeout
            )
            response.raise_for_status()  
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
            print(f"Response content: {err.response.text}") 
            return None
        except Exception as err:
            print(f"Error posting solution: {err}")
            return None

#jarvis = JarvisClient()
# example_solution=["mente", "espacio"]
# solution = jarvis.post_solution(1, example_solution)
# print(solution) # Print the solution response
# problema = jarvis.get_problem(1)
# print(problema) # Print the problem details