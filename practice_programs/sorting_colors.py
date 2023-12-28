def sort_colors(colors) -> list:
    """ Given an array, colors, which contains a combination of the following three elements:
    0 - (representing red)
    1 - (representing white)
    2 - (representing blue)

    Sort the array in place so that the elements of the same color are adjacent,
    with the colors in the order of red, white, and blue. The function should return the same array.
    """
    red, white, blue = 0, 0, len(colors) - 1
    while white <= blue:
        if colors[white] == 0:
            if colors[red] != 0:
                colors[white], colors[red] = colors[red], colors[white]
            white += 1
            red += 1
        elif colors[white] == 1:
            white += 1
        else:
            if colors[blue] != 2:
                colors[white], colors[blue] = colors[blue], colors[white]
            blue -= 1
    return colors


arr = [2, 2, 2,  1, 0, 2, 1 , 1, 2, 0]
print(sort_colors(arr))