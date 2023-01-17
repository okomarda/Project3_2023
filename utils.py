import json

file_json = "posts.json"
file_json_com = "comments.json"

def load_posts(file_json) :
    '''Передача данных файла json в список'''
    with open (file_json, 'r', encoding='utf-8') as file :
        posts = json.load (file)
    for post in posts:
        posts

    return posts

def load_comments(file_json_com) :
    '''Передача данных файла json в список'''
    with open (file_json_com, 'r', encoding='utf-8') as file :
        comments = json.load (file)
    return comments

def get_posts_by_user(poster_name) :
    '''Поиск постов по выбранному имени пользователя'''
    posts_user = []
    posts = load_posts (file_json)
    for post in posts :
        if poster_name.lower ( ) in post['poster_name'].lower ( ) :
            posts_user.append (post)
    return posts_user

def get_comments_by_post_id(post_id):
    '''Возвращает комментарии к посту по его номеру'''
    comments_by_id = []
    comments = load_comments(file_json_com)
    for comment in comments:
        if int(post_id) == int(comment['post_id']):
            comments_by_id.append(comment)
    #return comments_by_id
    return comments_by_id


def search_by_posts(key_word) :
    '''Поиск постов по ключевому слову'''
    posts_select = []
    posts = load_posts (file_json)
    for post in posts :
        if key_word.lower ( ) in post['content'].lower ( ) :
            posts_select.append (post)
    return posts_select

def search_posts_by_heshteg(heshteg):
    '''Поиск постов по хештегу'''
    posts_heshteg = []
    posts = load_posts(file_json)
    for post in posts:
        if ("#"+heshteg).lower( ) in post['content'].lower( ):
            posts_heshteg.append (post)
    return posts_heshteg

def get_list_of_heshteg(heshteg):
    '''Формирование списка хештегов'''
    heshtegs = []
    posts = load_posts(file_json)
    for post in posts:
        if ("#"+heshteg).lower( ) in post['content'].lower( ):
            heshtegs.append("#"+heshteg)
    return heshtegs

def get_posts_by_pk(pk):
    '''Возвращает пост по его идентификатору'''
    posts = load_posts(file_json)
    for post in posts:
        if int(pk) == int(post['pk']):
            return post

def wrap_to_link(tag):
    """
    Оборачивает тег в ссылку
    """
    return f"<a href='/tag/{tag}'>#{tag}</a>"


def get_tags(pk):
    '''Возвращает пост по его идентификатору'''
    words = []
    posts = load_posts(file_json)
    for post in posts:
        if int(pk) == int(post['pk']):
            for word in post['content'].split (" ") :
                if word[0] == "#" :
                    words.append (wrap_to_link (word[1 :]))
                else :
                    words.append (word)

            return " ".join (words)

#print(load_posts(file_json))
#print(('').join(list(posts[0]['content'][0:50])))
#print(search_by_posts("ага"))
#print(len(search_by_posts("ага")))
#print(get_posts_by_pk(3))
#print(get_posts_by_pk(1)[0]["views_count"])
#print(get_comments_by_post_id(1))