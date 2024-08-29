pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'py manage.py runserver'
            }
        }
    }
}
