from cryptography.fernet import Fernet

global MessageCrypter 
MessageCrypter = "Andriamasimanana Ny Hasina Finaritra"


# def encryptCF():
#     keys = Fernet.generate_key()
#     global fernet
#     fernet = Fernet(keys)
#     global msClaire
#     msClaire = fernet.encrypt(MessageCrypter.encode())

#     print(msClaire)


def encrypt() :
    key = 14
    acrypter = MessageCrypter.upper()
    lg = len(acrypter)
    global MessageCrypte
    MessageCrypte = ""

    for i in range(lg):
        if acrypter[i] == ' ':
            MessageCrypte+=' '
        else:
            asc = ord(acrypter[i])+key
            MessageCrypte += chr(asc+26*((asc<65)-(asc>90)))

    print (MessageCrypte)
    

encrypt()


def decrypt():
    lg = len(MessageCrypte)
    global MessageClair
    MessageClair = ""
    key=14

    for i in range(lg):
        if MessageCrypte[i]==' ':
            MessageClair+=' '
        else:
            asc = ord(MessageCrypte[i])-key
            MessageClair += chr(asc+26*((asc<65)-(asc>90)))

    print (MessageClair)


# def decryptCF():
#     global msClaireDec
#     msClaireDec = fernet.decrypt(MessageClair).decode()
#     print(msClaireDec)


# decryptCF()
decrypt()
