pipeline {
    agent any
	stages {
        stage('Export Data') {
            steps {
                script {
                    bat 'python ExportXL.py'
                }
            }
        }
    }
}
