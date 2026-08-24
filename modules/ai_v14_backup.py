import urllib.request
import json


SERVER="http://127.0.0.1:8080/completion"


def ask(prompt):

    data = {
        "prompt": prompt,
        "n_predict": 128
    }

    try:

        req = urllib.request.Request(
            SERVER,
            data=json.dumps(data).encode(),
            headers={
                "Content-Type":"application/json"
            }
        )

        response = urllib.request.urlopen(req)

        result=json.loads(
            response.read()
        )

        print(
            result.get("content","")
        )


    except Exception as e:

        print("[GI AI Error]", e)
