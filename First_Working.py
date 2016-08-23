#!/usr/bin/python

import dns.resolver

NameServers = raw_input("Which nameservers to you wish to question? >> ")
DomainNameToSearch = raw_input("Enter Domain to search >> ")
#RecordType = raw_input("Enter Record Type >> ")
myResolver = dns.resolver.Resolver()
#myResolver.nameservers = ['8.8.8.8', '8.8.4.4']
myResolver.nameservers = [NameServers]

try:
        myAnswers = myResolver.query(DomainNameToSearch, 'A')
        for rdata in myAnswers:
                print "The IP of your site is: %s " % rdata
        myAnswers2 = myResolver.query(DomainNameToSearch, 'MX')
        for rdata2 in myAnswers2:
                print "Your Email Server is: %s " % rdata2
except Exception as e:
        print e
