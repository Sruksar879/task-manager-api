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
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Test'){
            steps{
             sh 'pytest'
            }
        }
        stage('Build Docker Image'){
            steps{
                sh 'docker build -t task-manager-api:v1'
            }
        }

    }
}