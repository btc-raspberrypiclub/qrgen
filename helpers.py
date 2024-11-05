from PIL import Image, ImageColor

def resize_logo(logo, basewidth):
    wpercent = (int(basewidth)/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))

    return logo.resize((int(basewidth), hsize))


def change_logo_color(logo, color):
    logo = logo.convert("RGB")
    mask = logo.convert("L").point(lambda x: 255 if x < 250 else 0)
    rgb_color = ImageColor.getcolor(color, "RGB")
    color_layer = Image.new("RGB", logo.size, rgb_color)
    
    return Image.composite(color_layer, logo, mask)

