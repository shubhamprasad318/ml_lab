import random

def display(room):
    print(room)

def generate_random_dirt():
    return [[random.choice([0, 1]) for _ in range(4)] for _ in range(4)]

def clean_room(room):
    dirty_count = 0
    for x in range(4):
        for y in range(4):
            if room[x][y] == 1:
                print("Vacuum in this location now,", x, y)
                room[x][y] = 0
                print("cleaned", x, y)
                dirty_count += 1

    return dirty_count

room = generate_random_dirt()
print("All the rooms are dirty")
display(room)

dirty_count = clean_room(room)

pro = (100 - (dirty_count / 16) * 100)
print("Room is clean now. Thanks for using.")
display(room)
print('Performance =', pro, '%')
