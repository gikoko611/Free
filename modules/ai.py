import urllib.request
import urllib.error
import json


SERVER = "http://127.0.0.1:8080"


def status():

    try:
        r = urllib.request.urlopen(
            SERVER + "/health",
            timeout=3
        )

        print("[GI AI] Server OK")

    except Exception as e:

        print("[GI AI] Server Offline")



def ask(prompt):

    url = SERVER + "/completion"

    data = {
        "prompt": prompt,
        "n_predict": 128,
        "temperature": 0.7
    }


    try:

        req = urllib.request.Request(
            url,
            data=json.dumps(data).encode(),
            headers={
                "Content-Type":"application/json"
            }
        )


        res = urllib.request.urlopen(
            req,
            timeout=60
        )


        result=json.loads(
            res.read()
        )


        print(
            result.get(
                "content",
                ""
            )
        )


    except urllib.error.HTTPError as e:

        print(
            "[GI AI HTTP Error]",
            e.code
        )


    except Exception as e:

        print(
            "[GI AI Error]",
            e
        )



def model():

    try:

        r=urllib.request.urlopen(
            SERVER + "/props",
            timeout=3
        )

        print(
            r.read().decode()
        )


    except:

        print(
            "[GI AI] Offline"
        )
