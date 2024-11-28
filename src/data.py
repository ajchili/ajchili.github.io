from dataclasses import dataclass
from typing import List


@dataclass
class Job():
    company_name: str
    link: str


current_job: Job = Job(company_name="Datavant",
                       link="https://www.datavant.com/")
previous_jobs: List[Job] = [
    Job(company_name="AWS", link="https://aws.amazon.com/console/"),
    Job(company_name="Leiods", link="https://www.leidos.com/"),
    Job(company_name="Google", link="https://cloud.google.com/"),
    Job(company_name="RAINN", link="https://rainn.org/"),
]
