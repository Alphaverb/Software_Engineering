def main(x, y, z, *args):
    one = x
    two = len(args)
    three = y
    four = sum(args)
    five = z
    print(f"one = {one}\ntwo = {two}\nthree = {three}\nfour = {four}\nfive = {five}")

    return x + str(two/four) + three + five

if __name__ == '__main__':
    result = main('We are ', ' times more ', 'effective', 1701, 113, 1.618, 42)
    print(f"\nresult = {result}")

