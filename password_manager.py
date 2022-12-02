from cryptography.fernet import Fernet

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f: #automatically closes file "with"
        #'a' for add - 'r' for read 'w' for write 
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: #write in bytes mode
        key_file.write(key)
'''

while True:
    mode = input("Would you like to add a new password or view existing ones? (view, add) Press q to quit. ").lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode. ")
        continue
