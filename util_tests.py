import pytest
import json

file_json = "posts.json"
file_json_com = "comments.json"

from utils import load_posts, load_comments, get_posts_by_user, get_comments_by_post_id, get_posts_by_pk, search_by_posts


def test_load_posts() :
    with pytest.raises (TypeError) :
        load_posts (list)


def test_load_comments() :
    with pytest.raises (TypeError) :
        load_comments (list)

# TEST GET_BY_USER

test_parameter = [("leo", 2), ("hank", 2), ("johnny", 2), ("larry", 2)]
@pytest.mark.parametrize("test_input, expected", test_parameter )
def test_get_posts_by_user(test_input, expected):
    assert len(get_posts_by_user(test_input)) == expected

# TEST GET_BY_POST_ID

test_parameter = [(1, 4), (2, 4), (3, 4), (4, 4), (5, 2), (6, 1), (7, 1)]
@pytest.mark.parametrize("test_input, expected", test_parameter )
def test_get_comments_by_post_id(test_input, expected):
    assert len(get_comments_by_post_id(test_input)) == expected

# TEST GET_POSTS_BY_PK

test_parameter = [(1, 376), (2, 233), (3, 187), (4, 366), (5, 287), (6, 299), (7, 166), (8, 141)]
@pytest.mark.parametrize("test_input, expected", test_parameter )
def test_get_posts_by_pk(test_input, expected):
    assert get_posts_by_pk(test_input)[0]["views_count"] == expected

# TEST SEARCH_BY_POST
test_parameter = [("Ага, опять еда", 376), ("Вышел погулять днем", 233), ("Смотрите-ка – ржавые елки", 187), ("Утром проснулся раньше", 366), ("Пурр-пурр", 287), ("Вот обычная лампочка", 299), ("Очень красивый закат", 166), ("Утром отправились", 141)]
@pytest.mark.parametrize("test_input, expected", test_parameter )
def test_search_by_posts(test_input, expected):
    assert search_by_posts(test_input)[0]["views_count"] == expected








