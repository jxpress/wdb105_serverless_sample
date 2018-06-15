#!/bin/bash

wget -O - https://s3-ap-northeast-1.amazonaws.com/dynamodb-local-tokyo/dynamodb_local_latest.tar.gz | tar zxvf -

java -Djava.library.path=. -jar DynamoDBLocal.jar -inMemory -port 8000
