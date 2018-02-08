from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere

app = Flask(__name__)

@app.route("/")
def index():
    # this is used to "setup" the session with starting values
    session['room_name'] = planisphere.START
    return redirect(url_for("game"))

@app.route("/game", methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name') # sets the room name to the first room

    if request.method == 'GET':
        if room_name:
            # what does this do?
            print(">>> room_name=", room_name)
            room = planisphere.load_room(room_name)
            print(">>> room=", room, " and its type is ", type(room))
            return render_template("show_room.html", room=room)
        else:
            # why is there here? do you need it?
            print(">> When does this logic happen?", room, " type", type(room))
            return render_template("show_room.html", room=room)
    else:
        print("***Starting a POST request.***")
        action = request.form.get('action')

        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)

            if not next_room:
                session['room_name'] = planisphere.name_room(room)
            else:
                session['room_name'] = planisphere.name_room(next_room)

        return redirect(url_for("game"))

# @app.route('/test') # why not? Holy shit it works!
# def test():
#     test_string = "<html><body><h1>Testing Testing Testing</h1></body></html>"
#     return render_template("test.html", test_string=test_string)

# YOU SHOULD CHANGE THIS IF YOU PUT ON THE INTERNET
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.run(debug=True)
