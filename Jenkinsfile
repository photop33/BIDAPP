pipeline {
    agent any
	stages {
        stage('Export Data') {
            steps {
                script {
                    sh 'python ExportXL.py'
                }
            }
        }
    }
}
