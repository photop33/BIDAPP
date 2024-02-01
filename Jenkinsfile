pipeline {
    agent any
	stages {
		stage('properties') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('0 0 * * *')])])
                    properties([buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20')),])
                }
                git 'https://github.com/photop33/BIDAPP.git'
            }
        }
        stage('Deploy Flask') {
            steps {
                script {
                    bat script: 'helm install ldap ./my-bitnami', returnStatus: true
                }
            }
        }
	}
}
