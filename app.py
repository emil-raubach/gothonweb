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
    room_name = session.get('room_name') # sets the room name to the first room and then to the room_name passed to the session by the last room.

    if request.method == 'GET':
        if room_name:
            # what does this do?
            print(">>> room_name =", room_name, "whose type is ", type(room_name))
            room = planisphere.load_room(room_name)
            print(">>> room =", room, " and its name is: ", str(room))
            return render_template("show_room.html", room=room)
        else:
            # why is there here? do you need it?
            print(">> When does this logic happen?", room, " type", type(room))
            return render_template("show_room.html", room=room)
    else:
        print("***Starting a POST request.***")
        print(">>>> Current room name is: ", room_name)
        action = request.form.get('action')
        print(">>>> The form action is =", action)
        if room_name and action:
            room = planisphere.load_room(room_name)
            print(">> room =", str(room), " which is the current room.")
            print(">> The path is ", repr(room.paths))
            # need to 'intercept' the action here and pass it to something
            # (a function or Room() object variable) that can change / update
            # the paths{} dict based on some logic that uses the input.
            next_room = room.choosepath.enter(action)
            #next_room = room.go(action)
            print(">> next_room =", str(next_room))

            if not next_room: # if next_room returns None, then reload the current room.
                session['room_name'] = planisphere.name_room(room)
            else: # otherwise update the session with the next_room
                session['room_name'] = planisphere.name_room(next_room)

        return redirect(url_for("game")) # I think this acts as the game loop

# YOU SHOULD CHANGE THIS IF YOU PUT ON THE INTERNET
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.run(debug=True)
