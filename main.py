import stageone

def level2check(r):
    if r == 'ef' or r == b'ef':
        return True
    return False

def level1check(r):
    if r != 6:
        return False
    return True

def truecheck(r):
    return r

def main():
    levels = (
        (stageone.level1, level1check),
        (stageone.level2, level2check),
        (stageone.level3, truecheck),
        (stageone.level4, truecheck),
    )


    for x in range(0, len(levels)):
        try:
            if not levels[x][1](levels[x][0]()):
                print('LEVEL %s FAILED BECAUSE OF RESULT' % (x + 1))
                return
        except Exception as e:
            print('LEVEL %s FAILED BECAUSE OF EXCEPTION' % (x + 1))
            raise e
        print('LEVEL %s PASSED' % (x + 1))


    return

main()