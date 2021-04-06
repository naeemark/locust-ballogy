from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)
    
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def check_health(self):
        self.client.get("http://********TO BE REPLACED********/update_data")

    # @task(2)
    # def login(self):
    #     self.client.post("http://********TO BE REPLACED********/auth_service/login/", {"email":"android@gmail.com", "password":"aaaaaa"})

    # @task(3)
    # def feed(self):        
    #     self.client.get("http://********TO BE REPLACED********/social_service/post/?score=true&measurement=true&post_from=followings,public,group", headers={"Authorization":  "Token eyJ0eXAi.********TO BE REPLACED********YIZ4AYsdsQ5sdjLtN"}
    #     )