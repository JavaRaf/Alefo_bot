from baixar_image import download_frame
from facebook import up_to_fb, publish_image_fb
from load_ids import save_ids_to_txt
from add_captions import legendar
from env import data

def enviar_frame_to_fb(frame, captions, id):
    
    path = download_frame(frame)
    
    if data.MESSAGE_FRAME_NOT_FOUND in path:
        status_code = publish_image_fb('', id, data.MESSAGE_FRAME_NOT_FOUND)
        if status_code == 200:
            print('comentario de ajuda enviado')
            save_ids_to_txt(id)
       
    elif 'frame' in path:
        
        link = f'https://raw.githubusercontent.com/{data.REPO_OWNER}/{data.REPO_FRAMES_NAME}/{data.GITHUB_FRAMES_BRANCH}/{data.PASTA_FRAMES}/frame_{frame}.jpg'
        
        if captions:
            path = legendar(path, captions)
            
        img_message = f'Filename: Frame {frame} \n\n Resolution: 1920x1080 \n Link: {link}'
        
        if link:
            foto_id = up_to_fb(path)
            if foto_id:
                status_code = publish_image_fb(foto_id, id, img_message)
                if status_code == 200:
                    print('imagem enviada, comentario respondido')
                    save_ids_to_txt(id)
