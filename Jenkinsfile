 
//Jenkinsfile (Declarative Pipeline)

pipeline{
    agent any
    
    stages
    {
        //get a repository from a github
        stage("checkout a repo"){
            steps{
                echo "checkout a repo"
                git 'https://github.com/etianshahla03050/worldOfGames'
           }
        }
       
       //build an image from the dockerfile
        stage("build a container"){
            steps{
                echo "build a container"
                 sh("docker-compose build")

            }
        }
        
        //run a container and test the application
        stage("run a container"){
            steps{
                echo "run a container"
               
                sh('docker-compose up')
            }
            
        }
        
        //run test
        stage("e2e test"){
            steps{
            //    echo 'Waiting 30 sec for container deployment '
            //    sleep 30 // seconds
                echo "e2e test"
                sh("pip3 install -r requirements.txt")
                sh( "python e2e.py")
            }

        }
                
         // stop the container
        stage("finalize"){
            steps{
                echo "drop the container"
                
                sh( "docker stop worldofgames_world_of_games_1")
            }
            
            
        }

    }
}