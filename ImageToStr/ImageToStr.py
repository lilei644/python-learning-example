import requests as req
from PIL import Image
from io import BytesIO

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()


if __name__ == '__main__':
    url = 'http://labfile.oss.aliyuncs.com/courses/370/ascii_dora.png'
    image = Image.open(BytesIO(req.get(url).content))
    width, height = image.size
    pix = image.load()
    result = ''
    for x in range(width):
        for y in range(height):
            r, g, b, a = pix[x, y]
            result += get_char(r, g, b)
        result += '\n'

    save_to_file('test.txt', result)
