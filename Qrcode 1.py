import qrcode
from tkinter import Tk, Label, Entry, Button, Toplevel, Canvas
from PIL import Image, ImageTk

def generate_qr():
    user_input = entry.get()
    if user_input.strip() == "":
        messagebox.showerror("Input Error", "Please enter some text to generate a QR code.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(user_input)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img = qr_img.convert("RGB")
    qr_img_tk = ImageTk.PhotoImage(qr_img)

    top = Toplevel(root)
    top.title("Generated QR Code")
    canvas = Canvas(top, width=qr_img.size[0], height=qr_img.size[1])
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=qr_img_tk)
    canvas.image = qr_img_tk

root = Tk()
root.title("QR Code Generator")
label = Label(root, text="Enter text to generate QR code:")
label.pack(pady=10)
entry = Entry(root, width=50)
entry.pack(pady=5)
generate_button = Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=20)
root.mainloop()
