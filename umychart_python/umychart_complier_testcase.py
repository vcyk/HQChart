import sys
from umychart_complier_jscomplier import JSComplier, SymbolOption, HQ_DATA_TYPE

from umychart_complier_jscomplier import ScriptIndexConsole, ScriptIndexItem, SymbolOption, RequestOption, HQ_DATA_TYPE, ArgumentItem

class TestCase :
    def __init__(self, code, option=SymbolOption()) :
        self.Code=code
        self.Option=option
    def Run(self):
        testCode=''
        for item in self.Code:
            testCode+=item
            testCode+='\n'

        result=JSComplier.Execute(testCode,self.Option)
        return True if result else False 
        

def Test_Tokenize():
    code1='VARHIGH:=IF(VAR1<=REF(HH,-1),REF(H,BARSLAST(VAR1>=REF(HH,1))),DRAWNULL),COLORYELLOW;'
    code2='VAR1=((SMA(MAX((CLOSE - LC),0),3,1) / SMA(ABS((CLOSE - LC)),3,1)) * 100);'
    tokens=JSComplier.Tokenize(code1+code2)
    return True if tokens else False

def Test_Parse():
    code1='VARHIGH:=IF(VAR1<=REF(HH,-1),REF(H,BARSLAST(VAR1>=REF(HH,1))),DRAWNULL),COLORYELLOW;'
    code2='VAR1=((SMA(MAX((CLOSE - LC),0),3,1) / SMA(ABS((CLOSE - LC)),3,1)) * 100);'
    ast=JSComplier.Parse(code1+code2)
    return True if ast else False

def Test_REF():
    result=JSComplier.Execute('VAR2:C-REF(O,1)')
    return True if result else False

def Test_Add() :
    result=JSComplier.Execute('VAR2:C+100')
    return True if result else False 

def Test_Multiply():
    code=[
        'VAR2:C*O;', 
        "VAR3:100*100;"
        ]
    result=JSComplier.Execute(code[0]+code[1])
    return True if result else False 


def Test_MAX_MIN():
    code=[
        'VAR2:MAX(C,O);', 
        "VAR3:MAX(C,100);",
        "VAR4:MAX(100,C);",
        'VAR5:MIN(C,O);',
        'VAR5:MIN(C,4);'
        ]
    result=JSComplier.Execute(code[0]+code[1]+code[2]+code[4]+code[3])
    return True if result else False 

def Test_MA() :
    code=[
        'VAR2:MA(C,5);', 
        'VAR3:MA(C,10);',
        'VAR4:MA(C,15);',
        'VAR4:MA(C,30);', 
        'VAR4:MA(C,33);', 
        ]

    result=JSComplier.Execute(code[0]+code[1]+code[2]+code[3])
    return True if result else False 

def Test_EMA():
    code=[
        'VAR2:EMA(C,5);', 
        'VAR3:EMA(C,10);',
        'VAR4:EMA(C,15);',
        'VAR4:EMA(C,30);', 
        ]
    result=JSComplier.Execute(code[0]+code[1]+code[2]+code[3])
    return True if result else False 

def Test_SMA():
    code=[
        'VAR2:SMA(C,5,10);', 
        'VAR3:SMA(C,10,10);',
        'VAR4:SMA(C,15,10);',
        'VAR4:SMA(C,30,10);', 
        ]
    result=JSComplier.Execute(code[0]+code[1]+code[2]+code[3])
    return True if result else False 

def Test_DMA():
    code=[
        'VAR3:C;',
        'VAR2:DMA(C,O/C);', 
        ]
    result=JSComplier.Execute(code[0]+code[1])
    return True if result else False 

def Test_WMA() :
    code=[
        'VAR3:C;',
        'VAR2:WMA(C,20);', 
        ]
    result=JSComplier.Execute(code[0]+code[1])
    return True if result else False 

def Test_SUMBARS() :
    code=[
        'VAR3:SUMBARS(C,O)',
        'VAR2:C;', 
        ]

    option=SymbolOption()
    option.Symbol='000001.sz'
    option.HQDataType=HQ_DATA_TYPE.MINUTE_ID
    result=JSComplier.Execute(code[0]+code[1],option)
    return True if result else False 

def Test_INDEX():
    code=[
        'VAR3:INDEXA;',
        'VAR2:INDEXC;', 
        'VAR2:INDEXO;', 
        ]

    option=SymbolOption()
    option.Period=5

    result=JSComplier.Execute(code[0]+code[1]+code[2],option)
    return True if result else False 

