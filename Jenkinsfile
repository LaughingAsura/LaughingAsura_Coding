pipeline {
  agent {
    node {
      label 'jenkins_pipeline_slave'
    }

  }
  parameters {
      string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
      text(name: 'BIOGRAPHY', defaultValue: '', description: 'Enter some information about the person')
      booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')
      choice(name: 'CHOICE', choices: ['One', 'Two', 'Three'], description: 'Pick something')
      password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')
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
