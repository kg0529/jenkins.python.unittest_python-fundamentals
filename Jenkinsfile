// Powered by Infostretch 

timestamps {

node () {

	stage ('Python_Sample - Checkout') {
 	 checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/kg0529/jenkins.python.unittest_python-fundamentals.git']]]) 
	}
	stage ('Python_Sample - Build') {
		powershell label: '', script: 'python -m unittest discover -s ./src/test/ -p \'*_test.py\''
 	

	}
}
}