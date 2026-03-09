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

// pipeline 
// {
//     agent any 
//     stages{
//         stage('Build')
//         {
//             steps{
//                 echo "Building application"
//             }
//         }
//         stage('Test')
//         {
//             steps
//             {
//                 echo "Testing application"
//             }
//         }
//         stage('Deloy')
//         {
//             steps
//             {
//                 echo "Deploying application"   
//             }
//         }

//     }
// }

<<<<<<< HEAD
// pipeline 
// {
//     agent any 
//     stages 
//     {
//         stage('System Info')
//         {
//             steps
//             {
//                 sh{

//                 whoami
//                 uname -a
//                 }
=======
pipeline 
{
    agent any 
    stages 
    {
        stage('System Info')
        {
            steps
            {
                sh '''
                whoami
                uname -a
                '''
>>>>>>> e62fc6855b5165d403ed292ca6ff142481bb21b5
                
//             }
//         }
//         stage('Check Files')
//         {
//             steps
//             {
//                 sh{
//                      pwd
//                 ls -lrt
//                 }
               
//             }
//         }
//     }
// }

pipeline
{
    agent slave1
    stages
    {
        stage('node check')
        {
            steps
            {
<<<<<<< HEAD
                echo "Running on master node"
                sh 'hostname'
=======
                sh '''
                     pwd
                ls -lrt
                '''
>>>>>>> e62fc6855b5165d403ed292ca6ff142481bb21b5
            }
        }
    }
}

