from requests import get
import sys
import os

if __name__ == "__main__":
    if os.path.isdir("favicons") == False:
        os.mkdir("favicons")

    resp = get("https://{}/favicon.ico".format(sys.argv[1]))
    if resp.status_code == 200:
        with open("favicons/{}_favicon.ico".format(sys.argv[1]), "wb") as f:
            f.write(resp.content)

    else:
        print("Host doesn't found")
