import sys, re
print(sum(len(s.strip()) - len(re.findall(r'([a-z]|\\\\|\\"|\\x[0-9a-f]{2})', s.strip())) for s in open(sys.argv[1]).readlines()))
print(sum(len(re.findall(r'("|\\)', s.strip())) + 2 for s in open(sys.argv[1]).readlines()))
