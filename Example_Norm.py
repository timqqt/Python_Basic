import re
#
# pattern1 = "cat"
# pattern2 = "bird"
# string = "dog runs to cat"
# print(re.search(pattern1, string))  # <_sre.SRE_Match object; span=(12, 15), match='cat'>
# print(re.search(pattern2, string))  # None
#
ptn = r"r[au]n"
# print(re.search(ptn, "dog rans to cat"))    # <_sre.SRE_Match object; span=(4, 7), match='run'>
# print(re.search(r"ab{2,10}", "abbbbb"))
# print(re.search(r"ab{2,10}", "a"))        # None No Space
# print(re.search(r"ab{2,10}", "abbbbb"))   # <_sre.SRE_Match object; span=(0, 6), match='abbbbb'>
# match = re.search(r"(\d+), Date: (.+)", "ID: 021523, Date: Feb/12/2017")
# print(match.group())                   # 021523, Date: Feb/12/2017
# print(match.group(1))                  # 021523
# print(match.group(2))                  # Date: Feb/12/2017
# match = re.search(r"(?P<id>\d+), Date: (?P<date>.+)", "ID: 021523, Date: Feb/12/2017")
# print(match.group('id'))                # 021523
# print(match.group('date'))              # Date: Feb/12/2017
# print(re.search(r"r[A-Z0-9a-z]n", "dog rUns to cat"))     # None
# print(re.search(r"r[a-z]n", "dog runs to cat"))     # <_sre.SRE_Match object; span=(4, 7), match='run'>
# print(re.search(r"r[0-9]n", "dog r2ns to cat"))     # <_sre.SRE_Match object; span=(4, 7), match='r2n'>
# print(re.search(r"r[0-9a-z]n", "dog runs to cat"))  # <_sre.SRE_Match object; span=(4, 7), match='run'>
# print(re.search(r"r[uae]n", "run ran ren"))    # ['run', 'ran']
# print(re.findall(r"r(u|a)n", "run ran ren")) # ['run', 'ran']
# print(re.sub(r"r[au]ns", "catches", "dog runs to cat"))     # dog catches to cat    # ['a', 'b', 'c', 'd', 'e']
# compiled_re = re.compile(r"r[ua]n")
# print(compiled_re.search("dog ran to cat"))  # <_sre.SRE_Match object; span=(4, 7), match='ran'>
# print(re.search(r"r.n", "r[ns to me"))