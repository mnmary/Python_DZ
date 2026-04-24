# --------------------------------------------------------- #
def boys_and_girls(boys: list, girls: list):
    result = ""  # в эту строку сохраните полученные пары или сообщение "Кто-то может остаться без пары!"

    if len(boys) == len(girls):  # проверьте, что длины списков одинаковы
        for i, j in zip(sorted(boys),
                        sorted(girls)):  # отсортируйте пары, объедините при помощи zip и распакуйте в цикле
            result += str(i) + " и " + str(j) + ", "
        result = result[:-2]
    else:
        result = "Кто-то может остаться без пары!"
    print(result)
    return result

# --------------------------------------------------------- #
def winner(hare_distances: list, turtle_distances: list):
    hare_all = 0 # подсчитайте общую дистанцию зайца
    for cnt in hare_distances:
        hare_all += int(cnt)
    turtle_all = 0 # подсчитайте общую дистанцию черепахи
    for cnt in turtle_distances:
      turtle_all += int(cnt)
    # определите, кто из двоих прошел бОльшую дистанцию
    if hare_all > turtle_all:
        result = "заяц"
    elif hare_all < turtle_all:
        result = "черепаха"
    else:
        result = "одинаково"
    return result
# --------------------------------------------------------- #

def konkurs(receipts: list):
    result = receipts[2::3]  # получите правильный срез списка receipts
    # print(result)
    return result, len(result)  # этот код менять не нужно


import pytest
@pytest.mark.parametrize(
        'hare_distances,turtle_distances, expected',
        (([8, 5, 3, 2, 0, 1, 1], [3, 3, 3, 3, 3, 3, 3], "черепаха"),
         ([8, 5, 3, 2, 2, 1, 1], [3, 3, 3, 3, 3, 3, 3], "заяц"),
         ([8, 5, 3, 2, 1, 1, 1], [3, 3, 3, 3, 3, 3, 3], "одинаково"))
    )
def test_winner(hare_distances, turtle_distances, expected):
        result = winner(hare_distances, turtle_distances)
        assert result == expected, \
            f'Ожидаемый результат {expected} не соответствует расчетному {result}'


@pytest.mark.parametrize(
        'boys,girls, expected',
        ((['Peter', 'Alex', 'John', 'Arthur', 'Richard'], ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'], "Alex и Emma, Arthur и Kate, John и Kira, Peter и Liza, Richard и Trisha"),
         (['Peter', 'Alex', 'John', 'Arthur'], ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'], "Кто-то может остаться без пары!"),
         (['Peter', 'Alex', 'John', 'Arthur', 'Richard'], ['Kate', 'Liza', 'Kira', 'Emma'], "Кто-то может остаться без пары!"))
    )
def test_boys_and_girls(boys: list, girls: list, expected):
        result = boys_and_girls(boys, girls)
        assert result == expected, \
            f'Ожидаемый результат {expected} не соответствует расчетному {result}'

@pytest.mark.parametrize(
        'receipts, expected',
        (([123, 145, 346, 246, 235, 166, 112, 351, 436], [346, 166, 436]),
         ([123, 145], []))
    )
def test_konkurs(receipts, expected):
        result, len_result = konkurs(receipts)
        assert result == expected and len_result == len(expected), \
            f'Ожидаемый результат {expected} len = {len(expected)} не соответствует расчетному {result} len = {len_result}'
