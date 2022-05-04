with open("input.txt", 'r') as f:
    seq = [int(d) for d in f.readlines()[0].strip()]

# Kieran's comment: I concatenated two .py files into one
answer = 0
for idx, d in enumerate(seq):
    if idx == 0 and d==seq[-1]:
        answer += d
    elif d == seq[idx-1]:
        answer += d

print(answer)

double_seq = seq+seq
seq_len = len(seq)
dist = int(seq_len / 2)
answer = 0
for idx, d in enumerate(seq):
    if d == double_seq[idx + dist]:
        answer += d

print(answer)
