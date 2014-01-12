# Constants here are from the Bluetooth Core Specification, Version 4.0,
# Part E, Section 7.7.8; (https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=229737)
# and from bluez's lib/hci.h (http://www.bluez.org/)

# BLE OpCode group field for the LE related OpCodes.
OGF_LE_CTL = 0x08

# BLE OpCode Commands.
OCF_LE_SET_EVENT_MASK = 0x0001
OCF_LE_READ_BUFFER_SIZE = 0x0002
OCF_LE_READ_LOCAL_SUPPORTED_FEATURES = 0x0003
OCF_LE_SET_RANDOM_ADDRESS = 0x0005
OCF_LE_SET_ADVERTISING_PARAMETERS = 0x0006
OCF_LE_READ_ADVERTISING_CHANNEL_TX_POWER = 0x0007
OCF_LE_SET_ADVERTISING_DATA = 0x0008
OCF_LE_SET_SCAN_RESPONSE_DATA = 0x0009
OCF_LE_SET_ADVERTISE_ENABLE = 0x000A
OCF_LE_SET_SCAN_PARAMETERS = 0x000B
OCF_LE_SET_SCAN_ENABLE = 0x000C
OCF_LE_CREATE_CONN = 0x000D
OCF_LE_CREATE_CONN_CANCEL = 0x000E
OCF_LE_READ_WHITE_LIST_SIZE = 0x000F
OCF_LE_CLEAR_WHITE_LIST = 0x0010
OCF_LE_ADD_DEVICE_TO_WHITE_LIST = 0x0011
OCF_LE_REMOVE_DEVICE_FROM_WHITE_LIST = 0x0012
OCF_LE_CONN_UPDATE = 0x0013
OCF_LE_SET_HOST_CHANNEL_CLASSIFICATION = 0x0014
OCF_LE_READ_CHANNEL_MAP = 0x0015
OCF_LE_READ_REMOTE_USED_FEATURES = 0x0016
OCF_LE_ENCRYPT = 0x0017
OCF_LE_RAND = 0x0018
OCF_LE_START_ENCRYPTION = 0x0019
OCF_LE_LTK_REPLY = 0x001A
OCF_LE_LTK_NEG_REPLY = 0x001B
OCF_LE_READ_SUPPORTED_STATES = 0x001C
OCF_LE_RECEIVER_TEST = 0x001D
OCF_LE_TRANSMITTER_TEST = 0x001E
OCF_LE_TEST_END = 0x001F

# BLE events; all LE commands result in a metaevent, specified by the subevent
# code below.
EVT_LE_META_EVENT = 0x3E

# LE_META_EVENT subevents.
EVT_LE_CONN_COMPLETE = 0x01
EVT_LE_ADVERTISING_REPORT = 0x02
EVT_LE_CONN_UPDATE_COMPLETE = 0x03
EVT_LE_READ_REMOTE_USED_FEATURES_COMPLETE = 0x04
EVT_LE_LTK_REQUEST = 0x05

# BLE address types.
LE_PUBLIC_ADDRESS = 0x00
LE_RANDOM_ADDRESS = 0x01

# Roles.
LE_ROLE_MASTER  =  0x00
LE_ROLE_SLAVE  =  0x01

# Advertisment event types.
LE_ADV_IND = 0x00
LE_ADV_DIRECT_IND = 0x01
LE_ADV_SCAN_IND = 0x02
LE_ADV_NONCONN_IND = 0x03
LE_ADV_SCAN_RSP = 0x04

# BLE scan types.
LE_SCAN_PASSIVE = 0x00
LE_SCAN_ACTIVE = 0x01

# BLE filter policies.
LE_FILTER_ALLOW_ALL = 0x00
LE_FILTER_WHITELIST_ONLY = 0x01
LE_FILTER_DUPLICATES_OFF = 0x00
LE_FILTER_DUPLICATES_ON = 0x01

# HCI error codes.
HCI_UNKNOWN_COMMAND = 0x01
HCI_NO_CONNECTION = 0x02
HCI_HARDWARE_FAILURE = 0x03
HCI_PAGE_TIMEOUT = 0x04
HCI_AUTHENTICATION_FAILURE = 0x05
HCI_PIN_OR_KEY_MISSING = 0x06
HCI_MEMORY_FULL = 0x07
HCI_CONNECTION_TIMEOUT = 0x08
HCI_MAX_NUMBER_OF_CONNECTIONS = 0x09
HCI_MAX_NUMBER_OF_SCO_CONNECTIONS = 0x0a
HCI_ACL_CONNECTION_EXISTS = 0x0b
HCI_COMMAND_DISALLOWED = 0x0c
HCI_REJECTED_LIMITED_RESOURCES = 0x0d
HCI_REJECTED_SECURITY = 0x0e
HCI_REJECTED_PERSONAL = 0x0f
HCI_HOST_TIMEOUT = 0x10
HCI_UNSUPPORTED_FEATURE = 0x11
HCI_INVALID_PARAMETERS = 0x12
HCI_OE_USER_ENDED_CONNECTION = 0x13
HCI_OE_LOW_RESOURCES = 0x14
HCI_OE_POWER_OFF = 0x15
HCI_CONNECTION_TERMINATED = 0x16
HCI_REPEATED_ATTEMPTS = 0x17
HCI_PAIRING_NOT_ALLOWED = 0x18
HCI_UNKNOWN_LMP_PDU = 0x19
HCI_UNSUPPORTED_REMOTE_FEATURE = 0x1a
HCI_SCO_OFFSET_REJECTED = 0x1b
HCI_SCO_INTERVAL_REJECTED = 0x1c
HCI_AIR_MODE_REJECTED = 0x1d
HCI_INVALID_LMP_PARAMETERS = 0x1e
HCI_UNSPECIFIED_ERROR = 0x1f
HCI_UNSUPPORTED_LMP_PARAMETER_VALUE = 0x20
HCI_ROLE_CHANGE_NOT_ALLOWED = 0x21
HCI_LMP_RESPONSE_TIMEOUT = 0x22
HCI_LMP_ERROR_TRANSACTION_COLLISION = 0x23
HCI_LMP_PDU_NOT_ALLOWED = 0x24
HCI_ENCRYPTION_MODE_NOT_ACCEPTED = 0x25
HCI_UNIT_LINK_KEY_USED = 0x26
HCI_QOS_NOT_SUPPORTED = 0x27
HCI_INSTANT_PASSED = 0x28
HCI_PAIRING_NOT_SUPPORTED = 0x29
HCI_TRANSACTION_COLLISION = 0x2a
HCI_QOS_UNACCEPTABLE_PARAMETER = 0x2c
HCI_QOS_REJECTED = 0x2d
HCI_CLASSIFICATION_NOT_SUPPORTED = 0x2e
HCI_INSUFFICIENT_SECURITY = 0x2f
HCI_PARAMETER_OUT_OF_RANGE = 0x30
HCI_ROLE_SWITCH_PENDING = 0x32
HCI_SLOT_VIOLATION = 0x34
HCI_ROLE_SWITCH_FAILED = 0x35
HCI_EIR_TOO_LARGE = 0x36
HCI_SIMPLE_PAIRING_NOT_SUPPORTED = 0x37
HCI_HOST_BUSY_PAIRING = 0x38
