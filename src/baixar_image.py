from env import data
import httpx
import os

def download_frame(FRAME) -> str:
    
    url = f'https://raw.githubusercontent.com/{data.REPO_OWNER}/{data.REPO_FRAMES_NAME}/{data.GITHUB_FRAMES_BRANCH}/{data.PASTA_FRAMES}/frame_{FRAME}.jpg'
    
    try:
        response = httpx.get(url)
        if response.status_code == 404:
            return f'{data.MESSAGE_FRAME_NOT_FOUND}'
        
        if response.status_code == 200:
            # Certifique-se de que a pasta images existe
            os.makedirs('images', exist_ok=True)
            with open(f'images/frame_{FRAME}.jpg', 'wb') as file:
                file.write(response.content)
            
            return f'images/frame_{FRAME}.jpg'
        
        else:
            print(f'Erro ao acessar o GitHub: {response.status_code}')
            print(response.text)  # Exibe o corpo da resposta para depuração
    except Exception as e:
        print(f'Erro durante a requisição HTTP: {str(e)}')