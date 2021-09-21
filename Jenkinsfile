pipeline {
  agent any
  options { 
    skipDefaultCheckout() 
  } 
  stages {
    stage('Docker') {
      parallel {
        stage('Docker') {
          steps {
            node(label: 'jenkins_pipeline_slave') {
              sh '''pwd
ls -lrt
'''
            }

          }
        }

        stage('ParallelBuild') {
          steps {
            echo 'Parallel Building..'
          }
        }

      }
    }

    stage('Cloning') {
      steps {
        sh '''pwd
git clone https://github.com/LaughingAsura/LaughingAsura_Coding.git'''
      }
    }

    stage('Testing') {
      steps {
        echo 'Testing'
      }
    }

  }
}
