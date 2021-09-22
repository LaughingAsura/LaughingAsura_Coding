pipeline {
  agent any
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
echo $runScript
echo $printString'''
      }
    }

    stage('Testing') {
      steps {
        echo 'Testing'
        build 'test1'
      }
    }

  }
  environment {
    runScript = 'True'
    printString = 'True'
  }
  options {
    skipDefaultCheckout()
  }
}