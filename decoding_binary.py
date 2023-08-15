import base64

base64_img = 'aG9sYSBjb21vIGVzdGFzIGxvY28KYSB2ZXIgcXVlIHBhc2EK'

base64_img_bytes = base64_img.encode('utf-8')
with open('decoded_image.txt', 'wb') as file_to_save:
    decoded_image_data = base64.decodebytes(base64_img_bytes)
    file_to_save.write(decoded_image_data)
