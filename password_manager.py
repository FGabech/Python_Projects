from cryptography.fernet import Fernet #pip install cryptography

"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: #wb - write in bytes
        key_file.write(key)
write_key()# fazemos isso para conseguir a chave de criptografia"""

def load_key():
    file = open("key.key", "rb") #rb - read bytes
    key = file.read()
    file.close() #importante fechar o arquivo toda vez que abrimos
    return key

key = load_key()
fer = Fernet(key)#inicializando o modulo de encriptografia

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|") #o data. split retorna os valores em formato de lista dividindo os textos em listas 
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f: #o with é para uma vez que terminamos de utilizar o codigo ele fecha automaticamente // depois do nome do arquivo podemos ter diversas letras, o w é para rescrever, ou seja deleta tudo e salva algo em cima, o r é para ler o arquivo, e o a é para adicionar algo para o arquivo existente e caso o arquivo não exista nos criamos um arquivo novo.  
        f.write(name + "| " + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit?").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue