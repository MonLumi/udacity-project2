from locust import HttpUser, task

class HelloWorldUser(HttpUser):
   @task(1)
   def hello_world(self):
      self.client.get("https://anhnvv1.azurewebsites.net")

   @task(2)
   def test_predict(self):
      self.client.post("https://anhnvv1.azurewebsites.net/predict", json={
            "CHAS":{
               "0":0
            },
            "RM":{
               "0":6.575
            },
            "TAX":{
               "0":296.0
            },
            "PTRATIO":{
               "0":15.3
            },
            "B":{
               "0":396.9
            },
            "LSTAT":{
               "0":4.98
            }
         })