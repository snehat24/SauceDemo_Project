pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Install Browsers') {
            steps {
                bat 'playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest -v'
            }
        }
    }
}