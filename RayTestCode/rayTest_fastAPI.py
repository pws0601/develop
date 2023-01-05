import requests
from fastapi import FastAPI
from ray import serve
import ray

# 1: Define a FastAPI app and wrap it in a deployment with a route handler.
app = FastAPI()


ray.init()

commValue = ray.put("000000")


@serve.deployment(route_prefix="/")
@serve.ingress(app)
class FastAPIDeployment:
    # FastAPI will automatically parse the HTTP request for us.
    @app.get("/hello")
    def say_hello(self, name: str) -> str:
        return f"Hello {name}! CommonValue {ray.get(commValue)}"
    
    @app.get("/valueChange")
    def valueChange(self) -> str:
        global commValue
        commValue = ray.put("111111")
        return f"Value Change!!!!"

# 2: Deploy the deployment.
serve.run(FastAPIDeployment.bind())

# 3: Query the deployment and print the result.
print(requests.get("http://localhost:8000/hello", params={"name":"Theodore"}).json())
print(requests.get("http://localhost:8000/valueChange").json())
print(requests.get("http://localhost:8000/hello", params={"name":"Theodore"}).json())
# "Hello Thedore!"

ray.shutdown()