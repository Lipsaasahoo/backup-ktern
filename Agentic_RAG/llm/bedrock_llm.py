import boto3
import json

REGION = "us-east-1"
MODEL_ID = "google.gemma-3-4b-it"

client = boto3.client("bedrock-runtime", region_name=REGION)


def call_bedrock(prompt):
    body = {
        "input": prompt,
        "parameters": {
            "max_new_tokens": 512,
            "temperature": 0.5
        }
    }

    response = client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json"
    )

    result = json.loads(response["body"].read())
    return result.get("output", "")