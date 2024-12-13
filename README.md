# py-secure-file-sharing
Вот пример README для вашего проекта:

---

# Secure File Sharing

This project provides a secure and decentralized file sharing system, leveraging encryption, IPFS (InterPlanetary File System) for distributed storage, and anonymity protocols like Tor for privacy. The system ensures high levels of data security and anonymity, making it ideal for secure file transfer and storage.

## Features

- **AES Encryption**: Files are encrypted using AES encryption for confidentiality.
- **Decentralized File Storage**: Files are stored in a decentralized way using IPFS.
- **Anonymity via Tor**: Optionally, files can be uploaded anonymously via the Tor network.
- **Digital Signatures**: Data can be signed with RSA private keys and verified using public keys to ensure integrity.
- **Easy File Upload/Download**: Files can be easily uploaded to and downloaded from IPFS.

## Requirements

To run this project, you need the following:

- Python 3.6+
- Libraries:
  - `cryptography`
  - `ipfshttpclient`
  - `requests`
  - `PySocks` (for Tor support)
  - `PyCryptodome`
  - `os`
  
You can install the required libraries using `pip`:

```bash
pip install cryptography ipfshttpclient requests PySocks pycryptodome
```

Additionally, you need to have an **IPFS node** running. You can either run a local IPFS daemon or use a public IPFS gateway like [Infura](https://infura.io/).

### Running IPFS Locally

To run IPFS locally, install IPFS and start the daemon:

```bash
ipfs daemon
```

This will start a local IPFS node on `localhost:5001`.

### Running the Program

1. Clone this repository:

```bash
git clone <repository-url>
cd secure_file_sharing
```

2. Ensure that your files (e.g., `example.txt`) are in the same directory as `app.py` or update the path in the script.

3. Run the script:

```bash
python app.py
```

### File Flow

- **File Encryption**: The script encrypts a file using AES encryption.
- **File Upload to IPFS**: The encrypted file is uploaded to the IPFS network.
- **File Download from IPFS**: The encrypted file can be downloaded from IPFS using its hash.
- **File Decryption**: Once the file is downloaded, it is decrypted using the AES key.

### Example Output

```bash
Looking for file in: C:\Users\Nazar\Downloads\secure_file_sharing\example.txt
Encrypted file: example.txt.enc
File uploaded to IPFS with hash: QmHashOfFile
File downloaded from IPFS: C:\Users\Nazar\Downloads\secure_file_sharing\downloaded_example.txt
File decrypted successfully
```

## Notes

- **Security**: The program uses strong AES encryption for file security and RSA for signing data.
- **Anonymity**: If you want to upload files through Tor for anonymity, ensure that Tor is running and accessible via the SOCKS proxy.

## Troubleshooting

1. **IPFS Connection Error**:
   - Ensure that the IPFS daemon is running.
   - If you are not running a local IPFS node, you can modify the connection settings in the code to use a public IPFS gateway like Infura.

2. **Tor Connection**:
   - If the program doesn't connect via Tor, make sure the Tor service is running on your machine.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README includes all the necessary information to get started with your project and explains the requirements, installation steps, and usage.
