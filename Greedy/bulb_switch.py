def bulb_switch(inital_state):
    n_switch = 0
    # if n_switch is odd -> the current state will be reverse of the old state
    # if n_switch is odd and bulb is 1 (bulb is actually 0) -> n_switch + 1
    # if n_switch is even and bulb is 0 (bulb is actually 1) -> n_switch + 1
    # if n_switch is odd and bulb is 0 -> nothing to do
    # if n_switch is even and bulb is 1 -> nothing to do
    # if previously_switched

    for bulb in inital_state:
        if (n_switch % 2 != 0 and bulb == 1) or (n_switch % 2 == 0 and bulb == 0):
            n_switch += 1

    return n_switch


def main():
    inital_state = [0, 1, 0, 1]
    print(bulb_switch(inital_state=inital_state))
    # 0, 1, 0, 1 -> initial
    # 1, 0, 1, 0 -> 1
    # 1, 1, 0, 1 -> 2
    # 1, 1, 1, 0 -> 3
    # 1, 1, 1, 1 -> 4

    inital_state = [0, 0, 0, 0]
    print(bulb_switch(inital_state=inital_state))
    # 0, 0, 0, 0 -> initial
    # 1, 1, 1, 1 -> 1

    inital_state = [1, 1, 1, 1]
    print(bulb_switch(inital_state=inital_state))

    inital_state = [0, 0, 1, 0, 1, 1, 0]
    print(bulb_switch(inital_state=inital_state))
    # 0, 0, 1, 0, 1, 1, 0 -> initial
    # 1, 1, 0, 1, 0, 0, 1 -> 1
    # 1, 1, 1, 0, 1, 1, 0 -> 2
    # 1, 1, 1, 1, 0, 0, 1 -> 3
    # 1, 1, 1, 1, 1, 1, 0 -> 4
    # 1, 1, 1, 1, 1, 1, 1 -> 5

if __name__ == '__main__':
    main()