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

// pipeline
// {
//     agent 
//     {
//       label  'slave1'
//     }
//     stages
//     {
//         stage('node check')
//         {
//             steps
//             {
//                 echo "Running on master node"
//                 sh 'hostname'
//             }
//         }
//     }
// }

pipeline {

    agent any

    parameters {

        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')

        text(name: 'BIOGRAPHY', defaultValue: '', description: 'Enter some information about the person')

        booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')

        choice(name: 'CHOICE', choices: ['One', 'Two', 'Three'], description: 'Pick something')

        password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')
    }

    stages {

        stage('Greeting') {
            steps {
                echo "Hello ${params.PERSON}"
            }
        }

        stage('Biography') {
            steps {
                echo "Biography entered:"
                echo "${params.BIOGRAPHY}"
            }
        }

        stage('Boolean Check') {
            steps {
                script {
                    if (params.TOGGLE) {
                        echo "Toggle is ON"
                    } else {
                        echo "Toggle is OFF"
                    }
                }
            }
        }

        stage('Choice Selection') {
            steps {
                echo "You selected option: ${params.CHOICE}"
            }
        }

        stage('Password Usage') {
            steps {
                echo "Password length is: ${params.PASSWORD.length()}"
            }
        }

    }
}


