#@Time  : 2019/5/17 13:37
#@Author: Root
#@File  : Utility.py

import enum
import os
from  gensim.models import KeyedVectors
import heapq
import xlrd
import jieba
import os

# 注意这个类一定要先初始化类的静态成员
class Majors(object):


    majorSet = None  # 成员变量表示所有的专业标签的集合
    cnsWordModel = None
    hotMajors = None

    def __init__(self, majors) :
        if Majors.cnsWordModel == None :
            Majors.initializeClass()
        self.majorSet = majors

    @classmethod
    def overlaps(cls, word1, word2) :
        return word1 in word2 or word2 in word1


    def getTopNSimilarity(self, word, N : int = 1) :
        """
        返回一个词与
        :param word:
        :return:
        """
        q = []
        if not Majors.hotMajors :
            raise Exception("Major类没有初始化")
        for major in self.majorSet :
            try :
                k = self.cnsWordModel.similarity(major, word)
                if Majors.overlaps(major, word) :
                    k = 0.85
                heapq.heappush(q, (-k, major) )
            except :
                pass
        i = 0
        ansList = []
        while i < N and len(q) :
            t = heapq.heappop(q)
            ansList.append((-t[0], t[1]) )
            i += 1
        if ansList :
            return ansList
        else :
            ansList.append(0.1)
            for major in self.majorSet :
                partsOfMajor = jieba.cut(major)
                ansList.append(max([self.cnsWordModel.similarity(part, word) for part in partsOfMajor]))
            return [(max(ansList), 0)]

    @classmethod
    def initializeClass(cls, path : str = r".\data\sgns.zhihu.bigram-char") :
        print("正在读入预训练词向量".center(25, "*"))
        Majors.cnsWordModel = KeyedVectors.load_word2vec_format(path, binary=False)
        print("读入预训练词向量完毕".center(25, "*"))
        cls.hotMajors = {"计算机", "经济", "人工智能", "金融", "电子"}





class SchoolOfYear(object) :
    schoolName = ""
    schoolId = ""
    schoolProvince = ""
    year = ""


# 读取txt文件
class TextHelper(object) :

    """
    # 在这个类中要完成对文本txt的信息提取
    """





# 读取xls文件
class XlsHelper(object) :

    """
    # 在这个类中完成对xls的信息读取
    """
    @classmethod
    def readInXlsByCol(cls, path, sheetName, col) :
        """
        通过列读入xls文件
        :param path:
        :return:
        """
        workBook = xlrd.open_workbook(path)
        workSheet = workBook.sheet_by_name(sheetName)
        colValues = workSheet.col_values(col)
        return colValues

    @classmethod
    def write2XlsByCol(cls, colValues, colIndex, toPath) :
        """
        将一列list写入toPath的某一列
        :param colValues:
        :param colIndex:
        :param toPath:
        :return:
        """



if __name__ == "__main__" :
    thisPath = os.getcwd()
    # Majors.initializeClass()
    # print(Majors.getTopNSimilarity("土木工程", N=3))
    # p1 = r"data\allColleges.xlsx"
    # p1 = os.path.join(thisPath, p1)
    # p2 = r"data\school2majors.xlsx"
    # p2 = os.path.join(thisPath, p2)
    # p3 = r"data\final.xlsx"
    # p3 = os.path.join(thisPath, p3)
    # totalWorkBook = openpyxl.load_workbook(p1)
    # school2MajorsWorkBook = openpyxl.load_workbook(p2)
    # finalWorkBook = openpyxl.load_workbook(p3)
    # totalWorkSheet = totalWorkBook.worksheets[0]
    # school2MajorsWorkSheet = school2MajorsWorkBook.worksheets[0]
    # finalWorkSheet = finalWorkBook.worksheets[0]
    #
    # # 处理total中的学校变成一个字典
    # maxRow = totalWorkSheet.max_row
    # totalSchool2RowDict = dict()
    # # 2行2列为学校名
    # for i in range(2, maxRow + 1) :
    #     totalSchool2RowDict[totalWorkSheet.cell(i, 2).value] = i
    #
    # print(totalSchool2RowDict)
    #
    # # 开始遍历school2majors
    # maxRow = school2MajorsWorkSheet.max_row
    # # 1行1列开始为学校名
    # k = 1
    # for i in range(1, maxRow + 1) :
    #     schoolName = school2MajorsWorkSheet.cell(i, 1).value
    #     if schoolName in totalSchool2RowDict.keys() :
    #         r = totalSchool2RowDict[schoolName]
    #         rowValues = [ totalWorkSheet.cell(r, col).value for col in range(1, 11)]
    #         rowValues.append(school2MajorsWorkSheet.cell(i, 2).value)
    #         for c, v in enumerate(rowValues) :
    #             finalWorkSheet.cell(k, c + 1, v)
    #         k += 1
    # finalWorkBook.save(p3)







