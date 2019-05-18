#!/usr/bin/python3

import server
import client

PORT = 6690

print("Выберете режим работы")
print("1-клиент; 2-сервер")

action=input(":")

if(action=="2"):
    server = server.ChatServer(PORT)

if(action=="1"):
    addres = input("Введите адрес сервера:");
    login = input("Введите свой логин:");
    client = client.ChatClient(addres,PORT,login)
