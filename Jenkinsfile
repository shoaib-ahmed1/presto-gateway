pipeline {
    agent any

    stages {
        stage('AddNewBackend') {

            steps {
       
               sh """curl -s -X POST \'http://presto-gateway-container:8090/entity?entityType=GATEWAY_BACKEND\' -d \'{"name": "${clusterName}", "proxyTo": "http://${clusterHost}:${port}", "active": true, "routingGroup": "adhoc"}\' """
       
            }
         }
        stage('RunDummyQueries') {

            steps {
                waitUntil(initialRecurrencePeriod: 15000) {
                    script {
                            def response = sh(returnStdout: true, script: 'python3 run_dummy_queries.py ${clusterHost} ${port}')
                            echo "response: $response"
                            // True = atleast one query failed to execute
                            // False = no query failed to execute. all is well
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
         stage('DeactivateOldBackend') {

            steps {
       
               sh """curl -s -X POST http://presto-gateway-container:8090/gateway/backend/deactivate/${clusterName}"""
            }
         }
      stage('TotalRunningQueriesOldBackend') {

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
