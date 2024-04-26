import psutil, pathlib, os, datetime

def bytes_para_gigas (valor):
    return valor / 1024 / 1024 / 1024


def monitorar_recursos(intervalo):
        data = datetime.date.today().strftime('%d/%m/%Y')


        uso_cpu = psutil.cpu_percent(interval=intervalo)
        freq_cpu = psutil.cpu_freq().current
        #A de sensor de temperatura e nem o de rpm das fans nao ira funcionar pois 
        #minha maquina nao possui o sensor nem no processador, 
        #mas deixarei o codigo em comentario
        #cpu_temp = psutil.sensors_temperatures()['coretemp'][0].current
        #sensor_fan = psutil.sensors_fans()
        uso_memoria = psutil.virtual_memory().percent
        uso_disco = psutil.disk_usage('/').percent
        disco_livre = psutil.disk_usage('/').free
        net_pacote_env = psutil.net_io_counters().packets_sent
        net_pacote_rec = psutil.net_io_counters().packets_recv
        numero_processos = len(psutil.pids())

        caminho = str(pathlib.Path.home() / 'registros' / 'info_maquina.txt')

        if os.path.exists(caminho):

            with open(caminho, 'a') as arquivo:

                arquivo.write("\nRelatório de monitoramento da maquina do dia: {}\n".format(data))
                arquivo.write("Uso da CPU: {}% \n".format(uso_cpu))
                arquivo.write("Frequencia atual da CPU: {:.2f} HZ \n".format(freq_cpu))
                arquivo.write("Uso de Memória: {}% \n".format(uso_memoria))
                arquivo.write("Uso de Disco: {}% \n".format(uso_disco))
                arquivo.write("Disco livre: {:.2f} GB \n".format(bytes_para_gigas(disco_livre)))
                arquivo.write("Pacotes de internet enviados: {}% \n".format(net_pacote_env))
                arquivo.write("Pacotes de internet recebidos: {}% \n".format(net_pacote_rec))  
                arquivo.write("Esta maquina estava com {} processos funcionando no dia {}!! \n \n".format(numero_processos, data))
        else:

            pasta = str(pathlib.Path.home() / 'registros')

            if not os.path.exists(pasta):
                os.makedirs(pasta)
                
            arquivo = str("info_maquina.txt")

            caminho_completo = os.path.join(pasta, arquivo)

            with open(caminho_completo, 'w') as arquivo:

                arquivo.write("\nRelatório de monitoramento da maquina do dia: {}\n".format(data))
                arquivo.write("\n Uso da CPU: {}% \n".format(uso_cpu))
                arquivo.write("Frequencia atual da CPU: {:.2f} HZ \n".format(freq_cpu))
                arquivo.write("Uso de Memória: {}% \n".format(uso_memoria))
                arquivo.write("Uso de Disco: {}% \n".format(uso_disco))
                arquivo.write("Disco livre: {:.2f} GB \n".format(bytes_para_gigas(disco_livre)))
                arquivo.write("Pacotes de internet enviados: {}% \n".format(net_pacote_env))
                arquivo.write("Pacotes de internet recebidos: {}% \n".format(net_pacote_rec)) 
                arquivo.write("Esta maquina estava com {} processos funcionando no dia {}!! \n \n".format(numero_processos, data))
                    


if __name__ == "__main__":
    intervalo = 1 #intervalo em segundos
    monitorar_recursos(intervalo)
