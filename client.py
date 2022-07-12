import socket                                                                                                                                                                                                                                               
from select import select
from parser import parse_args

argg = {
    'DEST_IP':None,
    'DEST_PORT':8881,
    'LOCAL_IP':'127.0.0.1',
    'LOCAL_SERVICE':51820,
    }


argums = parse_args(argg)     

DEST_IP = argums.DEST_IP
DEST_IP = socket.gethostbyname(DEST_IP)
DEST_PORT = argums.DEST_PORT
LOCAL_IP = argums.LOCAL_IP 
LOCAL_SERVICE = argums.LOCAL_SERVICE  
                                                                                                                                                                                                                                                             
sock_remote = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock_remote.connect((DEST_IP,DEST_PORT)) 
sock_local = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock_local.connect((LOCAL_IP,LOCAL_SERVICE)) 
sockets = (sock_remote, sock_local) 
while True:    
    for s in sockets:
        s.setblocking(0)                                                                                                                                                                                                                                     
    
    # loop forever forwarding packets between the connections while True:
        avail, _, _ = select((sock_local, sock_remote), (), (), 1)                                                                                                                                                                                           
    
        # send a keep alive message every timeout
        if not avail:
            sock_remote.send(b'keep alive')
            continue
    
        for s in avail:
            # something from the local server, forward it on
            if s is sock_local:
                msg = sock_local.recv(8192)                                                                                                                                                                                                                  
                sock_remote.send(msg)                                                                                                                                                                                                                        
    
            # something from the remote server
            if s is sock_remote:
                msg = sock_remote.recv(8192)                                                                                                                                                                                                                 
                # don't forward keep alives to local system
                if msg != b'keep alive':
                    sock_local.send(msg)
