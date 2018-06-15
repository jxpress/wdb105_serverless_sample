import boto3

client = boto3.client('dynamodb')

def handle(event, context):
    for rec in event['Records']:
        # DynamoDBストリーム以外のレコードは無視する
        if 'dynamodb' not in rec:
            continue
        
        # 登録・更新以外のレコードは無視する
        if 'NewImage' not in rec['dynamodb']:
            continue

        # レコードをそのまま新テーブルに登録する
        client.put_item(
            TableName='serverless-table-v1'
        )
