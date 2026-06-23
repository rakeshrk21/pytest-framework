pipeline{
    agent Any
    stages {
        stage('Build Image'){
            steps {
                sh '/usr/local/bin/docker build -t pytest-framework .'
            }
       }
        stage('Run test'){
                steps {
                    sh '/usr/local/bin/docker run --rm pytest-framework .'
                }
        }
    }
}