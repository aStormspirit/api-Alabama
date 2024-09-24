from celery_app import app
import subprocess


@app.task(bind=True)
def run_docker_container(self, image_name):
    
    try:
        result = subprocess.run(['./container.sh', image_name], capture_output=True, text=True, check=True)
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
    except subprocess.CalledProcessError as e:
        return {
            "stdout": e.stdout,
            "stderr": e.stderr,
            "returncode": e.returncode
        }

