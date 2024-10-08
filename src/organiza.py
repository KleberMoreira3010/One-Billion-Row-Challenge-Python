
import os


# Pegar nome dos arquivios
# pegar a extensdão do arquivo, para determinar o tipo
# Criar as pastas (Documentos, videos, imagens, vídeos e outros)
# Mover arquivos


audio = ['.mp3', '.wav']
videos =['.mp4', '.moov', '.avi']
imagens =['.jpg', '.jpeg', '.png']
documento =['.txt', '.pdf', '.doc', '.docx']




def pegar_extensao(nome):
    index = nome.rfind('.')
    return nome[index:]


def organizar(diretorio):
    AUDIO_DIR = os.path.join(diretorio,"audios")
    IMAGENS_DIR = os.path.join(diretorio,"imagens")
    DOC_DIR = os.path.join(diretorio,"documentos")
    VIDEOS_DIR = os.path.join(diretorio,"videos")    
    OUTROS_DIR = os.path.join(diretorio,"outros")

    if not os.path.isdir(AUDIO_DIR):
        os.mkdir(AUDIO_DIR)
    if not os.path.isdir(IMAGENS_DIR):
        os.mkdir(IMAGENS_DIR)
    if not os.path.isdir(DOC_DIR):
        os.mkdir(DOC_DIR)
    if not os.path.isdir(VIDEOS_DIR):        
        os.mkdir(VIDEOS_DIR)
    if not os.path.isdir(OUTROS_DIR):  
        os.mkdir(OUTROS_DIR)


    nomes_arquivos = os.listdir(diretorio)
    nova_pasta=''
    for arquivo in nomes_arquivos:
        if os.path.isfile(os.path.join(diretorio, arquivo)):
        #extensao dos arquivos com letras minusculas
            extensao = str.lower(pegar_extensao(arquivo))
            print(arquivo, extensao)
            if extensao in videos:
                nova_pasta=AUDIO_DIR
            elif extensao in videos:
                nova_pasta=VIDEOS_DIR
            elif extensao in documento:
                nova_pasta =DOC_DIR
            elif extensao in imagens:
                nova_pasta=IMAGENS_DIR
            else:
                nova_pasta=OUTROS_DIR                
        velho=os.path.join(diretorio, arquivo)
        novo=os.path.join(nova_pasta, arquivo)
        os.rename( velho,novo )
        print("Moveu" ,velho, "-->", novo)

if __name__ =='__main__':
    organizar('C:\\users\\Kleber\\Downloads')
