#!/usr/bin/env python
import os
import sys
import socket
import requests

def check_server(server, port):
    # Create a TCP socket
    s = socket.socket()
    try:
        s.connect((server, port))
        f.write("%s => %s:%s [OK]\n" % (local, server, port))
        return True
    except:
        f.write("%s => %s:%s [Error]\n" % (local, server, port))
        return False
    finally:
        s.close()
        f.close()

def remove_logfile(logfile,sum_file):
   if os.path.exists(logfile):
      os.remove(logfile)

   if os.path.exists(sum_file):
      os.remove(sum_file)


def aggregate_logs(servers_list):
    f = open(sum_file, "a")
    for server in servers_list:
        try:
            response = requests.get('http://'+server+'/netcheck.log')
            f.write(response.text)
        except:
            f.write("Failed to get log from %s [Error]\n" % (server))
    f.close()

if __name__ == '__main__':
  local = socket.gethostname()
  logfile = '/var/www/html/netcheck.log'
  sum_file = 'summary.log'
  func = sys.argv[1]

if func == 'cleanup':
    remove_logfile(logfile, sum_file)
elif func == 'check':
    server = sys.argv[2]
    port = int(sys.argv[3])
    if local == 'mainserver':
      f = open(logfile, "a")
    else:
      f = open(logfile, "w")
    check_server(server, port)
elif func == 'aggregate':
    servers_list = sys.argv[2:]
    aggregate_logs(servers_list)
