// pipeline {
//     agent any

//     stages {

//         stage('Build') {
//             steps {
//                 echo 'Building application'
//                 sh 'date'
//             }
//         }

//         stage('Test') {
//             steps {
//                 echo 'Running tests'
//                 sh 'whoami'
//             }
//         }

//         stage('Deploy') {
//             steps {
//                 echo 'Deploying application'
//             }
//         }

//     }
// }

pipeline 
{
    agent any 
    stages{
        stage('Build')
        {
            steps{
                echo "Building application"
            }
        }
        stage('Test')
        {
            steps
            {
                echo "Testing application"
            }
        }
        stage('Deloy')
        {
            steps
            {
                echo "Deploying application"   
            }
        }

    }
}