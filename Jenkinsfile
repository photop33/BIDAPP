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
        stage('Export Data') {
            steps {
                script {
                    bat script: 'start ExportXL.py', returnStatus: true
                }
            }
        }
	stage('Orgine XL') {
            steps {
                script {
                    bat script: 'start organize_XL.py', returnStatus: true
                }
            }
        }
	stage('convert Json') {
            steps {
                script {
                    bat script: 'start Convert_json.py', returnStatus: true
                }
            }
        }
	stage('check Json') {
            steps {
                script {
                    bat script: 'start Check_json.py', returnStatus: true
                }
            }
        }
    }
}
