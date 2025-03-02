import re

# Daftar port default untuk berbagai skema URI
DEFAULT_PORTS = {
    "http": 80,
    "https": 443,
    "ftp": 21,
    "ssh": 22,
    "telnet": 23,
    "smtp": 25,
    "dns": 53,
    "dhcp": 67,
    "tftp": 69,
    "gopher": 70,
    "finger": 79,
    "pop3": 110,
    "nntp": 119,
    "imap": 143,
    "snmp": 161,
    "ldap": 389,
    "https-alt": 8443,
    "smtps": 465,
    "imaps": 993,
    "pop3s": 995,
    "rtsp": 554,
    "sip": 5060,
    "sips": 5061,
    "xmpp": 5222,
    "bittorrent": 6881,
    "irc": 6667,
    "rdp": 3389,
    "mysql": 3306,
    "postgresql": 5432,
    "redis": 6379,
    "mongodb": 27017,
}

# Regex untuk parsing URI
URI_REGEX = re.compile(
    r'^(?P<scheme>[a-zA-Z][a-zA-Z0-9+.-]+)://'  # Skema (http, https, dll.)
    r'(?:(?P<userinfo>[^@/]+)@)?'  # Opsional: userinfo 
    r'(?P<host>[^:/?#]+)'  # Host  
    r'(?::(?P<port>\d+))?'  # Opsional: port (:8080)
    r'(?P<path>/[^?#]*)?'  # Opsional: path (/docs/resource.txt)
    r'(?:\?(?P<query>[^#]+))?'  # Opsional: query string (?name=value)
    r'(?:#(?P<fragment>.*))?$'  # Opsional: fragment (#section1)
)

def parse_uri(uri):
    """Fungsi untuk mengekstrak komponen URI menggunakan regex"""
    match = URI_REGEX.match(uri)
    if not match:
        return None

    components = match.groupdict()

    # Jika port tidak ada, gunakan port default sesuai skema
    if components["port"] is None:
        components["port"] = DEFAULT_PORTS.get(components["scheme"], None)

    return components
