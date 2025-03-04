"""Constants used by multiple MQTT modules."""
from homeassistant.const import CONF_PAYLOAD

ATTR_DISCOVERY_HASH = "discovery_hash"
ATTR_DISCOVERY_PAYLOAD = "discovery_payload"
ATTR_DISCOVERY_TOPIC = "discovery_topic"
ATTR_PAYLOAD = "payload"
ATTR_QOS = "qos"
ATTR_RETAIN = "retain"
ATTR_TOPIC = "topic"

CONF_AVAILABILITY = "availability"
CONF_BROKER = "broker"
CONF_BIRTH_MESSAGE = "birth_message"
CONF_COMMAND_TEMPLATE = "command_template"
CONF_COMMAND_TOPIC = "command_topic"
CONF_ENCODING = "encoding"
CONF_QOS = ATTR_QOS
CONF_RETAIN = ATTR_RETAIN
CONF_STATE_TOPIC = "state_topic"
CONF_STATE_VALUE_TEMPLATE = "state_value_template"
CONF_TOPIC = "topic"
CONF_WILL_MESSAGE = "will_message"

CONF_CERTIFICATE = "certificate"
CONF_CLIENT_KEY = "client_key"
CONF_CLIENT_CERT = "client_cert"
CONF_TLS_INSECURE = "tls_insecure"
CONF_TLS_VERSION = "tls_version"

CONFIG_ENTRY_IS_SETUP = "mqtt_config_entry_is_setup"
DATA_CONFIG_ENTRY_LOCK = "mqtt_config_entry_lock"
DATA_MQTT_CONFIG = "mqtt_config"
DATA_MQTT_RELOAD_NEEDED = "mqtt_reload_needed"

DEFAULT_PREFIX = "homeassistant"
DEFAULT_BIRTH_WILL_TOPIC = DEFAULT_PREFIX + "/status"
DEFAULT_DISCOVERY = True
DEFAULT_ENCODING = "utf-8"
DEFAULT_QOS = 0
DEFAULT_PAYLOAD_AVAILABLE = "online"
DEFAULT_PAYLOAD_NOT_AVAILABLE = "offline"
DEFAULT_RETAIN = False

DEFAULT_BIRTH = {
    ATTR_TOPIC: DEFAULT_BIRTH_WILL_TOPIC,
    CONF_PAYLOAD: DEFAULT_PAYLOAD_AVAILABLE,
    ATTR_QOS: DEFAULT_QOS,
    ATTR_RETAIN: DEFAULT_RETAIN,
}

DEFAULT_WILL = {
    ATTR_TOPIC: DEFAULT_BIRTH_WILL_TOPIC,
    CONF_PAYLOAD: DEFAULT_PAYLOAD_NOT_AVAILABLE,
    ATTR_QOS: DEFAULT_QOS,
    ATTR_RETAIN: DEFAULT_RETAIN,
}

DOMAIN = "mqtt"

MQTT_CONNECTED = "mqtt_connected"
MQTT_DISCONNECTED = "mqtt_disconnected"

PAYLOAD_EMPTY_JSON = "{}"
PAYLOAD_NONE = "None"

PROTOCOL_31 = "3.1"
PROTOCOL_311 = "3.1.1"
