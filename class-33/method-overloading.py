def area(height=None, width=None, length=None):
    if height and width:
        return height * width
    elif height and width and length:
        return height * width * length
    elif height:
        return height * height
    elif width:
        return width * width
    elif length:
        return length * length
    else:
        return 0

def area():
    pass