import azure.functions as func
import json
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.function_name(name="merakiWebhook")
@app.route(route="merakiWebhook")
@app.queue_output(arg_name="msg", queue_name="funcqueue", connection="AzureWebJobsStorage")
def merakiWebhook(req: func.HttpRequest, msg: func.Out[func.QueueMessage]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    
    if req.method == "GET":
        msg.set("string")
        return func.HttpResponse(body="string", status_code=200)
    
    elif req.method == "POST":
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            shared_secret = req_body.get('sharedSecret')

        if shared_secret:
            msg.set(json.dumps(req_body))
            return func.HttpResponse(body=json.dumps(req_body), headers=headers, status_code=200)
        else:
            return func.HttpResponse(
                "Please provide correct shared secret",
                status_code=401
            )