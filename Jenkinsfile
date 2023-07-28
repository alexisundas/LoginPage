pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = 'spik3r/login-page'
        AWS_REGION = 'eu-west-2b'
        AWS_INSTANCE_IP = 'ec2-13-42-63-64.eu-west-2.compute.amazonaws.com'
        AWS_SSH_KEY_CREDENTIALS = 'aws-ssh-key'
        AWS_INSTANCE_USER = 'ubuntu'
        DOCKERHUB_CREDENTIALS= credentials('dockerhub')
        
        
    }

    stages {
        stage('Debug Environment Variables') {
            steps {
                script {
                    echo "DOCKER_IMAGE_NAME: ${DOCKER_IMAGE_NAME}"
                    echo "AWS INSTANCE: ${AWS_INSTANCE_IP}"
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    // Log in to Docker Hub
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                }
            }
        }
        stage('Build and Push Docker Image to Docker Hub') {
            steps {
                script {
                sh "docker build -t login-page:latest ."
                sh "docker tag login-page:latest {$DOCKER_IMAGE_NAME}"
                sh "docker push {$DOCKER_IMAGE_NAME}"
               }
            }
        }    

        stage('Deploy to AWS EC2') {
            steps {
                script {
                    sshagent(['aws-ssh-key']) {
                    // SSH into the EC2 instance and pull the latest Docker image
                        sh "ssh -o StrictHostKeyChecking=no ${AWS_INSTANCE_USER}@${AWS_INSTANCE_IP} 'docker pull ${DOCKER_IMAGE_NAME}:latest'"

                    // Stop and remove the running container (if any)
                        sh "ssh -o StrictHostKeyChecking=no ${AWS_INSTANCE_USER}@${AWS_INSTANCE_IP} 'docker stop ${DOCKER_IMAGE_NAME} || true && docker rm ${DOCKER_IMAGE_NAME} || true'"

                    // Run the Docker container on the EC2 instance
                        sh "ssh -o StrictHostKeyChecking=no ${AWS_INSTANCE_USER}@${AWS_INSTANCE_IP} 'sudo docker run -d --rm -p 80:80  ${DOCKER_IMAGE_NAME}:latest'"
                    }
                }
            }
        }
    }
}