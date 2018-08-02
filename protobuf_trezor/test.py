fp = open('test.txt', 'r')

ctx = fp.readlines()

fp.close()
##print(ctx)
##print('==============================')
##print(ctx[0].find('/'))
##print(ctx[0][15:117])

all_string_list = []  # delete black lines
for val in ctx:
    if val[15:117] != '':  # delete black line
        all_string_list.append(val[15:117])
##print(all_string_list)

begin_index_list = []  # String begin is '3f 23 23'
index = 0
for val in all_string_list:
    if val[0:2:] == '3f' and val[3:5:] == '23' and val[6:8:] == '23':
        begin_index_list.append(index)
    index = index + 1

messages_string_list = []
for val in begin_index_list:
    temp_string = all_string_list[val] + ' ' + all_string_list[val+1]
    link_index = 2
    while all_string_list[val+link_index][:2:] == '3f' \
          and all_string_list[val+link_index][3:5:] != '23' \
          and all_string_list[val+link_index][6:8:] != '23':
        temp_string = temp_string + ' ' + all_string_list[val+link_index][3::] + ' ' + all_string_list[val+link_index+1]
        link_index = link_index + 2
    messages_string_list.append(temp_string)
print(messages_string_list)

