pipeline{
    stages{
        stage('Stage1'){
            steps{
                echo "This is the stage 1"
            }
        }
        stage('stage2'){
            steps{
                echo "This is the stage 2"
            }
        }
    }
}