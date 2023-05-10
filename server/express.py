from collections.abc import Callable
import io,sys
import socket,http.server as httpserver,socketserver,netrc,pip,html,http.client as httpclient,http
from typing import Any, BinaryIO
from socketserver import BaseRequestHandler
from socket import socket as _socket

class ActionSet(dict):

    def setdefault(self,rule,action,value):
        if(rule==None):
            rule="*"
        action_ = self.action(action)
        if(super().get(rule)==None):
            super().setdefault(rule,{})
        self[rule].setdefault(action_,value)

    def get(self,rule,action,default_):
        try:
            action = self[rule][0]
        except KeyError as key_error:
            action = default_
        finally:
            return action


def makeheaders(buff:bytes):
    delim = b'\r\n'
    buff = buff.split(b"\r\n",1)
    head = buff[0].lsplit(" ",0)
    if(len(head)<2):
        head = ["GET","/ HTTP/1.1"]
    head = [head[0]]+head[1].rsplit(" HTTP/",1)
    if(len(head)<3):
        head=head+["HTTP/1.1ß"]
    if(len(buff)>=2):
        buff= buff[1]
    else:
        buff=b''
    
    headers = {t[0].lower().strip() : (t[1] if len(t)>=2 else True)  for t in [[k.strip()  for k in i.split(b':')] for i in buff.split(delim)]}
    headers.setdefault("head",head)
    return headers


def readheader(s:socket.SocketIO):
    buffer = b''
    while b'\r\n\r\n' not in buffer :
        buffer+=s.read(1)
    sys.stdout.write(buffer.decode(errors="replace"))
    return makeheaders(buffer)


class RawHTTPServer(socket.socket):
    pass

class RefinedHTTPServer(httpserver.HTTPServer):
    
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate: bool = True) -> None:
        super().__init__(server_address, RequestHandlerClass, bind_and_activate)
        
    def serve_forever(self, poll_interval: float = 0.5) -> None:
        return super().serve_forever(poll_interval)
    def get_request(self) -> "tuple[socket.socket, _RetAddress]":
        return super().get_request()
    def process_request(self, request: '_RequestType', client_address: "_RetAddress") -> None:
        return super().process_request(request, client_address)
    def close_request(self, request: '_RequestType') -> None:
        return super().close_request(request)
    def finish_request(self, request: '_RequestType', client_address: "_RetAddress") -> None:
        return super().finish_request(request, client_address)
    def handle_request(self) -> None:
        return super().handle_request()
    def handle_error(self, request: '_RequestType', client_address: "_RetAddress") -> None:
        return super().handle_error(request, client_address)
    def verify_request(self, request: '_RequestType', client_address: "_RetAddress") -> bool:
        return super().verify_request(request, client_address)
    def shutdown_request(self, request: '_RequestType') -> None:
        return super().shutdown_request(request)
    def handle_timeout(self) -> None:
        return super().handle_timeout()
    def server_activate(self) -> None:
        return super().server_activate()
    def server_bind(self) -> None:
        return super().server_bind()
    def server_close(self) -> None:
        return super().server_close()
    def service_actions(self) -> None:
        return super().service_actions()
    def shutdown(self) -> None:
        return super().shutdown()
    def fileno(self) -> int:
        return super().fileno()

class HTTPREQHandler(httpserver.SimpleHTTPRequestHandler):
    
    def end_headers(self) -> None:
        return super().end_headers()
    
    def log_error(self, format: str, *args: Any) -> None:
        return super().log_error(format, *args)
    
    def send_error(self, code: int, message: 'str | None' = None, explain: 'str | None' = None) -> None:
        return super().send_error(code, message, explain)
    
    def handle_expect_100(self) -> bool:
        return super().handle_expect_100()
    
    def log_request(self, code: 'int | str' = "-", size: 'int | str' = "-") -> None:
        return super().log_request(code, size)
    
    def send_response(self, code: int, message: str | None = None) -> None:
        return super().send_response(code, message)
    
    def send_response_only(self, code: int, message: 'str | None' = None) -> None:
        return super().send_response_only(code, message)
    
    def parse_request(self) -> bool:
        return super().parse_request()
    
    def handle_one_request(self) -> None:
        return super().handle_one_request()
    
    def translate_path(self, path: str) -> str:
        return super().translate_path(path)
    
    def date_time_string(self, timestamp: int | None = None) -> str:
        return super().date_time_string(timestamp)
    
    def guess_type(self, path: "StrPath") -> str:
        return super().guess_type(path)
    
    def log_date_time_string(self) -> str:
        return super().log_date_time_string()
    
    def address_string(self) -> str:
        return super().address_string()
    
    def send_head(self) -> 'io.BytesIO | BinaryIO | None':
        return super().send_head()
    
    def send_header(self, keyword: str, value: str) -> None:
        return super().send_header(keyword, value)
    
    def setup(self) -> None:
        return super().setup()
    
    def version_string(self) -> str:
        return super().version_string()
    
    def do_GET(self) -> None:
        return super().do_GET()
    
    def do_HEAD(self) -> None:
        return super().do_HEAD()
    
    def list_directory(self, path: "StrPath") -> "io.BytesIO| None":
        return super().list_directory(path)
    
    def handle(self) -> None:
        return super().handle()
    
    def flush_headers(self) -> None:
        return super().flush_headers()
    
    def log_message(self, format: str, *args: Any) -> None:
        return super().log_message(format, *args)
    
    def copyfile(self, source: 'SupportsRead[str]', outputfile: 'SupportsWrite[str]') -> None:
        return super().copyfile(source, outputfile)
    
    def ext(self):
        pass

class HTTTPMixer(RefinedHTTPServer,HTTPREQHandler):

    config={}
    
    def __init__(self, server_address: '_AfInetAddress', bind_and_activate: bool = True) -> None:
        self.handle_reqs = self.handlereq
        self.config=self.__str__(),{"parent":self.config}
        self.actions = ActionSet()
        super().__init__(server_address, self, bind_and_activate)
    
    def finish_request(self, request: '_RequestType', client_address: "_RetAddress") -> None:
        return self.handle_reqs(request, client_address)
    
    def handlereq(self,req:socket.socket,client_address:"tuple[str,int]") -> None:
        print(req.__dir__())
        s = req.makefile("rwb",0)
        headers = readheader(s)
        print(headers)
        message = s.read(int(headers.get("content-length","0").strip()))
        print(f"=========\r\n{message.decode()}=======\r\n\r\n")
        print(client_address)
    
    handle_reqs = handlereq

    def setAction(self,method,action,callback):
        self.actions.setdefault(method,action,callback)

    def getAction(self,method,action):
        self.actions.get(method,action)

    def get(self,action,callback):
        self.setaction("get",action,callback)

    def set(self,key,value,global_=False,ancestory_=None):
        config = self.config
        if(global_):
            while self.config.get("parent")
        self.config.setdefault(key,value)
    
        

server = HTTTPMixer(("127.0.0.1",8080))

server.serve_forever()