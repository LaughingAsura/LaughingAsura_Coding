pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            echo 'Building'
          }
        }

        stage('ParallelBuild') {
          steps {
            echo 'ParallelBuild'
          }
        }

      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying'
      }
    }

    stage('Testing') {
      steps {
        echo 'Testing'
      }
    }

  }
}