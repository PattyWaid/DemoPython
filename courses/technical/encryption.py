#from colour.models import Category
from string import maketrans
import string

def do_encryption(token):
    secret_key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    encrypt="QWERTYUIOPLKJHGFDSAZXCVBNM1234567890@#$%~&|?/qwertyuioplzxcvbn"

    
    #Encryption
    encrypted_table = string.maketrans(secret_key,encrypt) #can have anything in the ""
    enc_token = token.translate(encrypted_table)

    return enc_token
