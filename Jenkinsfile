pipeline {
   agent any
  
   environment {
       DOCKER_HUB_REPO = "dangasper/placid-lake"
       CONTAINER_NAME = "poamtrkr"
       DOCKERHUB_CREDENTIALS=credentials('dockerhub-credentials')
   }
  
    stages {     
        stage('Build') {
           steps {
               echo 'Building..'
               sh 'docker image build -t $DOCKER_HUB_REPO:latest .'
           }
       }
       stage('Test') {
           steps {
               echo 'Testing..'
               sh 'docker stop $CONTAINER_NAME || true'
               sh 'docker rm $CONTAINER_NAME || true'
               sh 'docker run --name $CONTAINER_NAME $DOCKER_HUB_REPO /bin/bash -c "pytest flake8"'
           }
       }
        stage('Push') {
            steps {
                echo 'Pushing image..'
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS --password-stdin'
                sh 'docker push $DOCKER_HUB_REPO:latest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'kubectl -- apply -f k8s/deployment.yaml'
                sh 'kubectl -- apply -f k8s/service.yaml'
            }
        }
   }
}
