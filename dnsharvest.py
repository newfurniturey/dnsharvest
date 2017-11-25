#!/usr/bin/env python3

import argparse;
import socket;
import os;
import sys;
import re;
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

def isValidDomain(domain):
    # shortest possible domain is 4 characters; ex: a.bc
    if len(domain) < 4:
        return False;

    # we need at least 1 `.`
    if '.' not in domain:
        return False;

    # rudimentary regex to check if it's a valid base-domain
    # this is based on RFC-1035, except we allow domains to being with integers too
    pattern = '^([a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,}$';
    return re.match(pattern, domain, re.IGNORECASE) is not None;

def main(options):
    domain = options.domain;
    input_file = options.input.name;
    
    if isValidDomain(domain) is False:
        logger.error("invalid domain name");
        return 1;

    try:
        processList(domain, input_file);
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
