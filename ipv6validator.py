import re

# IPv6 regex pattern including subnet
ipv6_pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}(/([0-9]|[1-9][0-9]|1[01][0-9]|12[0-8]))?$|^([0-9a-fA-F]{1,4}:){1,7}:(/([0-9]|[1-9][0-9]|1[01][0-9]|12[0-8]))?$|^::([0-9a-fA-F]{1,4}:){1,6}[0-9a-fA-F]{1,4}(/([0-9]|[1-9][0-9]|1[01][0-9]|12[0-8]))?$')

# Test the regex with the provided IPv6 address
test_address = "2001:4888:a01:2106:a1:fef:0::/112"
match = ipv6_pattern.match(test_address)

if match:
    print(f"{test_address} is a valid IPv6 address.")
else:
    print(f"{test_address} is not a valid IPv6 address.")
