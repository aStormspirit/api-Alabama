import base64

def png_to_base64(png_file_path):
    try:
        with open(png_file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return encoded_string
    except Exception as e:
        print(f"Ошибка при конвертации изображения: {str(e)}")
        return None

def base64_to_png(base64_string, output_file_path):
    try:
        image_data = base64.b64decode(base64_string)
        with open(output_file_path, "wb") as image_file:
            image_file.write(image_data)
        print(f"Изображение успешно сохранено в {output_file_path}")
    except Exception as e:
        print(f"Ошибка при конвертации Base64 в PNG: {str(e)}")