def Test_COUNT():
    code=[
        'VAR3:COUNT(C,5);',
        'VAR2:COUNT(O,10);', 
        'VAR2:COUNT(H,20);', 
        ]

    option=SymbolOption()

    result=JSComplier.Execute(code[0]+code[1]+code[2],option)
    return True if result else False 

def Test_HHV_HHL() :
    case =TestCase(
        code=[
        'VAR3:HHV(C,5);',
        'VAR2:HHV(O,10);', 
        'VAR2:HHV(H,20);', 
        'VAR3:LLV(H,5);',
        'VAR4:LLV(H,10);',
        ])

    result=case.Run()
    return result

def Test_STD():
    case =TestCase(
        code=[
        'VAR3:STD(C,5);',
        'VAR2:STD(O,10);', 
        'VAR2:STD(H,20);', 
        'VAR3:STD(H,15);',
        'VAR4:STD(H,0);',
        ])

    result=case.Run()
    return result

def Test_AVEDEV():
    case =TestCase(
        code=[
        'VAR3:AVEDEV(C,5);',
        'VAR2:AVEDEV(O,10);', 
        'VAR2:AVEDEV(H,20);', 
        'VAR3:AVEDEV(H,15);',
        'VAR4:AVEDEV(H,0);',
        ])

    result=case.Run()
    return result

def Test_CROSS() :
    case =TestCase(
        code=[
        'VAR3:CROSS(C,O);',
        'VAR2:CROSS(O,10);', 
        'VAR2:CROSS(O,C);', 
        ])

    result=case.Run()
    return result

def Test_MULAR() :
    case =TestCase(
        code=[
        'VAR3:MULAR(C,5);',
        'VAR2:MULAR(O,10);', 
        'VAR2:MULAR(O,30);', 
        ])

    result=case.Run()
    return result


def Test_SUM() :
    case =TestCase(
        code=[
        'VAR3:SUM(C,5);',
        'VAR2:SUM(O,0);', 
        'VAR2:BARSCOUNT(O);', 
        ])

    result=case.Run()
    return result


def Test_DEVSQ():
    case =TestCase(
        code=[
        'VAR3:DEVSQ(C,5);',
        'VAR2:DEVSQ(O,0);', 
        'VAR2:DEVSQ(O,5);', 
        ])

    result=case.Run()
    return result

def Test_FINANCE(): # 财务数据测试
    case =TestCase(
        code=[
        'DRAWLINE(HIGH>=HHV(HIGH,20),HIGH,LOW<=LLV(LOW,20),LOW,1);'
        'VAR4:CAPITAL;',
        'VAR3:FINANCE(32);',
        'VAR2:FINANCE(1);', 
        'VAR2:MA(FINANCE(33),5);', 
        "DRAWTEXT(C<=O,O,'xxxx');",
        'STICKLINE(CLOSE>OPEN, CLOSE, OPEN, 0.8, 1);',
        'DRAWNUMBER(CLOSE/OPEN>1.0001,LOW,C);',
        'DRAWNUMBER(CLOSE/OPEN>1.0001,LOW,33);',
        'DRAWICON(CLOSE>OPEN,LOW,1);',
        'PLOYLINE(HIGH>=HHV(HIGH,20),HIGH);',
        'CYW: SUM(VAR4,10)/10000, COLORSTICK;',
        ])

    result=case.Run()
    return result

def Test_ScriptIndexConsole():

    # 创建脚本, 及参数
    scpritInfo=ScriptIndexItem(name='测试脚本', id=888888,
        script='MA1:MA(CLOSE,M1);\n'    # 指标脚本代码
            'MA2:MA(CLOSE,M2);\n'
            'MA3:MA(CLOSE,M3);',
        args=[ ArgumentItem(name='M1', value=5), ArgumentItem(name='M2', value=10), ArgumentItem(name='M3', value=20) ] # 参数
        )

    indexConsole = ScriptIndexConsole(scpritInfo)

    option = SymbolOption(
        symbol='000001.sz',
        right=1, # 复权 0 不复权 1 前复权 2 后复权
        period=5 # 周期 0=日线 1=周线 2=月线 3=年线 4=1分钟 5=5分钟 6=15分钟 7=30分钟 8=60分钟
        )
    indexConsole.ExecuteScript(option)



#Test_Add()
#Test_Multiply()
#Test_MAX_MIN()
#Test_FINANCE()

Test_ScriptIndexConsole()