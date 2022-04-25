pipeline {
  agent any
  stages {
    stage("verify tooling") {
      steps {
        bat '''
          docker version
          docker info
          docker compose version 
        '''
      }
    }
    stage('Stop and remove prev docker container') {
      steps {
        bat 'docker container rm kafka-git-jenkins'
      }
    }
    stage('Start container') {
      steps {
        bat 'docker compose up -d'
        bat 'docker compose ps'
      }
    }
    
  }
}
