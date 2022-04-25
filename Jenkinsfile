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
        bat '''for /f %%i in ('docker ps -qf "name=^kafka-git-jenkins"') do set containerId=%%i
echo %containerId%
If "%containerId%" == "" (
  echo "No Container running"
) ELSE (
  docker stop %ContainerId%
  docker rm -f %ContainerId%
)'''
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
