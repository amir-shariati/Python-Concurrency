from time import perf_counter
import os
from PIL import Image, ImageFilter

from multiprocessing import Process

filenames = [
    'images/1.jpg',
    'images/2.jpg',
    'images/3.jpg',
    'images/4.jpg',
    'images/5.jpg',
]


def create_thumbnail(filename, size=(50, 50), thumb_dir='thumbs'):
    # open the image
    img = Image.open(filename)

    # apply the gaussian blur filter
    img = img.filter(ImageFilter.GaussianBlur())

    # create a thumbnail
    img.thumbnail(size)

    # save the image
    img.save(f'{thumb_dir}/{os.path.basename(filename)}')

    # display a message
    print(f'{filename} was processed...')


def main():
    start = perf_counter()

    # create processes
    processes = [Process(target=create_thumbnail, args=[filename])
                 for filename in filenames]

    # start the processes
    [process.start() for process in processes]

    # wait for completion
    [process.join() for process in processes]

    finish = perf_counter()

    print(f'It took {finish - start:.2f} second(s) to finish')


if __name__ == '__main__':
    main()
