pipeline {
    agent {
        docker {
            image 'ubuntu:22.04'   // Uses Ubuntu as build environment
            args '-u root:root'    // Runs as root to install packages and use Docker
        }
    }

    environment {
        IMAGE_NAME = "jhonny535/akash-web-app"
        AKASH_WALLET_NAME = credentials('AKASH_WALLET_NAME')
        AKASH_WALLET_MNEMONIC = credentials('AKASH_WALLET_MNEMONIC')
        AKASH_KEYRING_BACKEND = "test"
    }

    stages {
        stage('Setup Tools') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y curl tar docker.io
                '''
            }
        }

        stage('Checkout') {
            steps {
                git 'https://github.com/jhonnyy3/akash-cicd-demo'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DOCKERHUB_CREDS', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $IMAGE_NAME'
            }
        }

        stage('Install Akash CLI') {
            steps {
                sh '''
                    curl -LO https://github.com/akash-network/node/releases/download/v0.38.2/akash_0.38.2_Linux_x86_64.tar.gz
                    tar -xzf akash_0.38.2_Linux_x86_64.tar.gz
                    mv akash /usr/local/bin/
                    akash version
                '''
            }
        }

        stage('Restore Wallet') {
            steps {
                sh '''
                    echo "$AKASH_WALLET_MNEMONIC" | akash keys add "$AKASH_WALLET_NAME" --recover --keyring-backend "$AKASH_KEYRING_BACKEND"
                    akash keys list --keyring-backend "$AKASH_KEYRING_BACKEND"
                '''
            }
        }

        stage('Validate Deployment') {
            steps {
                sh '''
                    akash tx deployment create deploy.yaml \
                    --from $AKASH_WALLET_NAME \
                    --keyring-backend $AKASH_KEYRING_BACKEND \
                    --chain-id akashnet-2 \
                    --node https://rpc.akash.forbole.com:443 \
                    --dry-run
                '''
            }
        }

        stage('Deploy to Akash') {
            steps {
                sh '''
                    akash tx deployment create deploy.yaml \
                    --from $AKASH_WALLET_NAME \
                    --keyring-backend $AKASH_KEYRING_BACKEND \
                    --chain-id akashnet-2 \
                    --node https://rpc.akash.forbole.com:443 \
                    --gas-prices 0.025uakt \
                    --gas auto \
                    --gas-adjustment 1.5 \
                    -y
                '''
            }
        }
    }
}

