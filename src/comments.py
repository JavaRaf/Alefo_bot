import httpx
from time import sleep
from env import data
from os import environ

def get_comments():
    ids = []
    comments = []
    
    dados = {'fields': 'comments.limit(100)', 'limit': '100', 'access_token': data.FB_TOKEN}
    try:
        
        while data.init < data.max:
            response = httpx.get(f'{data.fb_url}/{environ.get("PAGE_ID")}/posts/', params=dados, timeout=12)
            if response.status_code == 200:
                response_data = response.json()
                
                if isinstance(response_data, dict):  # Verifica se a resposta é um dicionário
                    for item in response_data.get('data', []):
                        comments_data = item.get('comments', {}).get('data', [])
                        if len(comments_data) >= 1:
                            for comment in comments_data:
                                if 'id' in comment:
                                    comments.append(comment.get('message'))
                                    ids.append(comment.get('id'))
                    
                    # Check for pagination
                    if 'paging' in response_data and 'next' in response_data['paging']:
                        after = response_data['paging']['cursors'].get('after', '')
                        dados['after'] = after
                        data.init += 1
                    else:
                        break
                else:
                    print("Unexpected response format")
                    break
            else:
                print(f"Failed to get posts: {response.status_code}")
                break
            
            sleep(1)
              
    except httpx.RequestError as exc:
        print(f"HTTP error occurred: {exc}")
    except Exception as exc:
        print(f"An error occurred: {exc}")
                
    data.init = 0
    return ids, comments


