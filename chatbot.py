import asyncio
import chainlit as cl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import urllib.request
import numpy as np
import os

async def upload_file():
    while True:
        files = input("Please upload a file (enter the file path): ").strip()
        if files and os.path.exists(files):
            with open(files, 'r') as file:
                text = file.read()
                print(f" File uploaded successfully! It contains {len(text)} characters.")
            break
        else:
            print("Invalid file path. Try again!")

async def send_messages():
    text_content = "Attention is all you need!"
    elements_text = [cl.Text(name="Text Element", content=text_content, display="inline")]
    await cl.Message(content=" Check out the text element", elements=elements_text).send()

    image_path = "./image1.jpg"
    if os.path.exists(image_path):
        elements_image = [cl.Image(name="Image1", display="inline", path=image_path)]
        await cl.Message(content="Look at this local image", elements=elements_image).send()
    else:
        print(" Image file not found!")

async def display_video():
    video_url = input("Enter the video URL: ").strip()
    if not video_url:
        print(" No URL provided!")
        return

    fig, ax = plt.subplots()
    ax.axis('off')

    def update(frame):
        try:
            img = urllib.request.urlopen(video_url)
            img_data = np.array(bytearray(img.read()), dtype=np.uint8)
            img = np.reshape(img_data, (480, 640, 3))
            ax.imshow(img)
        except Exception as e:
            print(f"Error loading frame: {e}")
        return ax

    anim = animation.FuncAnimation(fig, update, frames=200, interval=20)
    plt.show()

async def main():
    print(" Starting asynchronous tasks...")
    await asyncio.gather(
        upload_file(),
        send_messages(),
        display_video()
    )

asyncio.run(main())
