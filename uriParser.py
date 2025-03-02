def parse_uri(uri):
    """Fungsi untuk mengekstrak komponen URI tanpa menggunakan regex"""
    
    components = {
        "scheme": None,
        "userinfo": None,
        "host": None,
        "port": None,
        "path": None,
        "query": None,
        "fragment": None
    }
    
    # 1. Memisahkan skema (scheme)
    if "://" in uri:
        scheme_split = uri.split("://", 1)
        components["scheme"], uri = scheme_split[0], scheme_split[1]
    else:
        return None  # URI tidak valid jika tidak ada skema
    
    # 2. Memeriksa adanya fragment (#)
    if "#" in uri:
        uri, components["fragment"] = uri.split("#", 1)

    # 3. Memeriksa adanya query string (?)
    if "?" in uri:
        uri, components["query"] = uri.split("?", 1)

    # 4. Memeriksa adanya userinfo (@)
    if "@" in uri:
        userinfo_split = uri.split("@", 1)
        components["userinfo"], uri = userinfo_split[0], userinfo_split[1]

    # 5. Memeriksa adanya port (:)
    if "/" in uri:
        host_port, components["path"] = uri.split("/", 1)
        components["path"] = "/" + components["path"]
    else:
        host_port = uri  # Jika tidak ada path, berarti hanya ada host dan port
    
    if ":" in host_port:
        host_port_split = host_port.split(":", 1)
        components["host"], components["port"] = host_port_split[0], host_port_split[1]
    else:
        components["host"] = host_port

    # 6. Menetapkan port default jika tidak ada
    DEFAULT_PORTS = {
        "http": 80, "https": 443, "ftp": 21, "ssh": 22, "telnet": 23, "smtp": 25,
        "dns": 53, "dhcp": 67, "tftp": 69, "pop3": 110, "imap": 143, "ldap": 389,
        "mysql": 3306, "postgresql": 5432, "redis": 6379, "mongodb": 27017,
    }
    
    if components["port"] is None:
        components["port"] = DEFAULT_PORTS.get(components["scheme"], None)

    return components
