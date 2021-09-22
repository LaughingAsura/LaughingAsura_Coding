pipeline {
  agent {
    node {
      label 'jenkins_pipeline_slave'
    }

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
      when {
        environment name: 'runScript', value: 'No'
      }
      steps {
        sh '''pwd
echo $runScript
echo $printString'''
      }
    }

    stage('Testing') {
      when {
        environment name: 'runScript', value: 'Yes'
      }
      steps {
        echo 'Testing'
        build 'test1'
      }
    }

  }
  environment {
    runScript = 'Yes'
    printString = 'Yes'
  }
  options {
    skipDefaultCheckout()
  }
}
