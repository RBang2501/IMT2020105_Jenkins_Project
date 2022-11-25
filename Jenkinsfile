pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/KaranjitSaha/SE-lab6-Assignment.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x function.py"
                sh "./function.py"
            }
        }
        stage('Passing Test Code') {
            steps {
                sh "chmod u+x pass.py"
                sh "./pass.py"
            }
        }
        stage('Failing Test Code') {
            steps {
                sh "chmod u+x fail.py"
                sh "./fail.py"
            }
        }
    } 
}
