"""
ID: 526989a41034285187000de4

Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.
"""

from ipaddress import IPv4Address

def ips_between(start, end):
    start = int(IPv4Address(start))
    end = int(IPv4Address(end))

    return end - start

print(ips_between("10.0.0.0", "10.0.0.50"), 50)
print(ips_between("20.0.0.10", "20.0.1.0"), 246)