import docker

client = docker.from_env()

container = client.containers.run("kansas", detach=True)

for line in container.logs(stream=True):
  print(line.strip())