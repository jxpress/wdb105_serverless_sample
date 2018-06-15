import base64
import json

def lambda_handler(event, context):
    output = []

    for record in event['records']:
        # Base64形式の文字列をデコードする
        data = base64.b64decode(record['data'])
        # デコードしたJSONをdict型にロードする
        payload = json.loads(data)
        # Firehoseが受け取った時刻をcreated_atとして追加
        created_at = record['approximateArrivalTimestamp']
        # ミリ秒で定義されているので、秒単位に戻す
        payload['created_at'] = created_at / 1000
        # dict型のデータをJSONにシリアライズする
        payload = json.dumps(payload).encode('utf-8')
        # レコードの区切りのため、改行を追加
        payload += b'\n'
        # JSONをBase64形式にする
        data = base64.b64encode(payload).decode('utf-8')
        output_record = {
          'recordId': record['recordId'],
          'result': 'Ok',
          'data': data
        }
        output.append(output_record)

    return {'records': output}
