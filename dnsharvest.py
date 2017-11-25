#!/usr/bin/env python3

import argparse;
import socket;
import os;
import sys;
import logging;
logger = logging.getLogger();

def processList(domain, filePath):
    with open(filePath) as fp:
        for line in fp:
            subdomain = line.strip();
            queryDomain('%s.%s' % (subdomain, domain));

def queryDomain(domain):
    try:
        ip = socket.gethostbyname(domain);
    except Exception:
        return False;
    
    print("%s\t%s" % (domain, ip));

def main(options):
    input_file = options.input.name;

    try:
        processList(options.domain, input_file);
        return 0;
    except Exception:
        logger.error("Unexpected error: %s - %s", exc.__class__.__name__, exc);
        return 1;

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Harvest the DNS');
    parser.add_argument('-d', '--domain',
        dest='domain', required=True, type=str,
        help='Target TLD to scan', metavar='DOMAIN');
    parser.add_argument('-i', '--input',
        dest='input', required=True, type=argparse.FileType('r', encoding='UTF-8'), 
        help='input file with subdomain names', metavar='FILE');
    args = parser.parse_args();
    
    sys.exit(main(args));
