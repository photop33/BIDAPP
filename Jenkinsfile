pipeline {
    agent any
	stages {
		stage('properties') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('0 0 * * *')])])
                    properties([buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20')),])
                }
            }
        }
        stage('Export Data') {
            steps {
                script {
                    bat 'echo hello'
                }
            }
        }
    }
}
