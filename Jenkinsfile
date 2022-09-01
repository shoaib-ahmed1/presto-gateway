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
        stage('RunDummyQueries') {

            steps {
                waitUntil(initialRecurrencePeriod: 15000) {
                    script {
                            def res = sh(returnStdout: true, script: 'python3 run_dummy_queries.py ${clusterHost} ${port}')
                            echo "res: $res"
                            if ( res == "True") {
                                println("waiting for coordinator to respond")
                                return false
                            }else {
                                println("coordinator is responding...")
                                return true
                            }
                        }
                }
            }
         }
         stage('DeactivateBackend') {

            steps {
       
               sh """curl -s -X POST http://presto-gateway-container:8090/gateway/backend/deactivate/${clusterName}"""
            }
         }
      stage('totalRunningQueries') {

            steps {
                waitUntil(initialRecurrencePeriod: 15000) {
                    script {
                        def res = sh(returnStdout: true, script: 'python3 totalRunningQueries.py')
                        int totalRunningQueriesVar = res as Integer
                        echo "$totalRunningQueriesVar"
                        if ( totalRunningQueriesVar <= 1) {
                            return true
                        }else {
                            println("waiting for running queries to stop!")
                            return false
                        }
                    }
                }
            }
         }
    }
}
