import argparse
import getpass
import requests


parser = argparse.ArgumentParser()
parser.add_argument("user", help="Input GITHUB username repos owner")
parser.add_argument("repo", help="Input GITHUB repo")
parser.add_argument("pulln", help="Input pull number", type=int)
parser.add_argument("--version", help="Script version", action="store_true")
parser.add_argument("--ca", help="When it was created", action="store_true")
parser.add_argument("--t", help="PR title", action="store_true")
parser.add_argument("--ms", help="State of merge", action="store_true")
parser.add_argument("--l", help="Is PR locked or not", action="store_true")
parser.add_argument("--rid", help="ID repo", action="store_true")
args = parser.parse_args()
u = input('Please enter your GITHUB username: ')
p = getpass.getpass()
q = 'https://api.github.com/repos/' + args.user + "/" + args.repo
r = requests.get(str(q) + '/pulls/' + str(args.pulln), auth=(u, p))
x = r.json()
if args.version:
    print("Version 1.0")
if args.ca:
    print('Created at:', x['created_at'])
if args.t:
    print('PR title:', x['title'])
if args.ms:
    print('State of merge:', x['mergeable_state'])
if args.l:
    print('PR locked:', x['locked'])
if args.rid:
    print('Repo ID:', x['base']['repo']['id'])
