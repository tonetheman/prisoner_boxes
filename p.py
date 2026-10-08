

class Box:
    def __init__(self, box_number, value):
        self.box_number = box_number
        self.value = value
    def __repr__(self):
        return f"{self.box_number} - v - {self.value}"

import random


def runthemall():
    values = list(range(1, 101))
    random.shuffle(values)
    boxes = [Box(i+1, values[i]) for i in range(100)]

    # every prisoner must find their number for the group to win
    for prisoner in range(1, 101):
        if not prisoner_finds_number(boxes, prisoner):
            return False
    return True


def prisoner_finds_number(boxes, prisoner):
    current_prison_number = prisoner
    target_prison_number = prisoner
    count = 0
    while True:
        # print(f"opening box {current_prison_number}")
        b = boxes[current_prison_number-1]
        # print("opened this box",b)
        res = b.value == target_prison_number
        if res:
            # print("found my number stopping")
            return True
            break

        count = count + 1
        # print(f"did not find my number moving on to {b.value}")
        # print()
        current_prison_number = b.value

        if count>=50:
            # print("broke for count")
            return False
            break

SIMCOUNT = 100000
_pass = 0
_fail = 0
for i in range(SIMCOUNT):
    res = runthemall()
    if res:
        _pass += 1
    else:
        _fail += 1

print("Results")
print(f"total runs   : {SIMCOUNT}")
print(f"win percent  : {_pass/SIMCOUNT}")
print(f"fail percent : {_fail/SIMCOUNT}")
