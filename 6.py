s = """Time:        56     97     77     93
Distance:   499   2210   1097   1440
"""

# times = []
# distances = []
#
# for line in s.splitlines():
#     items = line.split()
#     if len(times) == 0:
#         x = times
#     else:
#         x = distances
#     x.append(int(items[1]))
#     x.append(int(items[2]))
#     x.append(int(items[3]))
#     x.append(int(items[4]))
#
# print('test')
# num_ways = []
#
# for i in range(len(times)):
#     t = times[i]
#     d = distances[i]
#
#     count = 0
#     for press_t in range(1, t):
#         t_left = t - press_t
#         finish_d = press_t * t_left
#         if finish_d > d:
#             count = count + 1
#
#     num_ways.append(count)
#
# prod = num_ways[0]
# for i in range(1, len(num_ways)):
#     prod = prod * num_ways[i]
# print(prod)

t = None
d = None

for line in s.splitlines():
    items = line.split()
    if t is None:
        t = ''.join(items[1:])
        t = int(t)
    else:
        d = ''.join(items[1:])
        d = int(d)


count = 0
for press_t in range(1, t):
    t_left = t - press_t
    finish_d = press_t * t_left
    if finish_d > d:
        count = count + 1

print(count)
