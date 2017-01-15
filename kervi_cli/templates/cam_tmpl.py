from kervi.camera import FrameCamera


class Cam_1(FrameCamera):
    def __init__(self):
        FrameCamera.__init__(self, "cam1", "camera 1")

    def get_frame(self, height, width):
        from PIL import Image, ImageDraw, ImageFont

        image = Image.new('RGBA', size=(width, height), color=(155, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.rectangle([(width/2-50, height/2-50), (width/2+50, height/2+50)])
        draw.rectangle([(10, 10), (width-10, height-10)])

        font = ImageFont.truetype("sans-serif.ttf", 32)
        draw.text((15, 15), "test x", font=font)
        return image

Cam_1()

