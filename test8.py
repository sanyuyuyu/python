#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-07-29 14:56:06
# @Last Modified time: 2022-08-01 19:15:17


x = ("you are beautiful")
x.center(5)
x.rjust(15)


x = "abcdedcba"
x.count("b")
x.count("b",0,5)
x.find("b")
x.rfind("b")
x.index("b")


code = ''
    print('yes'）
        print('no')
new_code = code.expandtabs(4)
print(new_code)


‘what are you doing'.replace('what are you doing now')
table = str.maketrans("abcdefg","1234567")
"apple".translate(table)
"apple".translate(str.maketrans("abcdefg","1234567"))


x = 'i love python'
x.startswith('i')
x.endswith('love')
x.isalpha('python')


importkeyword
keyword.iskeyword('if')


'        left'.lstrip()
'rught       '.rstrip()
'    middle  '.strip()

'www.zjzs.com'.removeprefix('www.')
'zjzs.com'


'www.zjzs.com'.removesuffix('.com')
'www.zjzs'


'www.zjzs.com'.partition('.')
('www','.','zjzs.com')


'ilovefish.com/python'.rpartition('/')
('ilovefish.com','/','python')


'.'.join(['www','zjzs','com'])
'www.zjzs.com'
connect'*'.join(['f','sh','c'])
'f*sh*c'


year = 1958
"浙江邮电职业技术学院成立于 {} 年".format(year)
'浙江邮电职业技术学院成立于 1956 年'


"1+2={},2的平方是{},3的立方是{}".format(1+2,2*2,3*3*3)
"1+2=3,2的平方是4,3的立方是27"
f"1+2=,2的平方是2*2，3的立方是3*3*3"
"1+2=3,2的平方是4，3的立方是27"


"{0}{0}{1}{1}".format('yes','no')
'yesyesnono'
"{:^}".format(250)
"{left:>10}{right:<10}".format(right=520,left=250)
'250'
"{:010}".format(250)
'0000000250'
"{:010}".format(-250)
'-0000000250'
"{1:%>10}{0:%<10}".format(250,520)
'%%%%%%%250520%%%%%%%'


"{:+}{:-}".format(250,-520)
'+250 -520'


"{:b}".format(80)
'1010000'
"{:c}".format(80)
'p'
"{:d}".format(80)
'80'
"{:o}",format(80)
'120'
"{:x}",format(80)
"50"


"{:.{prec}f}",.format(3.1415,prec=2)
'3,14'
"{:{fill}{align}{width}.{prec}{ty}".format(3.1415,fill='+',align='^',width=10,prec=3,ty='g')
'+++3,14+++'
fill=‘+‘
align='^'
width=10
prec=3
ty='g'
f"{3.1415:{fill}{align}{width}.{prec}{ty}}"


t = (1,2,3)
t *=2
(1,2,3,1,2,3)
































