import pytest
import requests
import json

@pytest.fixture
def supply_url():
    return "https://reqres.in/api"

@pytest.mark.parametrize("userid, firstname", [(1,"cerulean"),(2,"fuchsia rose")])
def test_list_valid_users(supply_url, userid, firstname):
    url = supply_url + "/users" + str(userid)
    resp = requests.get(url)
    j = json.loads(resp.text)
    
    assert resp.status_code == 200, resp.text
    assert j['data'][userid-1]['id'] == userid, resp.text
    assert j['data'][userid-1]['name'] == firstname, resp.text

def test_list_invaliduser(supply_url):
    url = supply_url + "/users/50"
    resp = requests.get(url)
    assert resp.status_code == 404, resp.text

if __name__=='__main__':
    url = "https://reqres.in/api" + "/users" + str(1)
    resp = requests.get(url)
    j = json.loads(resp.text)
    print(j)
    print(j['data'][0]['name'])