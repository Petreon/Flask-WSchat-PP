from flask import request, session
from flask_socketio import emit
from .extensions import socketio

users = {}

@socketio.on("connect")
def handle_connect():
    print("Client connected!")


@socketio.on("user_join")
def handle_user_join(username):
    print(f"User {username} joined ")
    users[username] = request.sid
    session["username"] = username
    print(users)

@socketio.on("new_message")
def handle_message(message):
    print(f"New message: {message}")
    username = None
    print("print session: " +session.get('username'))

    for user in users:
        ## in this request it compares if the user has an session id in the dictionary and sendo to the server i dont think its a good practice but works, but i think it may give the server slowdown a bit
        if users[user] == request.sid:
            username = user
    emit("chat", {"message": message, "username":username}, broadcast=True)