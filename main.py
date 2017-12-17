from PIL import Image, ImageGrab
import pytesseract
import argparse
import os
import time
from imageutils import ImageUtils
from fuzzywuzzy import fuzz
import operator

def fuzzy_substring(needle, haystack):
    """Calculates the fuzzy match of needle in haystack,
    using a modified version of the Levenshtein distance
    algorithm.
    The function is modified from the levenshtein function
    in the bktree module by Adam Hupp"""
    m, n = len(needle), len(haystack)

    # base cases
    if m == 1:
        return not needle in haystack
    if not n:
        return m

    row1 = [0] * (n+1)
    for i in range(0,m):
        row2 = [i+1]
        for j in range(0,n):
            cost = ( needle[i] != haystack[j] )

            row2.append( min(row1[j+1]+1, # deletion
                               row2[j]+1, #insertion
                               row1[j]+cost) #substitution
                           )
        row1 = row2
    return min(row1)

def search_image_for_text(img, textToFind, minRatio = 75):
    ocrText = pytesseract.image_to_string(img)
    ratio = fuzz.ratio(textToFind, ocrText.rstrip().lower())
    if (ratio >= minRatio):
        return True
    return False

def find_item_in_list(ocrText, list):
    dict = {}

    for char in list:
        dict[char] = fuzz.ratio(char.lower(), ocrText.rstrip().lower())

    #print(dict)
    sortedDict = sorted(dict, key=lambda x: dict[x], reverse=True)
    for k in sortedDict:
        return k if dict[k] > 50 else None


pytesseract.pytesseract.tesseract_cmd = 'E:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

characters = [
    "Arthur", "Black Panther", "Black Widow", "Captain America", "Captain Marvel",
    "Chris", "Chun-Li", "Dante", "Doctor Strange", "Dormammu", "Firebrand",
    "Frank West", "Gamora", "Ghost Rider", "Hawkeye", "Hulk", "Jedah", "Iron Man",
    "Haggar", "Monster Hunter", "Morrigan", "Nemesis", "Nova", "Rocket Raccoon",
    "Ryu", "Sigma", "Spencer", "Strider Hiryu", "Spider-Man", "Thanos", "Thor",
    "Ultron", "Venom", "Winter Soldier", "X", "Zero"
]

players = [
    "mohnjiles", "Alexis", "Beastitude", "Papertowels", "Player 1", "Player 2"
]

stones = [
    "Reality", "Power", "Mind", "Space", "Time", "Soul"
]

player1characters = {}
player2characters = {}
player1Stones = {}
player2Stones = {}
gameStarted = False
gameOver = False

counter = 0

#ocrText = pytesseract.image_to_string(Image.open('p2c1.png'))
#print (get_character(ocrText))

