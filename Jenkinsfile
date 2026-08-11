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
                sh 'docker build -t task-manager-api:v1 .'
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
                    docker tag task-manager-api:v1 $DOCKER_USERNAME/task-manager-api:v1
                    docker push $DOCKER_USERNAME/task-manager-api:v1
                '''
            }
        }
     }

    }
}