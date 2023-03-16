# python3
#Dāvis Zommers 221RDB150

def build_heap(data):
    swaps = []
    for i in range(int(len(data)/2-1), -1, -1):
        heapify(data, i, swaps)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    return swaps
def heapify(data, i, swaps):
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < len(data) and data[left_child] < data[i]:
        min_val = left_child
    else:
        min_val = i
    if right_child<len(data) and data[min_val] > data[right_child]:
        min_val = right_child
    if min_val != i:
        data[i], data[min_val] = data[min_val], data[i]
        swaps.append((i, min_val))
        heapify(data, min_val, swaps)


            #data[1], data[4] = data[4], data[1]

    #print(data)
    #return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    choice = input()
    #n = int(input())
    if ("I" in choice):
        n = int(input())
        data = list(map(int, input().split()))


    if ("F" in choice):
        print("Input file path")
        path = input()
        path = "./tests/" + path
        f = open(path, "r")
        n = int(f.readline())
        data = list(map (int, f.readline().split()))
        f.close()
    # first two tests are from keyboard, third test is from a file

    print(data)


    # checks if lenght of data is the same as the said lenght
    assert len(data) == n
    
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

