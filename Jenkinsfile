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
       
               sh """curl -s -X POST \'http://presto-gateway-container:8090/entity?entityType=GATEWAY_BACKEND\' -d \'{"name": "${clusterName}", "proxyTo": "http://${clusterName}.careem-engineering.com:8080", "active": true, "routingGroup": "adhoc"}\' """
       
            }
         }
         stage('DeactivateBackend') {

            steps {
       
               sh """curl -s -X POST http://presto-gateway-container:8090/gateway/backend/deactivate/${clusterName}"""
            }
         }
      stage('totalRunningQueries') {

            steps {
       
              dir('presto-gateway'){
                sh """
                totalRunningQueriesVar = python3 totalRunningQueries.py
                echo $totalRunningQueries
                """
              }
            }
         }
    }
}
