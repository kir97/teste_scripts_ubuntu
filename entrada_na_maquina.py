import datetime, subprocess, os, pathlib

def entrada_na_maquina ():

    data = datetime.date.today().strftime('%d/%m/%Y')
    
    comando_1 = ["last"]
    
    execucao_1 = subprocess.run(comando_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
    comando_2 = ["last", "reeboot"]
    
    execucao_2 = subprocess.run(comando_2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    caminho = str(pathlib.Path.home() / 'registros' / 'logins.txt')

    if os.path.exists(caminho):

        with open(caminho, 'a') as arquivo:
                
            arquivo.write("\n\n************************************************************")
            arquivo.write("\n\nRelatório de monitoramento de entrada da maquina do dia: {}\n\n".format(data)) 
            arquivo.write("************************************************************\n")
            arquivo.write("\n\n{} \n\n".format(execucao_1.stdout))
            arquivo.write("************************************************************\n")
            arquivo.write("************************************************************")
            arquivo.write("\n\nUltimas reinicializações feitas na maquina!!\n\n")
            arquivo.write("************************************************************\n")
            arquivo.write("************************************************************\n")
            arquivo.write("\n\n{} \n\n".format(execucao_2.stdout))  
            arquivo.write("\n************************************************************\n")
            arquivo.write("************************************************************\n\n\n")
    else:

        pasta = str(pathlib.Path.home() / 'registros')

        if not os.path.exists(pasta):
            os.makedirs(pasta)
                
        arquivo = str("logins.txt")

        caminho_completo = os.path.join(pasta, arquivo)

        with open(caminho_completo, 'w') as arquivo:

            arquivo.write("************************************************************")
            arquivo.write("\n\nRelatório de monitoramento de entrada da maquina do dia: {}\n\n".format(data)) 
            arquivo.write("************************************************************")
            arquivo.write("\n\n {} \n\n".format(execucao_1.stdout))
            arquivo.write("************************************************************\n")
            arquivo.write("************************************************************\n")
            arquivo.write("\n\nUltimas reinicializações feitas na maquina!!\n\n")
            arquivo.write("************************************************************\n")
            arquivo.write("************************************************************\n")
            arquivo.write("\n\n {} \n\n".format(execucao_2.stdout))  
            arquivo.write("************************************************************\n")
            arquivo.write("************************************************************\n\n\n")

if __name__ == "__main__":
    entrada_na_maquina()
