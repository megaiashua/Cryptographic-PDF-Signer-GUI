# *-* coding: utf-8 *-*
import datetime
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.serialization import pkcs12
from endesive.pdf import cms
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def select_file(file_type):
    file_types = [("All Files", "*.*")]
    if file_type == "certificate":
        file_types = [("Certificate Files", "*.p12 *.pfx")]
    elif file_type == "pdf":
        file_types = [("PDF Files", "*.pdf")]

    file_path = filedialog.askopenfilename(filetypes=file_types)
    return file_path

def sign(password, certificate, pdf):
    date = datetime.datetime.utcnow() - datetime.timedelta(hours=12)
    date = date.strftime("D:%Y%m%d%H%M%S+00'00'")
    dct = {
        "aligned": 0,
        "sigflags": 1,
        "sigflagsft": 132,
        "sigpage": 0,
        "sigbutton": False,
        "sigfield": "Signature1",
        "auto_sigfield": False,
        "sigandcertify": True,
        "contact": "",
        "location": "",
        "signingdate": date,
        "reason": "",
        "password": password,
        # "signature_img": "signature_test.png",  # Signature image line removed
        "certification": "CERTIFIED_NO_CHANGES_ALLOWED", 
        # Certification level with no changes allowed after is signed, variations are
        # CERTIFIED_FORM_FILLING: Form fields can be filled in, but no other changes are allowed.
        # CERTIFIED_FORM_FILLING_AND_ANNOTATIONS: Form fields can be filled in, and annotations (comments) can be added, but no other changes are allowed.
    }
    p12 = pkcs12.load_key_and_certificates(
        certificate.read(), password.encode("ascii"), backends.default_backend()
    )

    datau = pdf.read()
    datas = cms.sign(datau, dct, p12[0], p12[1], p12[2], "sha256")
    return datau, datas

def sign_pdf():
    pdf_path = pdf_file_path.get()
    cert_path = cert_file_path.get()
    password = password_entry.get()

    if not password or not cert_path or not pdf_path:
        messagebox.showerror("Error", "All fields are required!")
        return
    try:
        with open(cert_path, "rb") as cert_file, open(pdf_path, "rb") as pdf_file:
            datau, datas = sign(password, cert_file, pdf_file)
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf")
        if output_path:
            with open(output_path, "wb") as output_file:
                output_file.write(datau)
                output_file.write(datas)
            messagebox.showinfo("Success", "PDF signed and certified successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI Setup
root = tk.Tk()
root.title("PDF Signer")

# Apply dark theme
style = ttk.Style()
style.theme_use('clam')

# Define dark theme colors
bg_color = '#2E2E2E'
fg_color = '#FFFFFF'
entry_bg_color = '#3E3E3E'
entry_fg_color = '#FFFFFF'
button_bg_color = '#3E3E3E'
button_fg_color = '#FFFFFF'

style.configure('TFrame', background=bg_color)
style.configure('TLabel', background=bg_color, foreground=fg_color, font=('Helvetica', 12))
style.configure('TButton', background=button_bg_color, foreground=button_fg_color, font=('Helvetica', 12), relief='flat')
style.configure('TEntry', fieldbackground=entry_bg_color, foreground=entry_fg_color, font=('Helvetica', 12), relief='flat')
style.map('TButton', background=[('active', button_bg_color)], relief=[('pressed', 'flat'), ('active', 'flat')])

root.configure(background=bg_color)

# Allow root window to be resizable
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Allow main_frame to expand
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=1)
main_frame.rowconfigure(3, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=0)

# PDF File
pdf_file_label = ttk.Label(main_frame, text="PDF File:")
pdf_file_label.grid(row=0, column=0, sticky=tk.W, pady=5)
pdf_file_path = tk.StringVar()
pdf_file_entry = ttk.Entry(main_frame, textvariable=pdf_file_path, width=50)
pdf_file_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
pdf_file_button = ttk.Button(main_frame, text="Browse", command=lambda: pdf_file_path.set(select_file("pdf")))
pdf_file_button.grid(row=0, column=2, sticky=tk.W, pady=5, padx=(25, 5))

# Certificate File
cert_file_label = ttk.Label(main_frame, text="Certificate File:  ")
cert_file_label.grid(row=1, column=0, sticky=tk.W, pady=5)
cert_file_path = tk.StringVar()
cert_file_entry = ttk.Entry(main_frame, textvariable=cert_file_path, width=50)
cert_file_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
cert_file_button = ttk.Button(main_frame, text="Browse", command=lambda: cert_file_path.set(select_file("certificate")))
cert_file_button.grid(row=1, column=2, sticky=tk.W, pady=5, padx=(25, 5))

# Password
password_label = ttk.Label(main_frame, text="Password:")
password_label.grid(row=2, column=0, sticky=tk.W, pady=5)
password_entry = ttk.Entry(main_frame, show="*", width=50)
password_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

# Sign Button
sign_button = ttk.Button(main_frame, text="Sign PDF", command=sign_pdf)
sign_button.grid(row=3, column=0, columnspan=3, pady=20)

root.mainloop()