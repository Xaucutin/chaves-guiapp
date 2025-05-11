import uuid
import datetime
import json

chave = str(uuid.uuid4()) + "="
nome_pc = input("Nome do PC do comprador: ")
dias = int(input("Validade em dias: "))

expira = (datetime.datetime.now() + datetime.timedelta(days=dias)).strftime("%Y-%m-%d")

nova_entrada = {
    chave: {
        "pc": nome_pc,
        "expira": expira
    }
}

with open("chaves.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

dados.update(nova_entrada)

with open("chaves.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4)

print("✅ Chave criada:")
print(f"Chave: {chave}")
print(f"PC autorizado: {nome_pc}")
print(f"Expira em: {expira}")
