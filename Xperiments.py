import numpy

board = [i for i in range(1,10)]
print(board)

move = input('make your move, input digit from 1-9\n>>> ')
move = int(move) 

for i in board :
    if move == i :
        print(i)
        i = 'X'
        print(i)
        #need to find way to replace the i in board, reverse the for i loop to put it back with new value

print(move)
print(board)


def f1(arr, find, replace):
    # fast and readable
    base=0
    for cnt in range(arr.count(find)):
        offset=arr.index(find, base)
        arr[offset]=replace
        base=offset+1

print(f1(board, move, 'X'))


#arr = numpy.asarray([1, 6, 1, 9, 8])
#arr[ arr == 8 ] = 0 
#print(arr)