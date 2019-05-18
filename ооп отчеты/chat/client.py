
import socket
import json
import threading

from tkinter import *

#класс клиента

class ChatClient:
    port = 0
    sock = None
    login = None
    
    sotr = None
    stdscr = None
    
    tk = None
    msg = None
    log = None
    
    #Инициализация клиента
    def __init__(self, address, PORT, login):
        self.port=PORT
        self.login=login
        self.sock = socket.socket()
        self.sock.connect((address, self.port))
        
        self.do_exit=False

        sotr = threading.Thread(target=self.socket_wait, args=(self,))
        sotr.start()
        
        self.tk=Tk()
        self.tk.title('ChatDes')
        self.tk.geometry('500x300')
        text=StringVar()
        self.log = Text(self.tk)
        self.msg = Entry(self.tk, textvariable=text)
        self.msg.pack(side='bottom', fill='x', expand='true')
        self.log.pack(side='top', fill='both',expand='true')
        
        self.msg.focus_set()
        
        self.msg.bind('<Return>', self.send_msg)
        
        self.tk.mainloop()
        
        self.do_exit=True
        
    #Обработка события нажатия Enter на клавиатуре
    def send_msg(self, event):
        print ('Message:'+ event.widget.get())
        self.send_to_server("send_message",event.widget.get())
        event.widget.delete(0, END)
        
    #Отправка информации на сервер
    def send_to_server(self,action,value):
        self.sock.send(bytearray(json.dumps({'action': action,'value': value}),"utf-8"));
        
    #Поток прослушивания сокета
    @staticmethod
    def socket_wait(me):
        me.send_to_server('login',me.login)
        while not me.do_exit:
            data = me.sock.recv(4096)
            if data != "":
                data=data.decode("utf-8")
                data=json.loads(data)
            
            if data['action'] == 'a_u_alive':
                me.send_to_server("alive","");
                
            if data['action'] == 'message':
                me.log.insert(END,data['value']+"\n")
                
            
        me.sock.close()
