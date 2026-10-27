def solution(coin, cards):
    n = len(cards)
    hand = set(cards[:n // 3])
    waiting = []
    round_num = 1

    for i in range(n // 3, n, 2):
        waiting.extend(cards[i:i + 2])

        found = False

        for card in list(hand):
            target = n + 1 - card
            if target in hand and card < target:
                hand.remove(card)
                hand.remove(target)
                found = True
                break

        if found:
            round_num += 1
            continue

        for card in list(hand):
            target = n + 1 - card
            if target in waiting and coin >= 1:
                hand.remove(card)
                waiting.remove(target)
                coin -= 1
                found = True
                break

        if found:
            round_num += 1
            continue

        for card in waiting:
            target = n + 1 - card
            if target in waiting and card < target and coin >= 2:
                waiting.remove(card)
                waiting.remove(target)
                coin -= 2
                found = True
                break

        if not found:
            return round_num

        round_num += 1

    return round_num