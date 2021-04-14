from locust import HttpUser, task, between

HOST_URL = "http://********TO BE REPLACED********/"
AUTHORIZATION_TOKEN = "Token eyJ0eXA********TO BE REPLACED********IUzI1NiJ9"

class ApiTestUser(HttpUser):
    wait_time = between(0.1, 0.5)
    
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    # @task(1)
    # def check_health(self):
    #     self.client.get(HOST_URL)


    # @task(2)
    # def login(self):
    #     url = HOST_URL + "/api/v3.4/auth_service/login/"
    #     self.client.post(url, {"email":"android@gmail.com", "password":"aaaaaa"})


    @task(3)
    def feed(self):
        url = HOST_URL + "/api/v3.5/social_service/post/?score=true&measurement=true&post_from=followings,public,group"   
        self.client.get(url, headers={"Authorization":  AUTHORIZATION_TOKEN})



# Execution Command: `locust -f test_script.py`