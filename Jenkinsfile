pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Activating virtual environment and starting the server...'

                // Activate the virtual environment and run the server
                bat '''
                call venv\\Scripts\\activate
                python manage.py runserver
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Additional clean-up actions if needed
        }
    }
}
