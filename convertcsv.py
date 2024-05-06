import os

# Pasta de origem e pasta de saída
input_folder = './results/pop909/omnizart_csv'
output_folder = './results/pop909/omnizart_lab'

# Verifica se a pasta de saída existe, se não, a cria
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Itera sobre os arquivos na pasta de origem
for filename in os.listdir(input_folder):
    # Lê o arquivo 
    csv_path = os.path.join(input_folder, filename)
    output_filename = os.path.splitext(filename)[0] + '.lab'
    output_path = os.path.join(output_folder, output_filename)
   
    with open(csv_path,'r') as file:
        with open(output_path,'w') as lab:
            for line in file:
                if line.startswith('chord,start,end'):
                    continue
                chord, start, end = line.strip().split(',')
                lab.write(f"{start} {end} {chord}\n")
    print(f"Arquivo {output_filename} criado")
    
   
    