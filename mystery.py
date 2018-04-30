def double(arg):
    print('Przed: ', arg)
    arg = arg*2
    print('Po:  ', arg)
def change(arg):
    print('Przed: ', arg)
    arg.append('Więcej danych')
    print('Po:  ', arg)
num=10
double(num)
saying='halo '
double(saying)
numbers=[42, 256, 16]
double(numbers)

change(numbers)