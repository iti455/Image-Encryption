from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                r ^ key,
                g ^ key,
                b ^ key
            )

    img.save(output_path)
    print(f"✅ Image saved as: {output_path}")

# Inputs
input_image = "input.png"         # Place your image in the same folder
encrypted_image = "encrypted.png"
decrypted_image = "decrypted.png"
encryption_key = 123              # Same key used for both encrypt/decrypt

# Encrypt
encrypt_image(input_image, encrypted_image, encryption_key)

# Decrypt (run again on the encrypted image)
encrypt_image(encrypted_image, decrypted_image, encryption_key)
