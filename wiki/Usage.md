## Usage

### 1. Encrypt Files

To encrypt a file before uploading to IPFS, run:

```bash
python app.py
```

This process includes:
- Encrypting the file using AES.
- Uploading the encrypted file to IPFS.
- Returning the file hash (CID), which can be used to retrieve it later.

### 2. Download Files

After uploading a file to IPFS, you can download it using its CID. To do so, run:

```bash
python app.py --download QmHashOfFile
```

This command will download the file from IPFS and decrypt it.