import cv2
import os
import numpy as np

def convert_non_black_pixels_to_white_opencv(image_path):
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    # Determine if the image has an alpha channel
    has_alpha = img.shape[2] == 4

    # Create a mask where non-black pixels are True
    if has_alpha:
        # Consider the alpha channel; keep fully transparent pixels as is
        mask = np.any(img[:, :, :3] != 0, axis=2) | (img[:, :, 3] == 0)
    else:
        mask = np.any(img[:, :, :3] != 0, axis=2)

    # Apply mask and set those pixels to white
    img[mask] = [1, 1, 1, 1] if has_alpha else [1, 1, 1]
    
    # Save the modified image
    cv2.imwrite(f"{image_path.rsplit('.', 1)[0]}.png", img)

def process_png_images_in_folder_with_opencv(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.png'):
            image_path = os.path.join(folder_path, filename)
            print(f"processing {filename}")
            convert_non_black_pixels_to_white_opencv(image_path)

# def process_png_images_in_folder_with_opencv(folder_path):
#     for filename in os.listdir(folder_path):
#         if filename.lower().endswith('.jpg'):
#             image_path = os.path.join(folder_path, filename)
#             img = cv2.imread(image_path)
#             print(img.dtype)
#             break
            

if __name__ == "__main__":
    folder_path = '/home/hamster02/courses/ugp_1/Motion_induction/tree/VOCdevkit/VOC2012/JPEGImages'  # Update this with the path to your images
    process_png_images_in_folder_with_opencv(folder_path)
