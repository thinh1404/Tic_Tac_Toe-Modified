pipeline {
    agent any 

    stages {
        stage('Build') {
            steps {
                script {
                echo 'Building the application...'
                sh 'docker login -u jimmythinh1404'
                sh 'docker build -t your_username/tic-tac-toe .'
              
                // For example, if you have a requirements.txt, you can use:
                // sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // You can run your tests here
                // For example, if you have a test suite, you can use:
                // sh 'pytest'  // or whatever testing framework you're using
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Here you would add your deployment commands
                // This might include copying files to a server or starting a service
                // Example:
                // sh 'scp -r ./* user@yourserver:/path/to/deploy/'
            }
        }

        stage('Release') {
            steps {
                echo 'Releasing the application...'
                // You can add steps to notify users or finalize the release here
                // For example:
                // sh 'echo "Application released!"'
                // Or you might trigger a notification to a chat system, etc.
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Clean up actions, if necessary
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
