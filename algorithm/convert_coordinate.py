# x, y to row, col
def cartesianToIndex(x, y, height):
    row = height - y - 1
    col = x
    return row, col

# row, col to x, y
def indexToCartesian(row, col, height):
    y = height - row - 1
    x = col
    return x, y