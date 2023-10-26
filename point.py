from PIL import Image, ImageDraw
import cv2
import os

new = Image.new(mode="RGB", size=(500,500), color="black")

x = 250
y = 250

images = []

for i in range(250):
    point_draw = ImageDraw.Draw(new)
    point_draw.point((x, y), fill="white")
    y = y + 1
    new.save(f"frames/{i}.jpg")
    images.append(f"{i}.jpg")

image_folder = "frames/"
video_name = "video.avi"

frame = cv2.imread(os.path.join(image_folder, images[0]))

height, width, layers = frame.shape
video = cv2.VideoWriter(video_name, 0, 50, (width, height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

os.system("sudo rm -r frames/*")







