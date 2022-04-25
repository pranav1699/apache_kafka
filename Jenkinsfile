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
    stage("Remove containers"){
      steps{
      bat 'docker-compose down --remove-orphans'
        
      }
    }
    
    
    stage('Start containers') {
      steps {
        bat 'docker-compose up -d'
        bat 'docker-compose ps'
      }
    }
    
  }
}
