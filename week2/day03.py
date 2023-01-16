song='''When an eel grabs your arm,
And it causes great harm,
That's -a morey '''

print(song.replace(' m',' M',100))

song_list = song.split()
print(song_list)
# if 'moray' in song_list:
#     song_list.title()
# print(song_list)
#
# song_list[14] = song_list[14].title()
# song_string = ' '.join(song_list)
# print(song_string)


start = int(input("start number : "))
end = int(input("end number : "))
for i in range(start, end+1):
    #is_prime = True

    for k in range(2, i):
        if i % k == 0:
            #is_prime = False
            break
        else:
            print(i , end='')
