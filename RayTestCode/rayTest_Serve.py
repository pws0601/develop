import requests
from typing import Dict
from starlette.requests import Request
from ray import serve

# 1 : Define a Ray Serve deployment.
@serve.deployment(route_prefix="/")
class MyModelDeployment:
    # Initialize model state: could be very large neural net weights.
    def __init__(self, msg: str):
        self._msg = msg
    
    def __call__(self, request: Request) -> Dict:
        return {"result": self._msg}


# 2 : Deploy the model.
serve.run(MyModelDeployment.bind(msg="HELLO world!"))
print(requests.get("http://localhost:8000/").json())