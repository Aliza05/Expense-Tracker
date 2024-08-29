pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Activating virtual environment and starting the server...'
                bat 'call venv\\Scripts\\activate && py manage.py runserver 0.0.0.0:8000'
            }
        }
    }
}
