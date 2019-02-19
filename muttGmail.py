import argparse
import os 
import getpass
parser = argparse.ArgumentParser()
parser.add_argument("username", help="Gmail username: <username>.gmail.com")
parser.add_argument("name", help="Real user name. ex: \"John Doe\"")
parser.add_argument("--f", help="path for password file. Default: ~/.mutt/passwd.pgp")
args = parser.parse_args()
passwd = getpass.getpass('Gmail Password: ')
os.system("mkdir ~/.mutt/")
os.system("touch ~/.mutt/passwd")
os.system("""
echo "set imap_pass = {0}\n\
set smtp_pass = {0}" >> ~/.mutt/passwd
""".format(passwd))
os.system("gpg -r {}@gmail.com -e ~/.mutt/passwd".format(args.username))
os.system("shred ~/.mutt/passwd")
os.system("rm ~/.mutt/passwd")
os.system("cp muttrc .muttrc")
os.system( """
echo "set realname = {0}\n\
set from = {1}\n\
set smtp_url = "smtps://{1}@gmail.com@smtp.gmail.com:465/"\n\
set imap_user = "{1}@gmail.com"\n\
source \\"gpg -d ~/mutt.password.gpg\\" " >> .muttrc
""".format(args.name, args.username))

