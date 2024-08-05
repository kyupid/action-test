import sys
import json
import time

def main():
    commits_json = sys.argv[1]
    commits = json.loads(commits_json)
    print("메롱")

    for commit in commits:
        author = commit['author']['email']
        message = commit['message']
        print(f"Processing commit by {author}")
        print(f"Message: {message}")
        time.sleep(1)

if __name__ == "__main__":
    main()

