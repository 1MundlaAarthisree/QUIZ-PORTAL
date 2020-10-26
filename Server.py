import socket
import select
from thread import *
import sys
import time
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3 :
    print "Format : <script> <IP address> <port number>"
    exit()

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.bind((IP_address, Port))
server.listen(3)
clientList = []

Question = ["The language spoken by the people by Pakistan is?\nA. Hindi \nB. Palauan \nC. Sindhi \nD. Nauruan\n", "The World Largest desert is? \nA. Thar \nB. Kalahari \nC. Sahara \nD. Sonoran\n", " Country that has the highest in Barley Production ?\nA. China \nB. India \nC. Russia \nD. France\n", "The metal whose salts are sensitive to light is?\nA. Zinc \nB. Silver \nC. Copper \nD.Aluminium\n", "The Central Rice Research Station is situated in?\nA. Chennai \nB. Cuttack \nC. Bangalore \nD. Quilon\n", "Mount Everest is located in?\nA. India \nB. Nepal \nC. Tibet \nD. China\n", "Which soil is suitable for agriculture? \nA. Red soil \nB. Sand \nC. Black soil \nD. Peaty soil\n", "Black soils are best suited for the cultivation of?\nA. Cotton \nB. Rice \nC. Cereals \nD. Sugarcane\n", "The device used for measuring altitudes is?\nA. altimeter \nB. ammeter \nC. audiometer \nD. galvanometer\n", "The Gate way of India is?\nA. Chennai \nB. Mumbai \nC. Kolkata \nD. New Delhi\n", "The first chairman of the Atomic Energy Commission was?\nA. Dr.C.V.Raman \nB. Dr.H.J.Bhabha \nC. Dr.A.P.J.Abdul Kalam \nD. Dr.Vickram Sarabhai\n", "12. D.D.T. was invented by?\nA. Mosley \nB. Rudeolf \nC. Karl Benz \nD. Dalton\n", "Which is considered as the biggest port of India?\nA. Kolkata \nB. Cochin \nC. Chennai \nD. Mumbai\n", "The gas used for making vegetables is?\nA. Oxygen \nB. Carbon dioxide \nC. Hydrogen \nD. Nitrogen\n", "The chief ore of Aluminium is?\nA. Iron \nB. Cryolite \nC. Bauxite \nD. Haematite\n"]

Answer = ['C','C','C','B','B','B','D','A','A','B','B','A','D','C','C']
score = []

plr = "Gayathri"
plrno = -1
qno=0
firstPlayerToAnswer = 0
quizOver = 0
count = 0

qstn = random.choice(Question)
for i in range(len(Question)) :
    	if qstn == Question[i] :
        	qno = i

def clientthread(conn, addr) :
	global plr, plrno, firstPlayerToAnswer, quizOver, count, qno
	conn.send("Welcome to the Quiz! There will be a set of 15 questions, and the answer that is received first is evaluated. First one to gain 5 point wins! If no participant earns 5 points, the one with the highest score wins.")
    	while True :
             
            	buzzr = conn.recv(2048)
		if buzzr :
			count += 1
                	if firstPlayerToAnswer == 0 :
				plr = conn
                    		firstPlayerToAnswer = 1
				for i in range(len(clientList)) :
					if clientList[i] == conn :
						plrno = i
						break
				while count != 3 :
					pass
				conn.send("Wrong answer. Try again!")
                	elif firstPlayerToAnswer == 1 and conn == plr :
				if message[0] == Answer[qno] :
					conn.send("Your answer is correct!")
					time.sleep(1)
                            		broadcast("\nPlayer" + str(plrno + 1) + " +1\n")
                            		score[plrno] += 1
                            		if score[plrno] == 5 :
                                		broadcast("Player" + str(plrno + 1) + " is the winner!\n")
                               		 	for i in range(len(clientList)) :
                                    			broadcast("Player" + str(i + 1) + " scored " + str(score[i])+ ".\n")
                                		quizOver = 1
						broadcast("\nThank you for playing!\n")
						time.sleep(10)
						conn.close()
						server.close()
                        	else :
					conn.send("Incorrect!")
					time.sleep(1)
                            		broadcast("\nPlayer" + str(plrno + 1) + " -1\n")
                            		score[plrno] -= 1
                        	Answer.pop(qno)
                        	Question.pop(qno)
                        	firstPlayerToAnswer = 0
                        	if len(Question) == 0 and quizOver == 0 :
                            		quizOver = 1
                            		i = score.index(max(score))
                            		broadcast("Player" + str(i + 1) + " is the winner!\n")
                            		for i in range(len(clientList)) :
                            	       		broadcast("Player" + str(i + 1) + " scored " + str(score[i])+ ".\n")
                            	    		quizOver = 1
						broadcast("Thank you for playing!\n")
						time.sleep(5)
						conn.close()
						server.close()
                        	if quizOver == 0 :
					time.sleep(1)
                            		quiz()
                	else :
				while count != 3 :
					pass
                    		conn.send("Sorry, player" + str(plrno + 1) + " was faster than you!")
		else :
			removeClient(conn)

def removeClient(connection) :
    	if connection in clientList :
        	clientList.removeClient(connection)

def broadcast(message) :
    	for client in clientList :
        	try :
           	 	client.send(message)
        	except:
            		client.close()
            		removeClient(client)


def quiz() :
	global count, qstn, qno
	if len(Question) != 0 :
        	qstn = random.choice(Question)
        	for i in range(len(Question)) :
            		if qstn == Question[i] :
                		qno = i
        for connection in clientList :
            connection.send(qstn)
	count = 0

while True :
    	conn, addr = server.accept()
    	clientList.append(conn)
    	score.append(0)
    	print addr[0] + " connected."
    	start_new_thread(clientthread, (conn,addr))
	if(len(clientList) == 3) :
        	time.sleep(1)
        	quiz()
