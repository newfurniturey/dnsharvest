DNS Harvest
-----------

**DNS Harvest** isn't anything fancy, it's a DNS dictionary bruteforce tool.

Right now, it's single-threaded and limited to IPv4 and domain-existence reconnaisance. Hopefully soon it'll be expanded =]

Oh yeah, also no error handling. Whatever =P

### Usage

    ./dnsharvest.py -d example.com -i data/small.lst

The input file, `-i` in the example above, should be a single-column dictionary of words matching the preferred name syntax outlined in [RFC 1035](https://tools.ietf.org/html/rfc1035).
