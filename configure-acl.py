# Python code block to configure ACL

import cps_utils

# Define enum map
e_stg = {'INGRESS': 1, 'EGRESS': 2}
e_ftype = {'SRC_MAC': 3, 'DST_MAC': 4, 'SRC_IP': 5, 'DST_IP': 6, 'IN_PORT': 9, 'DSCP': 21}
e_atype = {'PACKET_ACTION': 3, 'SET_TC': 10}
e_ptype = {'DROP': 1}

# Tell CPS utility about the type of each attribute
type_map = {
    'base-acl/entry/SRC_MAC_VALUE/addr': 'mac',
    'base-acl/entry/SRC_MAC_VALUE/mask': 'mac',
}
for key,val in type_map.items():
    cps_utils.cps_attr_types_map.add_type(key, val)
