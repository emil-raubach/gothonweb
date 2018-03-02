from nose.tools import *
from app import app
import flask
# Need to set the app.testing = True so that the exceptions propagate
# to the test client.  Otherwise the exception woudl be handled by the
# application (not visible to the test client) and the only indication
# of an AssertionError or other exception would be a 500 status code
# response to the test client.  The flask example code is:
#
#     app.testing = True
#     client = app.test_client()
#
# Not sure what Zed is doing with the .config() attribute of the app
# module.  Must investigate...
app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    #assert_equal(rv.status_code, 200)
    assert rv.status_code == 200 # using pytest syntax inplace of nosetest

    with app.test_request_context('/'):
        assert flask.request.path == '/'

def test_game():
    rv = web.get('/game', follow_redirects=True)
    # assert_equal(rv.status_code, 200)
    assert rv.status_code == 200 # using pytest sytax inplace of nosetest
    # assert_in(b"Gothons From Planet Percal #25", rv.data)
    assert b"Gothons From Planet Percal #25" in rv.data

def test_central_corridor_action():
    # can't run the 'shoot!' code and this one...
    data = {'action': 'tell a joke'}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert b"Laser Weapon Armory" in rv.data

# def test_central_corridor_shoot():
#     # make a test request to the test app (web), gving it an argument
#     # that simulates a death scene.
#     data = {'action': 'shoot!'}
#     rv = web.post('/game', follow_redirects=True, data=data)
#     assert b"Death" in rv.data

def test_laser_weapon_armory():
    data = {'action': '0132'}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert b"The Bridge" in rv.data

def test_the_bridge():
    data = {'action': 'slowly place the bomb'}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert b"Escape Pod" in rv.data

def test_escape_pod():
    data = {'action': '2'}
    rv = web.post('/game', follow_redirects=True, data=data)
    assert b"The End" in rv.data # both endings have the same title...
