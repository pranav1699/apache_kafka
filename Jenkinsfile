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
    
    stage('Start container') {
      steps {
        bat 'docker compose up -d'
        bat 'docker compose ps'
      }
    }
    
  }
}
