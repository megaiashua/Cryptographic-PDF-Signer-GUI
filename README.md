# Cryptographic-PDF-Signer-GUI

Let's you invisibly sign PDF documents with a pfx or p12 (pkcs12) certificate
It signs the document using the PAdES-BASELINE-B signature format

You can check the signature validation from the generated PDFs with:

- https://ec.europa.eu/digital-building-blocks/DSS/webapp-demo/validation (use it just for test purposes, the files attached there are sent to EU Gov servers)
- Acrobat

# Recommended use for Windows users

Run the executable file in the link below.

https://pixeldrain.com/u/pS9DMzx4

If you run the .exe through VirusTotal it may show 10 warnings of malware, those are false positives because the code is not signed, I will have to send a report to those AV companies claiming false positives.

In case that you do not want to use the executable or have a different OS you can find the instructions below in order to run the script with python.

# Prerequisites for running the script

Add Python and Python scripts to PATH

C:\Users\USER\AppData\Local\Programs\Python\Python311

C:\Users\USER\AppData\Local\Programs\Python\Python311\Scripts

Doesn't need to be python 3.11, newer versions should work too.


Open CMD and add these libraries

```
pip install cryptography
pip install endesive
```

In case pip fails, try updating pip or use

```
python -m pip install cryptography
python -m pip install endesive
```

After those libraries are installed, just run the signer1.0.py scrip

I don't know the specifics to setup Python on Linux or MacOS, if you know how to please tell me.
