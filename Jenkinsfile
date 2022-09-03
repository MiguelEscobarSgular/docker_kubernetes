pipeline {
  agent any
  stages {
    stage('environmet') {
      steps {
        bat 'dir'
        bat 'build'
      }
    }

    stage('run') {
      steps {
        bat 'run'
      }
    }

  }
}