import logging
from flask import Flask, request, render_template, jsonify
import json
from utils import load_posts, load_comments, get_posts_by_pk, get_comments_by_post_id, search_by_posts, get_posts_by_user
from utils import search_posts_by_heshteg, get_tags

file_json = "posts.json"
file_json_com = "comments.json"

app = Flask(__name__)
logging.basicConfig (filename = "./logs/api.log", level=logging.INFO, format=u'%(asctime)s [%(levelname)s] %(message)s', encoding='utf-8')
logger = logging.getLogger()

@app.route('/')
def get_posts():
    '''Загрузка главной страницы со списком постов'''
    try:
        posts = load_posts(file_json)
        len_posts=len(posts)
        return render_template('index.html', posts=posts, len_posts=len_posts)
    except:
        return "Файл json не найден, либо имеется ошибка в файле html"

@app.route('/search_form')
def search_page():
    '''Загрузка страницы поиска'''
    try:
        return render_template('search.html')
    except:
        return "Имеется ошибка в файле html: файл не найден или допущена ошибка в названии"

@app.route('/post/<pk>')
def get_post_commemts__by_pk(pk):
    '''Загрузка страницы с постом по его идентификатору'''
    try:
        post = get_posts_by_pk(pk)
        comments = get_comments_by_post_id(pk)
        len_comments = len(comments)
        content = get_tags(pk)
        return render_template("post.html", post = post, comments=comments, len_comments=len_comments, content=content)
    except:
        return "Файл html c таким названием не существует, либо проверьте еще раз содержание файла html"

@app.route('/search_form/search_results')
def search_posts():
    '''Выгрузка страницы с результами поиска по ключевым словам'''
    try:
        key_word = request.args.get('s', 'нет страницы для поиска')
        posts_searched = search_by_posts(key_word)
        len_posts_searched = len(posts_searched)
        return render_template("search.html", posts_searched = posts_searched,key_word=key_word, len_posts_searched=len_posts_searched)
    except:
        return "Файл html c таким названием не существует, либо проверьте еще раз содержание файла html"

@app.route('/users/<user_name>')
def get_post_user(user_name):
    '''Выгрузка страницы по имени пользователя'''
    try:
        posts = get_posts_by_user(user_name)
        return render_template("user-posts.html", posts = posts, poster_name=user_name)
    except:
        return "Файл html c таким названием не существует, либо проверьте еще раз содержание файла html"

@app.route('/tag/<heshteg>')
def get_post_heshteg(heshteg):
    '''Выгрузка страницы с постами, имеющими одинаковые хештеги'''
    try:
        posts = search_posts_by_heshteg(heshteg)
        return render_template("tag.html", posts = posts, heshteg=heshteg)
    except:
        return "Файл html c таким названием не существует, либо проверьте еще раз содержание файла html"

@app.errorhandler(404)
def page_not_found(e):
    '''Проверка на наличие ошибки 404'''
    return (f"ошибка 404: искомая страница не найдена")

@app.errorhandler(500)
def internal_error(e):
    '''Проверка на наличие ошибки 500'''
    return (f"ошибка 500: проблема на стороне сервера")

@app.route("/api/posts")
def get_json():
    '''Выгрузка страницы, отражающая все посты в формате json'''
    logger.info("Эндпоинт по всем постам запущен", )
    posts = load_posts(file_json)
    return jsonify(posts)


@app.route("/api/posts/<pk>")
def get_json_by_pk(pk):
    '''Выгрузка страницы с постом по идентификатору в формате json'''
    logger.info("Эндпоинт по номеру поста запущен")
    posts = load_posts(file_json)
    for post in posts:
        if int(pk) == int(post['pk']):
            return jsonify(post)


app.run (debug=True)


