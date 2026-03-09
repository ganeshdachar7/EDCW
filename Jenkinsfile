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
// pipeline 
// {
//     agent any 
//     stages 
//     {
//         stage('System Info')
//         {
//             steps
//             {
//                 sh '''
//                 whoami
//                 uname -a
//                 '''
                
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
    agent 
    {
      label  'Slave1'
    }
    stages
    {
        stage('node check')
        {
            steps
            {
                echo "Running on master node"
                sh 'hostname'
            }
        }
    }
}

