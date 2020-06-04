pipeline {
  agent { docker { image 'python:3.7.4' } }
  stages {
    stage('build') {
      steps {
        echo "Building application..."
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        echo 'Testing...'
        sh 'python3 tests.py'
      }   
    }
  }
}