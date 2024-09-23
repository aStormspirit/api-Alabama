import docker
from celery_app import app

def run_docker_container(image_name):
    client = docker.from_env()
    container = client.containers.run(image_name, detach=True)
    return container

@app.task(bind=True)
def run_and_wait_for_container(self, image_name, timeout=300):
    container = run_docker_container(image_name)
    all_logs = ""
    
    while container.status != 'exited':
        logs = container.logs(stream=True, follow=True, tail=1)
        for log in logs:
            log_line = log.decode('utf-8')
            all_logs += log_line
            print(log_line, end='')  # Выводим логи в реальном времени
        container.reload()  # Обновляем статус контейнера
    
    if container.status != 'exited':
        print(f"Контейнер не завершил работу за {timeout} секунд. Принудительно останавливаем.")
        container.stop()
    
    exit_code = container.wait()['StatusCode']
    container.remove()
    
    return all_logs, exit_code

    