import requests
import platform
import datetime
import subprocess
import os

URL_CHAVES = "https://raw.githubusercontent.com/Xaucutin/chaves-guiapp/refs/heads/main/chaves.json?token=GHSAT0AAAAAADDWHDLKCB62MP6OVACGFFCQ2BBFRJA"

def validar_chave(chave_usuario):
    try:
        dados = requests.get(URL_CHAVES).json()
        if chave_usuario not in dados:
            print("❌ Chave inválida.")
            return False

        chave_info = dados[chave_usuario]
        nome_pc = platform.node()

        if chave_info["pc"] != nome_pc:
            print("❌ Este PC não está autorizado.")
            return False

        validade = datetime.datetime.strptime(chave_info["expira"], "%Y-%m-%d")
        if datetime.datetime.now() > validade:
            print("❌ Chave expirada.")
            return False

        return True

    except Exception as e:
        print(f"Erro ao validar: {e}")
        return False

chave = input("🔑 Digite sua chave de acesso: ")

if validar_chave(chave):
    print("✅ Acesso liberado.")
    subprocess.Popen(["GuiKey V3.exe"])
else:
    input("Acesso negado. Pressione Enter para sair.")
