# Model, Controller, View (MVC) Pattern Example (in Python)
import os 
from typing import Callable, Any
import time
import requests

class Model:
    def __init__(self):
        self.data = {}

    def get_data(self, key: str) -> Any:
        return self.data.get(key)

    def set_data(self, key: str, value: Any):
        self.data[key] = value

class View:
    def display(self, data: Any):
        print(f"Displaying data: {data}")   

class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def update_data(self, key: str, value: Any):
        self.model.set_data(key, value)
        self.view.display(self.model.get_data(key))

    def fetch_data_from_api(self, url: str):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for key, value in data.items():
                self.update_data(key, value)
        else:
            print(f"Failed to fetch data from {url}")

if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)

    # Simulate fetching data from an API
    api_url = "https://jsonplaceholder.typicode.com/posts/1"
    controller.fetch_data_from_api(api_url)

    # Update data manually
    controller.update_data("new_key", "new_value")
    
    # Display current state of the model
    print("Current model data:", model.data)


