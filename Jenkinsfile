pipeline {
  agent {
    node {
      label 'jenkins_pipeline_slave'
    }

  }
  parameters {
    string(runScript: 'Yes', defaultValue: 'NA')
    string(printString: 'Yes', defaultValue: 'NA')
    string(BRANCH: 'testing_branch', defaultValue: 'NA')
    string(TESTBED: '/builds/testbeds/ucsblr742cip', defaultValue: 'NA')
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
        build job: 'your-job-name', 
          parameters: [
            string(name: 'runScript', value: String.valueOf(runScript)),
            string(name: 'printString', value: 'prefix-' + String.valueOf(printString))
    ]
      }
    }

  }
  options {
    skipDefaultCheckout()
  }
}
