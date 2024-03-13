from PIL import Image
import os



def encrypt_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    encrypted_pixels = []

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            encrypted_pixel = (pixel[1], pixel[2], pixel[0])  # Swap RGB values
            encrypted_pixels.append(encrypted_pixel)

    encrypted_img = Image.new(img.mode, (width, height))
    encrypted_img.putdata(encrypted_pixels)
    encrypted_image_path = os.path.splitext(image_path)[0] + "_encrypt_.png"
    encrypted_img.save(encrypted_image_path)
    # encrypted_img.show()

    return encrypted_image_path

def decrypt_image(encrypted_image_path):
    encrypted_img = Image.open(encrypted_image_path)
    width, height = encrypted_img.size
    decrypted_pixels = []

    for y in range(height):
        for x in range(width):
            pixel = encrypted_img.getpixel((x, y))
            decrypted_pixel = (pixel[2], pixel[0], pixel[1])  # Swap RGB values back
            decrypted_pixels.append(decrypted_pixel)

    decrypted_img = Image.new(encrypted_img.mode, (width, height))
    decrypted_img.putdata(decrypted_pixels)
    # decrypted_img.show()
    decrypted_image_path = os.path.splitext(image_path)[0] + " "+ "_decrypt_.jpg"
    decrypted_img.save(decrypted_image_path)

# Example usage:
image_path = "C:\\Users\\zubia\\OneDrive\\Desktop\\manuplate\\2.jpg"

# Encrypt image
encrypt_image_path=encrypt_image(image_path)

# Decrypt image
decrypt_image(encrypt_image_path)
