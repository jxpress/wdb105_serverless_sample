# coding: utf-8

import sys
import pathlib

# functions/serverless_wsgi/vendorに置いたライブラリを呼べるように
vendor_path = str(pathlib.Path('./vendor').absolute())
sys.path.append(vendor_path)

import awsgi

# 自作のプロジェクトパッケージを呼び出す
from serverless_wsgi.main import app


def lambda_handler(event, context):
    # appをAWSGIに渡す
    return awsgi.response(app, event, context)

