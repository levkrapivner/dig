#!/usr/bin/python

import dns.resolver

myResolver = dns.resolver.Resolver()
myResolver.nameservers = ['8.8.8.8', '8.8.4.4']
ip = raw_input("Please Enter IP for PTR search ---> ")
try:
        req = '.'.join(reversed(ip.split("."))) + ".in-addr.arpa"
        myAnswers = myResolver.query(req, "PTR")
        for i in myAnswers:
                print i
except Exception as e:
        print e
