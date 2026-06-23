pipeline {
    agent any

    stages {
        stage('Build Image') {
            steps {
                sh '/usr/local/bin/docker build -t pytest-framework .'
            }
        }

        stage('Run Tests') {
            steps {
                sh '/usr/local/bin/docker run --rm pytest-framework'
            }
        }
    }
}
