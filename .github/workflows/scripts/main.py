import sys
import time

def main():
    commits = sys.argv[1].split(',')
    for commit in commits:
        if commit:
            author, message = commit.split('::', 1)
            print(f"Processing commit by {author}")
            print(f"Message: {message}")
            time.sleep(1)

if __name__ == "__main__":
    main()
