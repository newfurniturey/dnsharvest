#!/usr/bin/env python3

import argparse;
import socket;

def processList(domain, filePath):
    with open(filePath) as fp:
        for line in fp:
            subdomain = line.strip();
            queryDomain('%s.%s' % (subdomain, domain));

def queryDomain(domain):
    try:
        data = socket.gethostbyname(domain);
        ip = repr(data);
    except Exception:
        return False;
    
    print("%s\t%s" % (domain, ip));

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Harvest the DNS');
    parser.add_argument('-d', '--domain',
        dest='domain', required=True, type=str,
        help='Target TLD to scan', metavar='DOMAIN');
    parser.add_argument('-i', '--input',
        dest='input', required=True, type=argparse.FileType('r', encoding='UTF-8'), 
        help='input file with subdomain names', metavar='FILE');
    args = parser.parse_args();
    
    processList(args.domain, args.input.name);
