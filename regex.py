# Stage 1 regex engine project.
# Compare a single character regex on the left to a single character string on the right divided by the symbol "|".
r, i = input().split('|')


def reg_ex(regex, inp):
    if not regex:
        return True
    elif not input:
        return False
    elif (regex == "." and len(inp) == 1) or regex == inp:
        return True
    else:
        return False


print(reg_ex(r, i))
