# Crytographic-PDF-Signer-GUI

Let's you invisibly sign PDF documents with a pfx or p12 (pkcs12) certificate
It signs the document using the PAdES-BASELINE-B signature format

# Prerequisites

Add Python and Python scripts to PATH

C:\Users\USER\AppData\Local\Programs\Python\Python311

C:\Users\USER\AppData\Local\Programs\Python\Python311\Scripts

Doesn't need to be python 3.11, newer versions should work too.


Open CMD and add these libraries

```
pip install Cryptography
pip install endesive
```

In case pip fails, try updating pip or use

```
python -m pip install Cryptography
python -m pip install endesive
```

After those libraries are installed, just run the signer1.0.py scrip

I don't know the specifics to setup Python on Linux or MacOS, if you know how to please tell me.
