segments = []
cnt_of_segments = int(input())
for i in range(1, cnt_of_segments+1):
    x, y = map(int, input().split()) # 4.5 3 6.2 2 9 14.2 1.2 4 8.7
    segments.append([x, y])

segments.sort()

start = 0
end = 0
common_segment = False
common_dots = []
for i in range(len(segments)):
    if common_segment == False:
        start = segments[i][0]
        end = segments[i][1]
        common_segment = True
        continue
    if end >= segments[i][0]:
        start = segments[i][0]
        end = min(end, segments[i][1])
    else:
        common_dots.append(end)
        start = segments[i][0]
        end = segments[i][1]

if common_segment:
    common_dots.append(end)

print(len(common_dots))
print(*common_dots, sep = ' ')




    

        
    
'''
number = pointsCover(segments)
print(f'Минимальное количество отрезков: {len(number)}')  # Минимальное количество отрезков: 6
print(*number, sep=', ')  # [1.2, 2.2], [3.0, 4.0], [4.5, 5.5], [6.2, 7.2], [8.7, 9.7], [14.2, 15.2]
'''
