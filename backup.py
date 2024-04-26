import pathlib, subprocess


def backup(caminho_origem, caminho_backup, pasta_excluir):

    print("Executando o backup!!")
    
    comando_bkp = ["rsync", "-av", "--exclude", pasta_excluir, caminho_origem, caminho_backup]

    subprocess.run(comando_bkp)


    print("backup efetuado com sucesso!!")



if __name__ == "__main__":

    caminho_backup = str(pathlib.Path.home() / 'backups')

    caminho_origem = str(pathlib.Path.home())
    
    pasta_excluir = "backups/"

    backup(caminho_origem, caminho_backup, pasta_excluir)