while True:
    # get image
    img = ImageUtils.grab_screen()


    # see if it matches any of our shit
    # -- Character Select --
    if search_image_for_text(ImageUtils.get_character_select(img), "select characters"):
        gameStarted = False
        gameOver = False
        print("Character select found")

    # -- Loading --
    if search_image_for_text(ImageUtils.get_loading_start(img), "now loading"):
        print("Loading screen found")

    # -- Game Start / Stones --
    p1stonepic = ImageUtils.get_player_one_stone(img);
    player1StoneOcr = pytesseract.image_to_string(p1stonepic)
    player1Stone = find_item_in_list(player1StoneOcr, stones)
    if player1Stone is not None and player1Stone not in player1Stones:
        player1Stones.update({player1Stone: 1})
    elif player1Stone is not None:
        player1Stones[player1Stone] += 1

    if player1Stone is not None and not gameStarted:
        gameStarted = True
        gameOver = False
        player1characters = {}
        player2characters = {}
        player1Stones = {}
        player2Stones = {}
        print("Game started")

    player2StoneOcr = pytesseract.image_to_string(ImageUtils.get_player_two_stone(img))
    player2Stone = find_item_in_list(player2StoneOcr, stones)

    if player2Stone is not None and player2Stone not in player2Stones:
        player2Stones.update({player2Stone: 1})
    elif player2Stone is not None:
        player2Stones[player2Stone] += 1

    if player2Stone is not None and not gameStarted:
        gameStarted = True
        gameOver = False
        player1characters = {}
        player2characters = {}
        player1Stones = {}
        player2Stones = {}
        print("Game started")

    if gameStarted:
        # -- Get Player 1 Character 1 --
        p1c1img = ImageUtils.get_player1_character1(img)
        p1c1img.save("p1c1.png")
        p1c1text = pytesseract.image_to_string(p1c1img)
        p1c1 = find_item_in_list(p1c1text, characters)
        if p1c1 is not None and p1c1 not in player1characters:
            player1characters.update({p1c1 : 1})
        elif p1c1 is not None:
            player1characters[p1c1] += 1

        # -- Get Player 1 Character 2 --
        p1c2img = ImageUtils.get_player1_character2(img)
        p1c2img.save("p1c2.png")
        p1c2text = pytesseract.image_to_string(p1c2img)
        p1c2 = find_item_in_list(p1c2text, characters)
        if p1c2 is not None and p1c2 not in player1characters:
            player1characters.update({p1c2 : 1})
        elif p1c2 is not None:
            player1characters[p1c2] += 1

        # -- Get Player 2 Character 1 --
        p2c1img = ImageUtils.get_player2_character1(img)
        p2c1img.save("p2c1.png")
        p2c1text = pytesseract.image_to_string(p2c1img)
        p2c1 = find_item_in_list(p2c1text, characters)
        if p2c1 is not None and p2c1 not in player2characters:
            player2characters.update({p2c1 : 1})
        elif p2c1 is not None:
            player2characters[p2c1] += 1

        # -- Get Player 2 Character 2 --
        p2c2img = ImageUtils.get_player2_character2(img)
        p2c2img.save("p2c2.png")
        p2c2text = pytesseract.image_to_string(p2c2img)
        p2c2 = find_item_in_list(p2c2text, characters)
        if p2c2 is not None and p2c2 not in player2characters:
            player2characters.update({p2c2 : 1})
        elif p2c2 is not None:
            player2characters[p2c2] += 1

        p1Sorted = sorted(player1characters, key=lambda x: player1characters[x], reverse=True)
        p2Sorted = sorted(player2characters, key=lambda x: player2characters[x], reverse=True)
        player1actual = p1Sorted[:2]
        player2actual = p2Sorted[:2]

        print(player1actual, player2actual)

    # -- Check for end of game --
    if ((search_image_for_text(ImageUtils.get_game_over(img), "results")
        or search_image_for_text(ImageUtils.get_player_one_win_status(img), "winner")
        or search_image_for_text(ImageUtils.get_player_one_win_status(img), "loser"))
        and not gameOver):
        gameOver = True
        gameStarted = False
        print("Game over")

        # figure out who was who, and who won
        player1NameOcr = pytesseract.image_to_string(ImageUtils.get_player_one_name(img))
        player1Name = find_item_in_list(player1NameOcr, players)
        player1Win = "Won" if search_image_for_text(ImageUtils.get_player_one_win_status(img), "winner") else "Lost"

        player2NameOcr = pytesseract.image_to_string(ImageUtils.get_player_two_name(img))
        player2Name = find_item_in_list(player2NameOcr, players)
        player2Win = "Won" if search_image_for_text(ImageUtils.get_player_two_win_status(img), "winner") else "Lost"

        # get stones
        p1StonesSorted = sorted(player1Stones, key=lambda x: player1Stones[x], reverse=True)
        p2StonesSorted = sorted(player2Stones, key=lambda x: player2Stones[x], reverse=True)
        p1StoneActual = p1StonesSorted[0]
        p2StoneActual = p2StonesSorted[0]

        # for local multiplayer
        if player1Name is "Player 1":
            player1Name = "Papertowels"
        if player2Name is "Player 1" or player2Name is "Player 2":
            player2Name = "mohnjiles"

        if (len(player1actual) is 1):
            player1actual.append("X")
        if (len(player2actual) is 1):
            player2actual.append("X")

        print(f"{player1Name} {player1Win} with {player1actual[0]} and {player1actual[1]} using {p1StoneActual} Stone")
        print(f"{player2Name} {player2Win} with {player2actual[0]} and {player2actual[1]} using {p2StoneActual} Stone")

    time.sleep(1)
