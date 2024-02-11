pipeline {
    agent any
      stages {
 	 stage('Export Data') {
      	     steps {
             	script {
                 	bat 'echo hello'
                }
            }
        }
	stage('Orgine XL') {
            steps {
                script {
                    bat script: 'python organize_XL.py', returnStatus: true
                }
            }
        }
	stage('convert Json') {
            steps {
                script {
                    bat script: 'python Convert_json.py', returnStatus: true
                }
            }
        }
	stage('check Json') {
            steps {
                script {
                    bat script: 'python Check_json.py', returnStatus: true
                }
            }
        }
    }
}
