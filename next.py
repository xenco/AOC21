import os
import sys
import urllib.request

from dotenv import load_dotenv


def main():
    load_dotenv()

    if not os.getenv("session"):
        print("Make sure to include a .env file containing a single key SESSION=[your session cookie]")
        raise SystemExit

    if len(sys.argv) < 2:
        print("Missing challenge number\nUsage: %s challenge_number" % sys.argv[0])
        raise SystemExit

    challenge_number = str(sys.argv[1])
    path = os.getcwd() + "/" + challenge_number + "/"
    input_name = "input"

    # create challenge dir
    if not os.path.exists(challenge_number):
        os.makedirs(challenge_number)

    # get challenge input
    req = urllib.request.Request(
        "https://adventofcode.com/2021/day/%s/input" % challenge_number,
        headers={
            "Cookie": "session=%s" % os.getenv("session")}
    )

    input_text = urllib.request.urlopen(req, timeout=15).read().decode("utf-8")
    if not os.path.exists(path + input_name):
        with open(os.getcwd() + "/" + challenge_number + "/input", "w") as f:
            f.write(input_text)
            f.close()

        with open(os.getcwd() + "/" + challenge_number + "/input_example", "w") as f:
            f.close()

    # create 1.py file
    if not os.path.exists(path + "1.py"):
        with open(path + "1.py", "w") as f:
            f.write("#!/usr/bin/python3\n\nwith open(\"input_example\") as f:\n\tfor line in f.readlines():\n\t\tpass")
            f.close()
        os.system("chmod +x " + path + "1.py")

    if not os.path.exists(path + "2.py"):
        with open(path + "2.py", "w") as f:
            f.write("#!/usr/bin/python3\n\nwith open(\"input_example\") as f:\n\tfor line in f.readlines():\n\t\tpass")
            f.close()
        os.system("chmod +x " + path + "2.py")


if __name__ == '__main__':
    main()
