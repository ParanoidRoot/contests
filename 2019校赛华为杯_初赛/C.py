#@Time  : 2019/5/18 11:23
#@Author: Root
#@File  : C.py


zeroStr = " - | |   | | - "
oneStr = "     |     |   "
twoStr = " -   | - |   - "
threeStr = " -   | -   | - "
fourStr = "   | | -   |   "
fiveStr = " - |   -   | - "
sixStr = " - |   - | | - "
sevenStr = " -   |     |   "
eightStr = " - | | - | | - "
nighStr = " - | | -   | - "
plusStr = "       +       "
minusStr = "       -       "

m = {
    zeroStr : "0",
    oneStr : "1",
    twoStr : "2",
    threeStr : "3",
    fourStr : "4",
    fiveStr : "5",
    sixStr : "6",
    sevenStr : "7",
    eightStr : "8",
    nighStr : "9",
    plusStr : "+",
    minusStr : "-",
    "-" : minusStr,
    "0" : zeroStr,
    "1" : oneStr,
    "2" : twoStr,
    "3" : threeStr,
    '4' : fourStr,
    "5" : fiveStr,
    "6" : sixStr,
    "7" : sevenStr,
    "8" : eightStr,
    "9" : nighStr,
}


def change2NumberStr(term) :
    """
    将其转换成一个数字或者
    :param term:
    :return:
    """
    ans = ""
    for line in term :
        ans += "".join(line)
    return m[ans]

def change2MStr(number : str) :
    """
    将number转换成火柴输出
    :param number:
    :return:
    """
    t = m[number]
    ans = []
    for i in range(0, 15, 3) :
        ans.append(t[i : i + 3])
    return ans

def changeNumber(number : int) :
    """

    :param number:
    :return:
    """
    p = []
    if number < 0 :
        p.append(change2MStr("-"))
    s = str(abs(number))
    for d in s :
        temp = change2MStr(d)
        p.append(temp)
    for i in range(5) :
        line = ""
        for t in p :
            line += t[i]
        print(line)





def solve() :
    inputs = [input() for i in range(5)]
    l = len(inputs[0])
    termNumber = l // 3

    terms = [[inputStr[i * 3: i * 3 + 3] for inputStr in inputs] for i in range(termNumber)]

    e = ""
    for term in terms :
        e += change2NumberStr(term)
    ans = eval(e)
    changeNumber(ans)

if __name__ == "__main__" :

    t = input()
    for i in range(int(t)) :
        solve()

