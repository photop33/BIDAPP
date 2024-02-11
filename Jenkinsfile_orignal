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
                    bat 'python ExportXL.py'
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
