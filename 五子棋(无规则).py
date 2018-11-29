#Time 10:00
#Writer Yang
#正在课程设计hhh
#在游戏中默认黑棋为O，白棋为X

import time

class ChessBoard(object):
    size = 15
    def __init__(self):
        self.board = [['+' for i in range(0,self.size+1)]for j in range(0,self.size+1)]#设置棋盘初始值

    def print_board(self): # 初始化＆打印棋盘
        self.board[0][0] = '' # 把 0 0位置变为空的
        for m in range(1,self.size+1):
            self.board[0][m] = m  # self.board[行][列] 设置横向序列
            self.board[m][0] = m  #设置纵列序列
        for i in self.board:
            for j in i:
                print(j,end='\t')
            print('')

    def set_chess(self,x,y,color):
        self.x = x
        self.y = y
        self.board[self.x][self.y] = color



class GameStart(object): #开始游戏的界面(询问)
    def __init__(self):
        pass

    # 初始界面
    def start(self):
        print('=======================================================================================')
        print('=======================================================================================')
        print('==                                                                                   ==')
        print('==   ===================      ===================       ===        ==    ==          ==')
        print('==           ==                            ====          ==      ============        ==')
        print('==           ==                         ====             ==        ==    ==          ==')
        print('==           ==                       ====            ========     ========          ==')
        print('==   =================       ==================        = == =      ==    ==          ==')
        print('==          ==      ==               ==                = == =      ========          ==')
        print('==          ==      ==               ==               =  ==  =     ==    ==          ==')
        print('==          ==      ==           ==  ==              =   ==   =  ============        ==')
        print('==   ===================            ===                  ==       ===    ===         ==')
        print('==                                                                                   ==')
        print('=======================================================================================')
        print('=======================================================================================')

    # 此处有问题未解决！！！！
    def choose(self): # 选择游戏方（选择黑白棋，默认黑棋先手）
        print('请问您想用黑棋还是白棋，黑棋先手，白棋后手。请选择(B代表黑棋，W代表白棋):')
        flag = input('输入B或者W>>>') #定义一个标识位
        time.sleep(0.5)
        print('游戏即将开始')
        time.sleep(0.5)
        if flag == 'B'or'b':
            return flag
        elif flag == 'W'or'w':
            return flag



class Set_Black(object): # 黑棋下棋
    def __init__(self):
        pass
    #初始化

    def set(self):
        print('请下黑棋：输入位置行列坐标，先输入行坐标再输入列坐标')
        color = 'O'
        # 接收输入的全部字符串
        while 1:
            black_x = int(input('行>>>(输入完成请按回车键)'))
            black_y = int(input('列>>>(输入完成请按回车键)'))
            if black_x > ChessBoard.size or black_y > ChessBoard.size :
                print('输入的坐标不对哦，请重新输入（纵横作弊需要大于0小于%d）' % ChessBoard.size)
                continue
            # chess.set_chess(black_x,black_y,color)
            else:
                return black_x,black_y,color # 返回横竖坐标


class Set_White(object): #与黑棋下棋类似
    def __init__(self):
        pass
    # 类初始化

    def set(self):
        print('请下白棋：输入位置行列坐标，先输入行坐标再输入列坐标')
        color = 'X'
        # 接收输入的全部字符串
        while 1:
            white_x = int(input('行>>>(输入完成请按回车键)'))
            white_y = int(input('列>>>(输入完成请按回车键)'))
            if white_x > ChessBoard.size or white_y > ChessBoard.size :
                print('输入的坐标不对哦，请重新输入（纵横作弊需要大于0小于%d）' % ChessBoard.size)
                continue
            else:
                return white_x, white_y, color  # 返回横竖坐标

def f_black(): # 黑棋先下的类
    chess.print_board()
    bx, by, bc = set_b.set()
    chess.set_chess(bx, by, bc)
    time.sleep(0.5)
    print('黑棋已下，轮换白棋玩家...')
    #在运行该类之后最好加延时0.5s

def f_white(): # 白棋先下的类
    chess.print_board()
    wx, wy, wc = set_w.set()
    chess.set_chess(wx, wy, wc)
    time.sleep(0.5)
    print('白棋已下，轮换黑棋玩家...')
    #在运行该类之后最好加延时0.5s



chess = ChessBoard()
set_b = Set_Black()
set_w = Set_White()
gamestart = GameStart()

def main1(): # 测试棋盘
    chess.print_board()
    # 完成
# main1()

def main2(): # 测试摆放棋子
    chess.print_board() # 打印棋盘
    x,y,c = set_b.set() # 接收横纵位置和颜色
    chess.set_chess(x,y,c) # 在ChessBoard中调用setchess函数放置棋子
    chess.print_board() # 打印棋盘
    # 完成
# main2()
#测试单独的放子
# chess.set_chess(1,1,'0')
# chess.print_board()

def main3(): #测试黑白棋轮下
    while 1:
        #黑棋先手下
        chess.print_board()
        bx,by,bc = set_b.set()
        chess.set_chess(bx,by,bc)
        time.sleep(0.5)
        print('黑棋已下，轮换白棋玩家...')
        #白棋下
        time.sleep(0.5)
        chess.print_board()
        wx,wy,wc = set_w.set()
        chess.set_chess(wx,wy,wc)
        time.sleep(0.5)
        print('白棋已下，轮换黑棋玩家...')
        time.sleep(0.5)
        # 完成
# main3()

def main4(): # 测试半成品
    gamestart.start()
    Flag = gamestart.choose()
    print(Flag)
    if Flag == 'B': #黑子先行
        while 1:
            f_black()
            time.sleep(0.5)
            f_white()
            time.sleep(0.5)
    else:
        while 1:
            f_white()
            time.sleep(0.5)
            f_black()
            time.sleep(0.5)
main4()



def anyone_win(self, x, y):
    state = self.get_xy_on_logic_state(x, y)
    for directions in self.__dir:  # 对米字的4个方向分别检测是否有5子相连的棋
        count = 1
        for direction in directions:  # 对落下的棋子的同一条线的两侧都要检测，结果累积
            point = (x, y)
            while True:
                if self.get_xy_on_direction_state(point, direction) == state:
                    count += 1
                    point = sedirectionslf.get_next_xy(point, direction)
                else:
                    break
        if count >= 5:
            return state
    return EMPTY