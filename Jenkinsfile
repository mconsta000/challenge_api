node {
   stage('Clone Repository') { 
      checkout scm
   }
   stage('Copy dependency') {
      git clone 'https://github.com/mconsta000/challenge_calc.git'
      copy(todir:"challenge") {
           fileset(dir:"../challenge_calc/challenge")
       }
   }
}