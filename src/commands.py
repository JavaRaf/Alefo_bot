import re
from env import data
from send_frame_to_fb import enviar_frame_to_fb



def extract_frame(message, id):
    frame, captions = '', ''
    numero_frame = re.findall(r'\d+', message)

    numero = numero_frame[0]
    if numero:
        frame = numero
        
        if data.ADD_LEGENDA in message:
            result = re.findall(r'"(.*?)"', message)
            captions = ' '.join(result)
    
    enviar_frame_to_fb(frame, captions, id)      


        
             
def search_command(comments_ids, comments_messages):
      for id, message in zip(comments_ids, comments_messages):
          
            if message.lower().replace(' ', '').startswith(data.DOWNLOAD_MESSAGE) and re.findall(r'\d+', message):
                extract_frame(message, id)
                                 