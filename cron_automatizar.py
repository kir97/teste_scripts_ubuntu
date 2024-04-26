import pathlib, subprocess

def colocar_no_cron():
    
    caminho_py = ("/usr/bin/python3") 

    caminho = (pathlib.Path().absolute())

    #A cada 2 minutos ele irá rodar o script de logins na maquina e irá acrescentar o relatório dentro
    #da pasta registros que ficará na home area do usuario em um arquivo chamado 'info_maquina.txt'

    comando_cron_1 = str("*/2 * * * * {} {}/monitorar_cpu.py".format(caminho_py,caminho))
    
    verificar_comando_1 = ("(crontab -l) | grep -qxF '{}'".format(comando_cron_1))

    resultado = subprocess.run(verificar_comando_1, shell=True)

    if resultado.returncode != 0:

        comando_1 = str("(crontab -l; echo '{}') | crontab -".format(comando_cron_1))
    
        subprocess.run(comando_1, shell=True)
    
        print("Script adicionado ao cron com Sucesso!!")

    else:
        print("O comando ja está presente neste cron. \nEntao o comando: \n\n{}\n\nNão sera adicionado.\n\n\n".format(comando_cron_1))

    #Todo dia as 20:00 Hrs ele irá rodar o script de logins na maquina e irá acrescenta o relatorio dentro
    #da pasta registros que ficara na home area do usuario em um arquivo chamado 'logins.txt'
    
    comando_cron_2 = str("0 20 * * * {} {}/entrada_na_maquina.py".format(caminho_py,caminho))
    
    verificar_comando_2 = ("(crontab -l) | grep -qxF '{}'".format(comando_cron_2))

    resultado = subprocess.run(verificar_comando_2, shell=True)

    if resultado.returncode != 0:

        comando_2 = str("(crontab -l; echo '{}') | crontab -".format(comando_cron_2))
    
        subprocess.run(comando_2, shell=True)
    
        print("Script adicionado ao cron com Sucesso!!")

    else:
        print("O comando ja está presente neste cron. \nEntao o comando: \n\n{}\n\nNão sera adicionado.\n\n\n".format(comando_cron_2))

    #todo dia as 20:00 Hrs da noite ele irá efetuar o script de backup criando uma pasta escrita backup
    #e irá salvar todos os arquivos e pastas que possui na home area do usuario e guardará na pasta 'backup' criada na
    #home area do usuario

    comando_cron_3 = str("0 20 * * * {} {}/backup.py".format(caminho_py,caminho))
    
    verificar_comando_3 = ("(crontab -l) | grep -qxF '{}'".format(comando_cron_3))

    resultado = subprocess.run(verificar_comando_3, shell=True)

    if resultado.returncode != 0:

        comando_3 = str("(crontab -l; echo '{}') | crontab -".format(comando_cron_3))
    
        subprocess.run(comando_3, shell=True)
    
        print("Script adicionado ao cron com Sucesso!!")

    else:
        print("O comando ja está presente neste cron. \nEntao o comando: \n\n{}\n\nNão sera adicionado.".format(comando_cron_1))






if __name__ == "__main__":
    colocar_no_cron()

