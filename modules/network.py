import urllib.request


def get(url):

    try:
        response = urllib.request.urlopen(
            url,
            timeout=10
        )

        data = response.read().decode(
            "utf-8",
            errors="ignore"
        )

        print(data)

    except Exception as e:

        print("[GI Network Error]", e)
