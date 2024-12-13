## Using Tor for Anonymity

To upload files via Tor, you must configure the connection to use Tor's SOCKS proxy:

```python
import socks
import socket

def configure_tor():
    socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
    socket.socket = socks.socksocket
```

After this configuration, all requests to IPFS and other networks will go through Tor.

## Troubleshooting

### 1. **IPFS Connection Error**

If you see a connection error to IPFS, ensure the IPFS daemon is running:

```bash
ipfs daemon
```

If using a public IPFS node, replace `localhost` with the URL of the provider (e.g., Infura).

### 2. **Tor Connection Issues**

Ensure Tor is running and accessible on port 9050. Check the Tor version:

```bash
tor --version
```

Also, verify that the SOCKS proxy for Tor is correctly set up.