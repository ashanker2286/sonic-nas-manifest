# Python code block to create MAC address table entry

import   cps_utils

# Register attribute type
cps_utils.add_attr_type("base-mac/table/mac-address",   "mac")

# Define VLAN attributes
d  =     {"mac-address":   "00:0a:0b:cc:0d:0e", "ifindex":   18, "vlan":   "100"}

# Create CPS object
obj   =  cps_utils.CPSObject('base-mac/table',data=   d)

# Associate operation to CPS object
tr_obj   =  ('create',   obj.get())

# Create transaction object
transaction   =  cps_utils.CPSTransaction([tr_obj])

# Verify the return value
ret = transaction.commit()
if not   ret:
    raise   RuntimeError   ("Error   creating   MAC   Table   Entry") 
