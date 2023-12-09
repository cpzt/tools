
from jenkins import Jenkins


class JenkinsTool:
    def __init__(self, url: str, username: str, password: str):
        self.client = Jenkins(url, username, password)

    def build(self, job_name: str, params: dict = None):
        self.client.build_job(job_name, params)
