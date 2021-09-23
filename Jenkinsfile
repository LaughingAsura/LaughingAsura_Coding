pipeline {
  agent {
    node {
      label 'jenkins_pipeline_slave'
    }

  }
  parameters {
    string(name: 'runScript', defaultValue: 'Yes')
    string(name: 'printString', defaultValue: 'Yes')
    string(name: 'BRANCH', defaultValue: 'Testing_Branch')
    string(name: 'TESTBED', defaultValue: '/builds/testbeds/ucsblr742cip')
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
        parameter name: 'runScript', value: 'No'
      }
      steps {
        sh '''pwd
echo $runScript
echo $printString'''
      }
    }

    stage('Testing') {
      when {
        parameter name: 'runScript', value: 'Yes'
      }
      steps {
        echo 'Testing'
        build job: 'your-job-name', 
          parameters: [
            string(name: 'runScript', value: String.valueOf(params.runScript)),
            string(name: 'printString', value: 'prefix-' + String.valueOf(params.printString))
    ]
      }
    }

  }
  options {
    skipDefaultCheckout()
  }
}
