from dataclasses import dataclass
from typing import List


@dataclass
class Job():
    name: str
    link: str


@dataclass
class Project():
    name: str
    details: str
    image_urls: List[str]
    github_link: str | None = None
    link: str | None = None


current_job: Job = Job(name="Datavant", link="https://www.datavant.com/")
previous_jobs: List[Job] = [
    Job(name="AWS", link="https://aws.amazon.com/console/"),
    Job(name="Leiods", link="https://www.leidos.com/"),
    Job(name="Google", link="https://cloud.google.com/"),
    Job(name="RAINN", link="https://rainn.org/"),
]

projects: List[Project] = [
    Project(
        name="Mock Me",
        details="Self-hosted interview practice web app.",
        github_link="https://github.com/ajchili/mock-me",
        image_urls=[
            "https://kirinpatel.nyc3.digitaloceanspaces.com/images/mock-me-candidate.png",
            "https://kirinpatel.nyc3.digitaloceanspaces.com/images/mock-me-interviewer.png"
        ],
        link="https://mock-me.kirinpatel.com",
    ),
    Project(
        name="Stu",
        details="Collaborative web app for music creation.",
        image_urls=[
            "https://kirinpatel.nyc3.digitaloceanspaces.com/images/stu.png"
        ],
    ),
    Project(
        name="Kiesel In Stock Finder",
        details="Indexer for the Kiesel Guitars list of in-stock instruments, offering the ability to filter instruments by all specs.",
        github_link="https://github.com/ajchili/kiesel-in-stock-finder",
        image_urls=[
                "https://kirinpatel.nyc3.digitaloceanspaces.com/images/kiesel-in-stock-finder.png"
        ],
        link="https://kiesel.kirinpatel.com"
    ),
    Project(
        name="Dossier Made Media",
        details="Portfolio website for my videography business.",
        github_link="https://github.com/ajchili/dossiermade",
        image_urls=[
            "https://kirinpatel.nyc3.digitaloceanspaces.com/images/dossier-made.png"
        ],
        link="https://dossiermade.com"
    ),
    Project(
        name="visum",
        details="YouTube video summary tool which uses captions for car repair videos to generate a list of tools and steps required for a DIY repair.",
        github_link="https://github.com/ajchili/visum",
        image_urls=[
                "https://kirinpatel.nyc3.digitaloceanspaces.com/images/visum.png"
        ],
        link="https://visum.kirinpatel.com"
    ),
    Project(
        name="Beam",
        details="A web based experience inspired by Level 6 in Backrooms: Escape Together. Level 6 has a section which replaces the traditional camera with a LiDAR camera. I thought that was cool and built this as a side project to replicate the experience.",
        github_link="https://github.com/ajchili/beam",
        image_urls=[
                "https://kirinpatel.nyc3.digitaloceanspaces.com/images/beam.png"
        ],
        link="https://beam.kirinpatel.com/"
    ),
    Project(
        name="wokehub",
        details="Silly little rating website for github users.",
        github_link="https://github.com/ajchili/wokehub",
        image_urls=[
                "https://kirinpatel.nyc3.digitaloceanspaces.com/images/wokehub.png"
        ],
        link="https://wokehub.lol/"
    ),
]
