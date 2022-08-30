pipeline {
    agent any

    stages {
        stage('PrintClusterName') {
            steps {
                echo "Name: ${params.clusterName}"
            }
        }
        stage('AddBackend') {

            steps {
       
               sh """curl -s -X POST \'http://presto-gateway-container:8090/entity?entityType=GATEWAY_BACKEND\' -d \'{"name": "${clusterName}", "proxyTo": "http://${clusterHost}:${port}", "active": true, "routingGroup": "adhoc"}\' """
       
            }
         }
         stage('DeactivateBackend') {

            steps {
       
               sh """curl -s -X POST http://presto-gateway-container:8090/gateway/backend/deactivate/${clusterName}"""
            }
         }
      stage('totalRunningQueries') {
            timeout(5) {
                waitUntil {
                    script {
                        def r = sh script: 'python3 totalRunningQueries.py', returnStdout: true
                        return (r == 0);
                    }
                }
            }
         }
    }
}
