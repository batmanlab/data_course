# Mult some nmbrs against a

import math,datetime
from numpy import *
random.seed(1)
a = random.normal(size=100)
def RanNumMaFunc(a1,a2):
    __a1 = math.ceil(a1)
    aa1=random.normal(size=(len(a),__a1));aa2=random.normal(size=(__a1,a2))
    _outMat1 = matmul(a,aa1); _outMat2 = matmul(_outMat1, aa2)
    d=datetime.datetime.now()
    dd = "Today's date is %s" % d
    print(dd)
    return _outMat2

