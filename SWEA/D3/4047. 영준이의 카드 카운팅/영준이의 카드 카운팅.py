T = int(input())
for test_case in range(1, T + 1):
    card = input()
    card_list = []
    card_kind = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    for i in range(0, len(card), 3):
        card_list.append(card[i:i + 3])
    card_set = set(card_list)
    if len(card_set) != len(card_list):
        result = "ERROR"
    else:
        for i in range(len(card_list)):
            if card_list[i][0] in card_kind.keys():
                card_kind[card_list[i][0]] -= 1
        result = str(card_kind['S']) + ' ' + str(card_kind['D']) + ' ' + str(card_kind['H']) + ' ' + str(card_kind['C'])

    print(f'#{test_case} {result}')