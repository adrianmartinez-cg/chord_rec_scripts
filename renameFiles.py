import os

# Defina o caminho da pasta onde os arquivos estão localizados
pasta = os.path.join(os.getcwd(),'pop909_expected')

# Itere sobre os arquivos na pasta
for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith('.txt'):
        # Extraia a parte numérica do nome do arquivo
        parte_numerica = nome_arquivo.split('_')[0]
        try:
            novo_nome = f"{parte_numerica}.lab"
            caminho_antigo = os.path.join(pasta, nome_arquivo)
            caminho_novo = os.path.join(pasta, novo_nome)
            os.rename(caminho_antigo, caminho_novo)
            print(f"Renomeado {nome_arquivo} para {novo_nome}")
        except ValueError:
            print(f"Pulando {nome_arquivo} (não está no formato esperado)")

print("Renomeação de arquivos concluída.")