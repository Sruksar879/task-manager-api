pipeline {
    agent any
    stages{
        stage('Checkout'){
            steps{
                checkout scm
            }
        }
        stage('Install Dependencies'){
            steps{
                sh 'python3 -m venv .venv'
                sh '.venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Test'){
            steps{
             sh '.venv/bin/pytest'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t task-manager-api:v2 .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([
                    usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )
            ]) 
            {
                sh '''
                    echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                    docker tag task-manager-api:v2 $DOCKER_USERNAME/task-manager-api:v1
                    docker push $DOCKER_USERNAME/task-manager-api:v2
                '''
            }
        }
     }
     stage('Deploy') {
            steps {
                sh '''
                    docker stop task-manager-prod || true
                    docker rm task-manager-prod || true

                    docker pull sruksar879/task-manager-api:v2

                    docker run -d \
                        --name task-manager-prod \
                        -p 8001:8000 \
                        sruksar879/task-manager-api:v2
                '''
            }
        }

    }
}