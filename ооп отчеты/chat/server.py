
import socket
import json
import threading


#Класс обслуживания соединения
class ConServ(threading.Thread):
    conn = None
    address = None
    parent = None
    cid = None
    do_run = True
    
    login = None
    #инициализация
    def __init__(self,parent,conn,address,cid):
        self.conn = conn
        self.address = address
        self.parent = parent
        self.cid = cid
        threading.Thread.__init__(self)
        self.daemon = True
        print("Подключен клиент:",address);
        self.conn.settimeout(10)
        self._stop_event = threading.Event()
        
    #Поток клиента
    def run(self):
        while self.do_run:
            #Ждём сообщения от клиента
            try:
                r=self.conn.recv(4096).decode("utf-8")
                if(r!=""):
                    data=json.loads(r)
                else:
                    self.check_alive()
            except socket.timeout:
                # Если клиент не ответил, то проверяем состояние соединения
                self.check_alive()
                continue
                    
            if(data['action']=='exit'):
                self.self_destruction()
                
            if(data['action']=='login'):
                self.login = data['value']
                
            if(data['action']=='send_message'):
                msg = self.login+": "+data['value']
                print (msg)
                self.parent.send_to_all(self.parent,msg)
    
    #Функция отправки сообщения клиенту
    def send_message(self, action, value):
        self.conn.send(bytearray(json.dumps({"action":action, "value":value}),"utf-8"))
    
    #Проверка подключен ли ещё клиент
    def check_alive(self):
        try:
            self.send_message("a_u_alive","");
        except socket.error:
            self.self_destruction()
    
    #Уничтожение соединения
    def self_destruction(self):
        print("Клиент отключен:",self.address)
        self.parent.remove_client(self.parent,self.cid)
        
    #Остановка сокета
    def stop(self):
       self.do_run = False
       self.conn.close();
       self._stop_event.set()
       
    def stopped(self):
        return self._stop_event.is_set()
        

#Класс сервера

class ChatServer:
    port = 0
    clients = []
    exit = False
    last_cid = 0
    
    #рассылка сообщения всем клиентам
    @staticmethod
    def send_to_all(me,msg):
        for client in me.clients:
            addr, t =client['val'];
            t.send_message('message',msg);
    
    #Удаление клиента из списка клиентов
    @staticmethod
    def remove_client(me,cid):
        i=0
        for client in me.clients:
            if client['id'] == cid:
                addr, t =client['val'];
                t.stop();
                del me.clients[i]
                break
            i+=1
     
    #Отключение всех клиентов
    def remove_all(self):
        for client in self.clients:
            addr, t =client['val'];
            t.self_destruction();           
    
    #Инициализация сервера
    def __init__(self, PORT):
        self.port=PORT
        print("Нажмите Ctrl+C для выхода")
        print("Слушаю порт ",self.port)
        sock = socket.socket()
        sock.bind(('', self.port))
        sock.listen(10)
        while True:
            try:
                conn, addr = sock.accept()
                t = ConServ(self,conn,addr,self.last_cid)
                self.clients.append({"id":self.last_cid, "val": (addr,t)})
                self.last_cid+=1
                t.start()
            except KeyboardInterrupt:
                break
            
        self.remove_all()
        sock.close()
     
