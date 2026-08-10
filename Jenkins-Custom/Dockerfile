FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    docker.io && \
    apt-get clean

# Make the docker group use the same GID as the mounted Docker socket
RUN groupmod -g 0 docker && \
    usermod -aG docker jenkins

USER jenkins