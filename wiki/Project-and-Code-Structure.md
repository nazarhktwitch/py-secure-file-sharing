Project and Code Structure

The project is organized into the following structure:

secure-file-sharing/

├── app.py                    Main file to run the application

├── encryption.py             Functions for file encryption and decryption

├── storage.py                IPFS interactions (uploading and downloading files)

├── anonymity.py              Handles Tor configuration for anonymity

├── crypto_keys.py            Utility for crypto keys

├── settings.py               Configuration settings (e.g., for IPFS, Tor, encryption keys)

├── requirements.txt          List of Python dependencies

├── README.md                 README of the project

├── example.txt               Example file for encryption

├── docs/

└───── See docs down:         Documentation for the project

Detailed Documentation Files:

    docs/Home.md:
        Home of documentation and navigation

    docs/Project-and-Code-structure.md:
        Project structure

    docs/License.md:
        License

    docs/Introduction.md:
        Introduction

    docs/Features-of-the-Project.md:
        Features of the project

    docs/Example-Workflow.md:
        Examples

    docs/Installation and setup.md:
        Explains in detail how to install the required dependencies, set up IPFS, configure Tor (if needed), and get the project running on a local machine.

    docs/File-Encryption-Guide.md:
        Provides an in-depth guide on how file encryption works in the project, including details on AES and RSA, how files are encrypted before upload, and how decryption works after downloading.

    docs/IPFS-Integration.md:
        Describes how to configure and use IPFS for storing files, including uploading, downloading, and retrieving files by their CID (hash).
        Details both local and public IPFS node usage.

    docs/Using-Tor-for-Anonymity.md:
        Provides instructions for configuring the Tor network for anonymity, including installation and connection setup using the SOCKS proxy.
        Details how to route IPFS traffic through Tor to hide the user's IP address.

    docs/usage.md:
        Explains how to run the project, including basic commands to encrypt files, upload to IPFS, and decrypt files.
        Includes example workflows and expected output.