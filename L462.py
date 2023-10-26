def main(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}. Mean = {mean(j)}")

def mean(data):
    return sum(data)/float(len(data))

if __name__ == '__main__':
    main(x=[1, 2, 3], y=[3, 3, 0], z=[22, 44, 6], r=[11, 7, 3])

