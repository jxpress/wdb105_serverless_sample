import os

import boto3
import pytest

# どのリージョンを利用するか環境変数から指定
dynamodb = boto3.resource('dynamodb', region_name=os.environ['AWS_DEFAULT_REGION'])

dynamodb = boto3.resource('dynamodb', endpoint_url=os.environ['DYNAMODB_ENDPOINT_URL'])


# 前処理・後処理でDynamoDBのテーブルの作成・削除を行うフィクスチャ
@pytest.fixture(scope='session', autouse=True)
def dynamodb_table():
    # DynamoDBの
    table = dynamodb.create_table(
                TableName='serverless-table-v1', KeySchema=[{
                    'AttributeName': 'foo', 'KeyType': 'HASH',
                }], AttributeDefinitions=[{
                    'AttributeName': 'foo', 'AttributeType': 'S'
                }], ProvisionedThroughput={
                    'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10
                })
    yield table
    table.delete()


# DynamoDBのテーブルに値を入れて取り出すテスト
def test_dynamodb_get_set_item(dynamodb_table):
    dynamodb_table.put_item(Item={'foo': 'bar'})
    res = dynamodb_table.get_item(Key={'foo': 'bar'})
    assert 'Item' in res
