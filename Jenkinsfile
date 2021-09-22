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
        environment name: 'runScript', value: False
      }
      steps {
        sh '''pwd
echo $runScript
echo $printString'''
      }
    }

    stage('Testing') {
      steps {
        echo 'Testing'
        build(job: 'test1', parameters: [[$class: 'StringParameterValue', runScript: $runScript, printString: $printString]])
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