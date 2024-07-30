N = int(input())

word_set = set()
for i in range(N):
    word_set.add(input())

word_list = list(word_set)
word_list.sort(key = lambda x : (len(x), x))
for i in word_list:
    print(i)
