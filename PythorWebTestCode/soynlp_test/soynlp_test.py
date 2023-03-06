from soynlp.normalizer import emoticon_normalize, repeat_normalize

sentence = '자영업자여시들 ㅠㅠ 이모가 가게하시는데 배달의 민 족 기본배달팁을 올려야하는데 혹시 어떻게 올리는지 알아 ㅜㅜ!? ㅠㅠ 아는 여시있나여 ㅠㅠ'

print(emoticon_normalize(sentence, num_repeats=1))
