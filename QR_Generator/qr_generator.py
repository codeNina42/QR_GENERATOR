# qr_generator.py
import qrcode
from PIL import Image

def generate_qr(
    data: str,
    filename: str = "qrcode.png",
    version: int | None = None,
    box_size: int = 10,
    border: int = 4,
    fill_color: str = "black",
    back_color: str = "white"
) -> str:
    """
    Generate a QR code image and save to filename.
    """
    # Create QR code object
    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate image
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)
    return filename

if __name__ == "__main__":
    text = input("Enter text or URL to encode: ").strip()
    filename = input("Output filename (default qrcode.png): ").strip() or "qrcode.png"

    # Optional: custom colors
    fill = input("Fill color (default black): ").strip() or "black"
    back = input("Background color (default white): ").strip() or "white"

    saved = generate_qr(text, filename, fill_color=fill, back_color=back)
    print(f"QR code saved to: {saved}")

    # Show the image
    try:
        Image.open(saved).show()
    except Exception as e:
        print(f"Could not open image: {e}")
#python qr_generator.py