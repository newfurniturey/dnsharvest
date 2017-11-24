#!/usr/bin/env python3

import argparse;

def processList(domain, filePath):
    with open(filePath) as fp:
        for line in fp:
            subdomain = line.strip();
            print('%s.%s' % (subdomain, domain));

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
