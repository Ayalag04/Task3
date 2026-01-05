import docker

client = docker.from_env()

container = client.containers.run(
    "busybox",          # Image
    "sleep 3600",       # Command that keeps the container running for one hour
    detach=True         
)

exec_log = container.exec_run("hostname")
print("Container hostname:", exec_log.output.decode())

container.stop()
container.remove()
