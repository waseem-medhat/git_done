#! /usr/bin/python3

from git import Repo, GitCommandError
import sys

if len(sys.argv) < 2:
    print("No message given... exiting")
    sys.exit()
else:
    commit_msg = sys.argv[1]

repo = Repo(".")
repo.git.add("--all")

try:
    repo.git.commit("-m", commit_msg)
except GitCommandError:
    print("Nothing to commit... exiting")
    sys.exit()


print(f"added commit \"{commit_msg}\"")

try:
    origin = repo.remote()
    origin.push()
    print("Successfully pushed!")
except:
    print("Problem with pushing... exiting")
    sys.exit()
