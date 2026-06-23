pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:${env.PATH}"
    }

    stages {
        stage('Build Image') {
            steps {
                sh 'docker build -t pytest-framework .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm pytest-framework'
            }
        }
    }
}
