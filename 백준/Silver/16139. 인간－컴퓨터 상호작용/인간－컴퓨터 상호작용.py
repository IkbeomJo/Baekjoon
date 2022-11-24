import sys
import copy
S = input()
q = int(input())

alphabet_count_list = [0 for _ in range(26)]
S_prefix_count = list()

for i in range(len(S)):
    alphabet_count_list[ord(S[i])-97] += 1
    x = copy.deepcopy(alphabet_count_list)
    S_prefix_count.append(x)

for i in range(q):
    x, l, r = sys.stdin.readline().split()
    l, r = int(l), int(r)
    x = ord(x) - 97
    if l == 0:
        print(S_prefix_count[r][x])
    else:
        print(S_prefix_count[r][x] - S_prefix_count[l-1][x])



