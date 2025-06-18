# Image-Encryption

🔐 Task 02 – Image Encryption Tool Using Pixel Manipulation
🧩 Objective
Create a simple image encryption tool that uses pixel manipulation. The tool should:
-Support operations like swapping pixel values or
-Apply a basic mathematical operation (e.g., XOR) to each pixel for encryption.

🛠️ Features
-Reads any .png image file.
-Encrypts the image by applying a bitwise XOR operation to each pixel.
-Decrypts the image using the same logic (XOR is symmetric).
-Saves both the encrypted and decrypted output.

📁 Project Structure
![image](https://github.com/user-attachments/assets/87eed591-6a16-4efc-847e-3a5b1a47feaf)

🧪 How It Works
-This project uses the Pillow library to manipulate pixel values. It performs:
-A bitwise XOR ( ^ ) operation on the RGB values of each pixel using a secret key.
-Re-running the same function with the encrypted image and the same key decrypts it.

💡 Prerequisites
Install Pillow (Python Imaging Library):
pip install Pillow

▶️ Run Instructions
Place an image named input.png in the project folder.
Run the Python script:
python image_encryptor.py

Check the folder for:
encrypted.png
![encrypted](https://github.com/user-attachments/assets/dcc704c7-96ca-44a8-9b92-ebff8c423a25)

decrypted.png
![decrypted](https://github.com/user-attachments/assets/79f04035-6da0-49fe-aeb8-90538baf340c)

# output
![image](https://github.com/user-attachments/assets/60b3b8bf-3344-4899-b348-59a7c5df082d)

