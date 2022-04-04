#!/bin/python3

import configparser
import  paramiko


config = configparser.ConfigParser()
config.read('version.ini',encoding='utf-8')

def ssh_params(hostname,port,username,passwd,command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname,port,username,passwd)
    stdin,stdout,stderr = ssh.exec_command(command)
    print(stdout.read())
    ssh.close()

ssh_params(hostname=config.get('cmd','hostname'),port=config.getint('cmd','port')
           ,username=config.get('cmd','username'),passwd=config.get('cmd','passwd'),
           command=config.get('cmd','command'))
