from check_tokens import check_variaveis
from time import time, sleep
from os import environ
from comments import get_comments
from load_ids import check_ids
from commands import search_command



def run_script():
    if environ.get("PAGE_ID"):
        
        start = time()
        ids, messages = get_comments()
        
        end = time()
        print(f'-------------------------------------\nA busca por comentarios levou: {end - start:.2f} segundos\n----------------------------------')
        
        print(f'----------------------------------------------\nRemovendo ids respondidos\n---------------------------------------------------------')
        new_ids, new_comments = check_ids(ids, messages)
        
        print('------------------------------------------------\nVerificando comentarios \n\n--------------------------------------------------------')
        search_command(new_ids, new_comments)

        

def main():
    check_variaveis()
    
    start: float = time()
    while (time() - start) < (180 * 60):  # 3 hours
        
        run_script()
        
        sleep(50) # seconds

if __name__ == '__main__':
    main()