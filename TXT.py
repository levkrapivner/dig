#!/usr/bin/python

import dns.resolver

myResolver = dns.resolver.Resolver()
myResolver.nameservers = ['8.8.8.8', '8.8.4.4']

try:
        myAnswers = myResolver.query("linuxadmin.biz", "TXT")
        for rdata in myAnswers:
                print rdata
except Exception as e:
        print e
