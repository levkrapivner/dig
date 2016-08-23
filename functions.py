#!/usr/bin/python

import dns.resolver
import socket

DomainNameToSearch = raw_input("Enter Domain to search >> ")
def dig_ns1():
        myResolver = dns.resolver.Resolver()
        myResolver.nameservers = ['80.244.161.84']

        try:
                myAnswers = myResolver.query(DomainNameToSearch, 'A')
                for rdata in myAnswers:
                        print "The IP of your site in ns1.sitesdepot.com is: %s " % rdata
                myAnswers2 = myResolver.query(DomainNameToSearch, 'MX')
                for rdata2 in myAnswers2:
                        print "Your Email Server in ns1.sitesdepot.com is: %s " % rdata2
        except Exception as e:
                print e


def dig_ns2():
        myResolver = dns.resolver.Resolver()
        myResolver.nameservers = ['80.244.160.50']
        try:
                myAnswers = myResolver.query(DomainNameToSearch, 'A')
                for rdata in myAnswers:
                        print "The IP of your site in ns2.sitesdepot.com is: %s " % rdata
                myAnswers2 = myResolver.query(DomainNameToSearch, 'MX')
                for rdata2 in myAnswers2:
                        print "Your Email Server in ns2.sitesdepot.com is: %s " % rdata2
        except Exception as e:
                print e
def ns():
        myResolver = dns.resolver.Resolver()
        myResolver.nameservers = ['80.244.161.84', '80.244.160.50']
        try:
                myAnswers = myResolver.query(DomainNameToSearch, "NS")
                for rdata in myAnswers:
                        print "Your NS is: %s " % rdata
        except Exception as e:
                print e
def TXT():
        myResolver = dns.resolver.Resolver()
        myResolver.nameservers = ['8.8.8.8']
        try:
                myAnswers = myResolver.query(DomainNameToSearch, "TXT")
                for rdata in myAnswers:
                        print "Your TXT is: %s " % rdata
        except Exception as e:
                print e
