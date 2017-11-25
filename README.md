DNS Harvest
-----------

**DNS Harvest** isn't anything fancy, it's a DNS dictionary bruteforce tool.

Right now, it's single-threaded and limited to IPv4 and domain-existence reconnaisance. Hopefully soon it'll be expanded =]

### Usage

    ./dnsharvest.py -d example.com -i data/small.lst

The input file, `-i` in the example above, should be a single-column dictionary of words. If they're not valid subdomain names, the lookup will fail gracefully and move on.
