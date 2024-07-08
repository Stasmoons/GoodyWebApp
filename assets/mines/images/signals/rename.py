import os

photos = [i for i in os.listdir('.') if i.endswith('.jpg')][144:]

for n, photo in enumerate(photos, start=145):
    os.rename(photo, f"{n}.jpg")

