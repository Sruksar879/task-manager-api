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
        stage('Build Docker Image'){
            steps{
                sh 'docker build -t task-manager-api:v1 .'
            }
        }

    }
}