def boxPrint(symbol, width, height):
    # Validate that the symbol is a single character.
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    # Validate that the width is greater than 2.
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    # Validate that the height is greater than 2.
    if height <= 2:
        raise Exception('Height must be greater than 2.')

    # Print the top edge of the box.
    print(symbol * width)
    # Print the sides of the box, with spaces in between the symbols.
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    # Print the bottom edge of the box.
    print(symbol * width)

# Loop through a tuple of symbol, width, and height combinations to print boxes.
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        # Attempt to print a box with the given dimensions and symbol.
        boxPrint(sym, w, h)
    except Exception as err:
        # Catch and print any exceptions raised by invalid inputs.
        print('An exception happened: ' + str(err))
