## Installation and Setup

### 1. Clone the repository to your local machine

Use the following command:

```bash
git clone https://github.com/yourusername/secure-file-sharing.git
cd secure-file-sharing
```

### 2. Install dependencies

Navigate to the project directory and run:

```bash
pip install -r requirements.txt
```

If this fails, install each library manually using `pip install`.

### 3. Configure IPFS and Tor (if needed)

If you want to use a local IPFS node, ensure it is running:

```bash
ipfs daemon
```

If you want to use Tor for anonymous uploads, ensure that Tor is running and accessible via the SOCKS proxy:

```bash
tor --version
```