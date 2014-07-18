import stageone

def level2check(r, _):
    if r == 'ef' or r == b'ef':
        return True
    return False

def level1check(r, _):
    if r != 6:
        return False
    return True

def retcheck(r, _):
    return r

def main():
    levels = (
        (stageone.level_notgoodtypes, level1check, None),
        (stageone.level_tryconcating, level2check, None),
        (stageone.level_mayberangefellshort, retcheck, True),
        (stageone.level_floatingnumbersnotright, retcheck, True),
        (stageone.level_indexingstringkindaconfusing, retcheck, 'h'),
        (stageone.level_shiftingisweird, retcheck, 0x80),
        (stageone.level_shiftingisweirder, retcheck, 0x01),
        (stageone.level_andingforabit, retcheck, 0x88),
        (stageone.level_bytesbutstrsame, retcheck, True),
        (stageone.level_whydifferentencoding, retcheck, True),
        (stageone.level_andsomestrings, retcheck, 'ab'),
    )


    for x in range(0, len(levels)):
        try:
            if not levels[x][1](levels[x][0](), levels[x][2]):
                print('LEVEL %s FAILED BECAUSE OF RESULT' % (x + 1))
                return
        except Exception as e:
            print('LEVEL %s FAILED BECAUSE OF EXCEPTION' % (x + 1))
            raise e
        print('LEVEL %s PASSED' % (x + 1))


    return

main()