import sys
import json
import time

def main():
    commits_json = sys.argv[1]
    commits = json.loads(commits_json)

    for commit in commits:
        author = commit['author']['email']
        message = commit['message']
        title, body = message.split('|', 1) if '|' in message else (message, "")
        print(f"Processing commit by {author}")
        print(f"Title: {title}")
        print(f"Body: {body}")
        time.sleep(1)

if __name__ == "__main__":
    main()
