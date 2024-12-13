
## Requirements

### 1. **Python 3.6+**
This project requires Python 3.6 or higher.

### 2. **Required Libraries**
To install all dependencies, use the following command:

```bash
pip install -r requirements.txt
```

Required libraries:
- **cryptography** — for file encryption and decryption.
- **ipfshttpclient** — for interacting with IPFS.
- **requests** — for HTTP requests.
- **PySocks** — for connecting through Tor.
- **pycryptodome** — for cryptographic operations.

### 3. **IPFS Node**
To store files in IPFS, you need either to run your own IPFS node or use a public one (e.g., Infura). To run your own node, download and install IPFS from the official [[IPFS Install](https://ipfs.io/docs/install/)](https://ipfs.io/docs/install/) page.

### 4. **Tor (Optional)**
Tor can be used for anonymity when uploading files. Download and install Tor from the [[Tor Project](https://www.torproject.org/download/)](https://www.torproject.org/download/).