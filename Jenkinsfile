pipeline {
    agent any

    environment {
        IMAGE_NAME = "jhonny535/akash-web-app"
        AKASH_WALLET_NAME = credentials('AKASH_WALLET_NAME')
        AKASH_WALLET_MNEMONIC = credentials('AKASH_WALLET_MNEMONIC')
        AKASH_KEYRING_BACKEND = "test"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/jhonnyy3/akash_web_app'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DOCKERHUB_CREDS', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    bat 'echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }

        stage('Push Docker Image') {
            steps {
                bat 'docker push %IMAGE_NAME%'
            }
        }

        stage('Install Akash CLI') {
            steps {
                bat '''
                curl --ssl-no-revoke -LO https://github.com/akash-network/node/releases/download/v0.38.2/akash_0.38.2_Windows_x86_64.zip
                tar -xf akash_0.38.2_Windows_x86_64.zip
                move akash.exe C:\\Windows\\System32\\
                akash.exe version
                '''
            }
        }

        stage('Restore Wallet') {
            steps {
                bat '''
                echo %AKASH_WALLET_MNEMONIC% | akash.exe keys add %AKASH_WALLET_NAME% --recover --keyring-backend %AKASH_KEYRING_BACKEND%
                akash.exe keys list --keyring-backend %AKASH_KEYRING_BACKEND%
                '''
            }
        }

        stage('Validate Deployment') {
            steps {
                bat '''
                akash.exe tx deployment create deploy.yaml ^
                    --from %AKASH_WALLET_NAME% ^
                    --keyring-backend %AKASH_KEYRING_BACKEND% ^
                    --chain-id akashnet-2 ^
                    --node https://rpc.akash.forbole.com:443 ^
                    --dry-run
                '''
            }
        }

        stage('Deploy to Akash') {
            steps {
                bat '''
                akash.exe tx deployment create deploy.yaml ^
                    --from %AKASH_WALLET_NAME% ^
                    --keyring-backend %AKASH_KEYRING_BACKEND% ^
                    --chain-id akashnet-2 ^
                    --node https://rpc.akash.forbole.com:443 ^
                    --gas-prices 0.025uakt ^
                    --gas auto ^
                    --gas-adjustment 1.5 ^
                    -y
                '''
            }
        }
    }
}
