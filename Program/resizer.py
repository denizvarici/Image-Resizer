from PIL import Image
import random

def resizeImageAndSave(image_path,width,height):
    image = Image.open(image_path)

    new_size = (width,height)

    resized_image = image.resize(new_size)

    path_parts = image_path.split("/")
    last_part = path_parts[-1]
    path_without_last_part = "/".join(path_parts[:-1])

    name_last_part = last_part.split(".")
    image_default_name = name_last_part[-2]
    image_type = name_last_part[-1]


    new_image_name = f"{image_default_name}_{width}x{height}.{image_type}"

    save_path = path_without_last_part +"/"+ new_image_name
    print(save_path)
    resized_image.save(save_path)

#sample usage for this script
#resizeImageAndSave("C:/Users/user/Desktop/theimage.png", 200, 200)