# Python code block to delete port to VLAN

import cps
import cps_object

# Create CPS object
cps_obj = cps_object.CPSObject('dell-base-if-cmn/if/interfaces/interface')

# Populate the VLAN attributes VLAN_ID='br100'
VLAN_ID='br100'
cps_obj.add_attr('if/interfaces/interface/name',VLAN_ID)

# Delete the untagged-ports from VLAN, include the ports which is needed in the if_port_list
if_port_list=['e101-002-0']
cps_obj.add_attr('dell-if/if/interfaces/interface/untagged-ports',if_port_list)

# Associate a CPS set operation with the CPS object
cps_update = {'change':cps_obj.get(),'operation': 'set'}

# Add the CPS operation, object pair to a new CPS transaction
transaction = cps.transaction([cps_update])

# Check for failure
ret = transaction.commit()
if not transaction:
    raise RuntimeError ("Error in deleting ports to Vlan")
print "successful"
