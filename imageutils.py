from PIL import Image, ImageGrab, ImageEnhance
import pytesseract
import argparse
import os
import time


class ImageUtils:
    @staticmethod
    def grab_screen():
        return ImageGrab.grab()
        #return Image.open('victory1.png')

    @staticmethod
    def get_player_one_win_status(img):
        width = img.size[0] / 3
        height = img.size[1] / 3

        new_img = img.crop(
            (
                width - 280,
                height - 90,
                width + 175,
                height + 70
            )
        )
        doubleWidth = new_img.size[0] * 3
        doubleHeight = new_img.size[1] * 3
        new_img = new_img.convert('L').resize((doubleWidth, doubleHeight), Image.NEAREST)
        enhance = ImageEnhance.Contrast(new_img)
        new_img = enhance.enhance(3)
        return new_img

    @staticmethod
    def get_player_one_name(img):
        width = img.size[0] / 3
        height = img.size[1] / 3

        new_img = img.crop(
            (
                width - 300,
                height - 200,
                width - 85,
                height - 75
            )
        )
        doubleWidth = new_img.size[0] * 3
        doubleHeight = new_img.size[1] * 3
        new_img = new_img.convert('L').resize((doubleWidth, doubleHeight), Image.NEAREST)
        enhance = ImageEnhance.Contrast(new_img)
        new_img = enhance.enhance(3)
        return new_img

    @staticmethod
    def get_player_one_stone(img):
        width = img.size[0] / 4
        height = img.size[1]

        new_img = img.crop(
            (
                width - 230,
                height - 110,
                width - 120,
                height - 80
            )
        )
        doubleWidth = new_img.size[0] * 4
        doubleHeight = new_img.size[1] * 4
        new_img = new_img.convert('L').resize((doubleWidth, doubleHeight), Image.NEAREST)
        enhance = ImageEnhance.Contrast(new_img)
        new_img = enhance.enhance(3)
        return new_img

    @staticmethod
    def get_player_two_win_status(img):
        width = img.size[0] / 3
        height = img.size[1] / 3

        new_img = img.crop(
            (
                width + 475,
                height - 90,
                width + 975,
                height + 55
            )
        )
        doubleWidth = new_img.size[0] * 2
        doubleHeight = new_img.size[1] * 2
        new_img = new_img.convert('L').resize((doubleWidth, doubleHeight), Image.NEAREST)
        enhance = ImageEnhance.Contrast(new_img)
        new_img = enhance.enhance(3)
        return new_img

    @staticmethod
    def get_player_two_name(img):
        width = img.size[0] / 2
        height = img.size[1] / 3

        new_img = img.crop(
            (
                width + 475,
                height - 185,
                width + 700,
                height - 75
            )
        )
        doubleWidth = new_img.size[0] * 3
        doubleHeight = new_img.size[1] * 3
        new_img = new_img.convert('L').resize((doubleWidth, doubleHeight), Image.NEAREST)
        enhance = ImageEnhance.Contrast(new_img)
        new_img = enhance.enhance(3)
        return new_img

    @staticmethod
    def get_player_two_stone(img):
        width = img.size[0]
        height = img.size[1]

        new_img = img.crop(
            (
                width - 360,
                height - 110,
                width - 250,
                height - 80
            )
        )
        doubleWidth = new_img.size[0] * 4
        doubleHeight = new_img.size[1] * 4
        new_img = new_img.convert('L').resize((doubleWidth, doubleHeight), Image.NEAREST)
        enhance = ImageEnhance.Contrast(new_img)
        new_img = enhance.enhance(3)
        return new_img

    @staticmethod
    def get_character_select(img):
        width = img.size[0] / 2
        height = img.size[1] / 2

        new_img = img.crop(
            (
                width - 200,
                height - 425,
                width + 200,
                height - 350
            )
        )
        doubleWidth = new_img.size[0] * 2
        doubleHeight = new_img.size[1] * 2
        new_img = new_img.convert('L').resize((doubleWidth, doubleHeight), Image.NEAREST)
        enhance = ImageEnhance.Contrast(new_img)
        new_img = enhance.enhance(3)
        return new_img

    @staticmethod
    def get_player_one_hits(img):
        width = img.size[0] / 8
        height = img.size[1] / 3

        new_img = img.crop(
            (
                width - 100,
                height - 40,
                width + 100,
                height + 90
            )
        )
        doubleWidth = new_img.size[0] * 2
        doubleHeight = new_img.size[1] * 2
        new_img = new_img.convert('L').resize((doubleWidth, doubleHeight), Image.NEAREST)
        enhance = ImageEnhance.Contrast(new_img)
        new_img = enhance.enhance(3)
        return new_img

    @staticmethod
    def get_loading_start(img):
        width = img.size[0] / 8
        height = img.size[1]

        new_img = img.crop(
            (
                width - 55,
                height - 150,
                width + 150,
                height - 10
            )
        )
        doubleWidth = new_img.size[0] * 2
        doubleHeight = new_img.size[1] * 2
        new_img = new_img.convert('L').resize((doubleWidth, doubleHeight), Image.NEAREST)
        enhance = ImageEnhance.Contrast(new_img)
        new_img = enhance.enhance(3)
        return new_img

    @staticmethod
    def get_game_start(img):
        width = img.size[0] / 2
        height = img.size[1] / 4

        new_img = img.crop(
            (
                width - 50,
                height - 175,
                width + 50,
                height - 85
            )
        )
        doubleWidth = new_img.size[0] * 2
        doubleHeight = new_img.size[1] * 2
        new_img = new_img.convert('L').resize((doubleWidth, doubleHeight), Image.NEAREST)
        enhance = ImageEnhance.Contrast(new_img)
        new_img = enhance.enhance(3)
        return new_img

    @staticmethod
    def get_player1_character1(img):
        width = img.size[0] / 3
        height = img.size[1] / 8

        new_img = img.crop(
            (
                width - 340,
                height - 70,
                width - 75,
                height - 27
            )
        )
        doubleWidth = new_img.size[0] * 2
        doubleHeight = new_img.size[1] * 2
        new_img = new_img.convert('L').resize((doubleWidth, doubleHeight), Image.NEAREST)
        enhance = ImageEnhance.Contrast(new_img)
        new_img = enhance.enhance(3)
        return new_img

    @staticmethod
    def get_player1_character2(img):
        width = img.size[0] / 3
        height = img.size[1] / 8

        new_img = img.crop(
            (
                width - 375,
                height + 32,
                width - 180,
                height + 62
            )
        )
        doubleWidth = new_img.size[0] * 3
        doubleHeight = new_img.size[1] * 3
        new_img = new_img.convert('L').resize((doubleWidth, doubleHeight), Image.NEAREST)
        enhance = ImageEnhance.Contrast(new_img)
        new_img = enhance.enhance(3)
        return new_img

    @staticmethod
    def get_player2_character1(img):
        width = img.size[0] / 2
        height = img.size[1] / 8
        new_img = img.crop(
            (
                width + 410,
                height - 68,
                width + 665,
                height - 17
            )
        )
        doubleWidth = new_img.size[0] * 2
        doubleHeight = new_img.size[1] * 2
        new_img = new_img.convert('L').resize((doubleWidth, doubleHeight), Image.NEAREST)
        enhance = ImageEnhance.Contrast(new_img)
        new_img = enhance.enhance(3)
        return new_img
    @staticmethod
    def get_player2_character2(img):
        width = img.size[0] / 2
        height = img.size[1] / 8
        new_img = img.crop(
            (
                width + 500,
                height + 40,
                width + 700,
                height + 65
            )
        )
        doubleWidth = new_img.size[0] * 3
        doubleHeight = new_img.size[1] * 3
        new_img = new_img.convert('L').resize((doubleWidth, doubleHeight), Image.NEAREST)
        enhance = ImageEnhance.Contrast(new_img)
        new_img = enhance.enhance(3)
        return new_img

    @staticmethod
    def get_game_over(img):
        width = img.size[0] / 2
        height = img.size[1] / 6
        new_img = img.crop(
            (
                width - 100,
                height - 75,
                width + 100,
                height - 15
            )
        )
        doubleWidth = new_img.size[0] * 2
        doubleHeight = new_img.size[1] * 2
        new_img = new_img.convert('L').resize((doubleWidth, doubleHeight), Image.NEAREST)
        enhance = ImageEnhance.Contrast(new_img)
        new_img = enhance.enhance(3)
        return new_img
