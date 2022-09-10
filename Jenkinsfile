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
        bat 'run_stage'
      }
    }

    stage('test') {
      steps {
        bat 'python3 ./test_script/test_api.py'
      }
    }

  }
}