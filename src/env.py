import os


class data:
  

    #m Mensages que vc precisa personalizar
    
    DOWNLOAD_MESSAGE = '!mikan' # comando princiapl do download
    ADD_LEGENDA = '-t' # adicione esse comando para uma legenda no topo da imagem
    
    
    MESSAGE_FRAME_NOT_FOUND = 'Desculpe nao encontrei o frame pedido' # messagem de frame nao encontrado
    
    
    # github
    REPO_FRAMES_NAME: str = 'bot'  # nome do repositorio onde estao os frames
    GITHUB_FRAMES_BRANCH: str = 'master' # branch dos frames
    PASTA_FRAMES = 'frames'
    
    # facebook
    fb_version: str = 'v20.0' # atualize caso a versão nao funcione mais. A ultima laçada foi a 20.0
    fb_url: str = f'https://graph.facebook.com/{fb_version}'
    
    #--------------------------------------------------------------------------------------------------------------------------------
    init = 0
    max = 6 # padrão 6, maximo recomendado 8. Essa opção controla a quantidade de posts que o bot vai olhar
    #--------------------------------------------------------------------------------------------------------------------------------

    # variaveis de ambiente, nao é preciso mexer aqui
    GIT_PAT: str = os.environ.get('GIT_PAT')  
    REPO_OWNER: str = os.environ.get('REPO_OWNER')  
    FB_TOKEN: str = os.environ.get('FB_TOKEN')