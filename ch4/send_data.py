import json
import uuid
import boto3
# boto3をFirehose用に初期化する
firehose = boto3.client('firehose')
# 例として、3人のユーザーのログデータを送る
firehose.put_record(
    DeliveryStreamName='wdp_firehose',
    # 任意の形式のデータを送れますが、ここではJSON形式にしています
    Record={
        'Data': b'{"user_id": "a", "event": "session"}\n'
    }
)
firehose.put_record(
    DeliveryStreamName='wdp_firehose',
    Record={
        'Data': b'{"user_id": "b", "event": "install"}\n'
    }
)
firehose.put_record(
    DeliveryStreamName='wdp_firehose',
    Record={
        'Data': b'{"user_id": "c", "event": "click"}\n'
    }
)
