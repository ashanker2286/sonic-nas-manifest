# Python code block to set IP address

import   cps_utils

# Populate the attributes for the CPS object
ifindex=16
ip_addr="10.0.0.1"
pfix_len=16
ip_attributes   =  {"base-ip/ipv4/ifindex":   ifindex,"ip":ip_addr,"prefix-length":pfix_len}

# Create CPS object
cps_utils.add_attr_type('base-ip/ipv4/address/ip',"ipv4")
cps_obj=cps_utils.CPSObject('base-ip/ipv4/address',data=ip_attributes)

# Create the CPS transaction for object create
cps_update   =  ('create',   cps_obj.get())
transaction   =  cps_utils.CPSTransaction([cps_update])

# Check for failure
ret = transaction.commit()
if not   ret:
    raise   RuntimeError   ("Error   ")
