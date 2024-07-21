from env import data
import httpx



def up_to_fb(path_to_img: str): 
    
    retries = 0
    max_retries = 3
    
    while retries < max_retries:
        try:
            # Verificar se o caminho fornecido está correto
            with open(f'{path_to_img}', 'rb') as frame:
                files = {'file': (path_to_img, frame, 'image/jpeg')}
                
                dados = {
                    'published': 'false',
                    'access_token': data.FB_TOKEN
                }
                
                response = httpx.post(f'{data.fb_url}/me/photos', files=files, data=dados, timeout=10)
                
                if response.status_code == 200:
                    foto_id = response.json().get('id')
                    if foto_id:
                        return foto_id
                else:
                    print(f'Erro ao fazer upload: {response.status_code}, {response.text}')
                    retries += 1
            
        except FileNotFoundError:
            print(f'Arquivo {path_to_img} não encontrado')
            return ''
        except Exception as e:
            print(f'Ocorreu um erro: {e}')
            return ''
    

def publish_image_fb(foto_id: str, id_comentario: str, message: str):
    retries = 0
    max_retries = 3
    
    while retries < max_retries:
        
        dados = {
            'message': message,
            'attachment_id': foto_id,
            'access_token': data.FB_TOKEN
        }
        response = httpx.post(f'{data.fb_url}/{id_comentario}/comments', data=dados, timeout=12)
    
        if response.status_code == 200:
            return response.status_code
        else:
            print('erro ao enviar a imagem pro fb', response.status_code, response.text)
            retries += 1

    return response.status_code