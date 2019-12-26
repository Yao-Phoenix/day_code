#!/usr/bin/env python3
from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass=ABCMeta):
    '''战斗者'''
    # 通过__slots__魔法限定对象可以绑定的成员变量
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        '''初始化方法

        :param name: 名字
        :param hp: 生命值
        '''

        self._name = name 
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        '''攻击
        :param other: 被攻击的对象
        '''
        pass

class Ultraman(Fighter):
    '''奥特曼'''
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        '''初始化方法
        :param name: 名字
        :param hp: 生命值
        :param mp: 魔法值
        '''
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)
        
    def huge_attack(self, other):
        '''究极必杀技(打掉对方至少50点或四分之三的血)
        :param other: 被攻击的对象
        :return: 使用成功返回True, 否则返回False
        '''
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False
    
    def magic_attack(self, others):
        '''魔法攻击
        :param others: 被攻击的群体
        :return: 使用魔法成功返回True, 否则返回False
        '''
        
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        '''恢复魔法值'''
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~{}奥特曼~~~\n生命值: {}\n魔法值: {}\n' \
                .format(self._name, self._hp, self._mp)

class Monster(Fighter):
    '''小怪兽'''

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~{}小怪兽~~~\n生命值: {}\n'.format(self._name, self._hp)
    
def is_any_alive(monsters):
    '''判断有没有小怪兽是活着的'''
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False

def select_alive_one(monsters):
    '''选中一只活着的小怪兽'''
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ultraman, monsters):
    '''显示奥特曼和小怪兽的信息'''
    print(ultraman)
    for monster in monsters:
        print(monster, end='')

def main():
    u = Ultraman('骆浩', 1000, 120)
    m1 = Monster('狄仁杰', 250)
    m2 = Monster('白元芳', 500)
    m3 = Monster('王大锤', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('=======第{:02d}回合======='.format(fight_round))
        m = select_alive_one(ms) # 选中一只小怪兽
        skill = randint(1, 10) # 通过随机数选择使用哪一个技能
        if skill <= 6: # 60%的概率使用普通攻击
            print('{}使用了普通攻击打了{}'.format(u.name, m.name))
            u.attack(m)
            print('{}魔法值恢复了{}点'.format(u.name, u.resume()))
        elif skill <= 9: # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
            if u.magic_attack(ms):
                print('{}使用了魔法攻击'.format(u.name))
            else:
                print('{}使用魔法失败'.format(u.name))
        else: # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.huge_attack(m):
                print('{}使用了究极必杀技虐了{}'.format(u.name, m.name))
            else:
                print('{}使用普通攻击打了{}'.format(u.name, m.name))
                print('{}魔法值恢复了{}点'.format(u.name, u.resume()))
        if m.alive > 0: # 如果选中的小怪兽没有死就回击奥特曼
            print('{}回击了{}'.format(m.name, u.name))
            m.attack(u)
            display_info(u, ms) # 每个回合结束后显示奥特曼和小怪兽的信息
            fight_round += 1
        print('\n=======战斗结束!======\n')
        if u.alive > 0:
            print('{}奥特曼胜利!'.format(u.name))
        else:
            print('小怪兽胜利!')

if __name__ == '__main__':
    main()
            
            


