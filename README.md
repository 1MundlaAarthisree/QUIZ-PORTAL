# QUIZ-PORTAL
This project is a quiz that facilitates multiple clients to connect to a server. A series of questions are broadcasted to the clients one at a time. The client who presses the buzzer first gets to answer, and if it happens to be correct, he scores a point.


This project is a quiz that facilitates multiple clients to connect to a server.
A series of questions are broadcasted to the clients one at a time. The
client who presses the buzzer first gets to answer, and if it happens to be
correct, he scores a point.


The server can effectively support 3 clients (players) in this game.
Multi-threading has been used to connect the clients with each other.
The rules of the game are as follows. When a question is displayed, all
players must key in an answer. 

An answer will be considered for evaluation
only if it is the first one to be received. If the answer happens to be correct,
he gains a point, else, he loses a point. The one who scores 5 points first,
wins. 

If no one scores 5 points by the end of twenty questions, the one with
the highest score wins.


The entire code has been written in Python.
