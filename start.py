import os

from dotenv import load_dotenv


os.environ["FLASK_APP"] = "index.py"
load_dotenv()

os.environ["DB_USER"] = os.getenv("DB_USER")
os.environ["DB_PASS"] = os.getenv("DB_PASS")
os.environ["DB_NAME"] = os.getenv("DB_NAME")


def run(stage: str):
    docker_cmd = f"docker-compose -f docker-compose.{stage}.yml up --build"

    os.system(f"{docker_cmd} -d {stage}-postgres")

    while True:
        log = os.popen(f"docker logs --until=2s {stage}-postgres").read()
        splitted = log.split()

        if splitted != []:
            if splitted[-1] == "initialization" or splitted[-1] == "up.":
                break

    os.chdir("./api")

    os.system("flask db migrate")
    os.system("flask db upgrade")

    os.chdir("..")

    os.system(docker_cmd)


run("dev")
