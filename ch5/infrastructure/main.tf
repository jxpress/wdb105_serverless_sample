provider "aws" {}

terraform {
  backend "s3" {
    bucket = "S3のバケット名"
    key    = "terraform.tfstate"
    region = "ap-northeast-1"
  }
}

resource "aws_dynamodb_table" "new" {
  name = "serverless-table-v1"
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "foo"

  attribute {
    name = "foo"
    type = "S"
  }
}

resource "aws_dynamodb_table" "old" {
  name = "serverless-table-v0"
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "foo"

  attribute {
    name = "foo"
    type = "S"
  }
}

resource "aws_dynamodb_table" "old" {
  name = "serverless-table-v0"
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "foo"

  attribute {
    name = "foo"
    type = "S"
  }

  # 以下を追記
  stream_enabled   = true
  stream_view_type = "NEW_IMAGE"
}

# トリガの設定を追加
resource "aws_lambda_event_source_mapping" "old_trigger" {
  enabled           = true
  batch_size        = 100
  event_source_arn  = "${aws_dynamodb_table.old.stream_arn}"
  function_name     = "${apex_function_sync}:current"
  starting_position = "LATEST"
}
