__author__ = 'Pavel.Malko'
COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

def cowsay(text):
    import re
    def header(width):
        return '\n ' + '_'*(width)+'\n'
    def footer(width):
        return ' ' + '-'*(width)
    def formatLine(line, width):
        return line + ' '*(width - len(line))

    filteredText = re.sub(r'\s{2,}', ' ', text)
    width = len(filteredText)

    if width > 39:
        lines = []
        filteredText += ' '
        while filteredText != '':
            spacePosistion = min(39, len(filteredText)-1)
            while filteredText[spacePosistion] != ' ' and spacePosistion != 0: spacePosistion -= 1
            if spacePosistion == 0:
                lines.append(filteredText[0:min(39,len(filteredText))])
                filteredText = filteredText[min(39,len(filteredText)):]
            else:
                lines.append(filteredText[0:spacePosistion])
                filteredText = filteredText[spacePosistion+1:]
        width = max([len(line) for line in lines])
        result = header(width+2)
        for lineIndex in range(0,len(lines)):
            if lineIndex == 0:
                result += r'/ ' + formatLine(lines[lineIndex],width) + ' \\' + '\n'
            elif lineIndex == len(lines) - 1:
                result += '\\ ' + formatLine(lines[lineIndex],width) + r' /' + '\n'
            else:
                result += r'| ' + formatLine(lines[lineIndex],width) + r' |' + '\n'
    else:
        result = header(width+2) + '< ' + filteredText + ' >\n'
    result += footer(width+2)
    return result+COW

def cmp(left,rigth):
    lenLeft,lenRigth=len(left),len(rigth)
    if lenLeft == lenRigth:
        if left == rigth: print('String are IDENTICAL!!!')
        else:
            for char in range(0,lenLeft):
                if left[char] != rigth[char]:
                    print('Wrong char in position ',char,' differnt is [', left[char], '] != [',rigth[char],']')
    else:
        for char in range(0,min(lenLeft,lenRigth)):
            if left[char] != rigth[char]:
                print('Wrong char in position ',char,' differnt is [', left[char], '] != [',rigth[char],']')
        if lenLeft > lenRigth:
            print('Left have stuff chars [',[left[i] for i in range(lenRigth,lenLeft)],']')
        else:
            print('Rigth have stuff chars [',[rigth[i] for i in range(lenLeft,lenRigth)],']')
print(cowsay("Gur Mra bs Clguba, ol Gvz Crgref  Ornhgvshy vf orggre guna htyl. Rkcyvpvg vf orggre guna vzcyvpvg. Fvzcyr vf orggre guna pbzcyrk. Pbzcyrk vf orggre guna pbzcyvpngrq. Syng vf orggre guna arfgrq. Fcnefr vf orggre guna qrafr. Ernqnovyvgl pbhagf. Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf. Nygubhtu cenpgvpnyvgl orngf chevgl. Reebef fubhyq arire cnff fvyragyl. Hayrff rkcyvpvgyl fvyraprq. Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff. Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg. Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu. Abj vf orggre guna arire. Nygubhtu arire vf bsgra orggre guna *evtug* abj. Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn. Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn. Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"))
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
                                'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
