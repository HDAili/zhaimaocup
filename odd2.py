import random as R


def zhaimao_cup():
    print("1.报名\n2.显示目前报名总人数\n3.开始随机抽取一名选手\n4.结束")


def main_code():
    while 1:
        zhaimao_cup()
        user_doing = int(input("欢迎参加摘帽杯！请输入您希望执行的操作："))
        if user_doing == 1:
            add_list()
        elif user_doing == 2:
            total_players()
        elif user_doing == 3:
            matching()
        elif user_doing == 4:
            print("已退出操作")
            break
        else:
            print("输入不合法, 请重新输入")
        continue
    return


def total_players():
    t = len(user_card)

    print("目前报名总人数为：", t)


def add_list():
    user_name = input('请输出你的昵称:')
    user_member = input('请输出你的团名称(临冬/星辰/白泽/野人):')
    players = {'昵称': user_name, '所属': user_member}
    if players in user_card:
        print("已经报过名了，报名失败")
        return main_code()
    user_card.append(players)
    print("恭喜报名成功!")


def matching():
    if len(user_card) <= 0:
        print("没有人了")
        return main_code()
    i = R.choice(user_card)
    print("抽中的选手是：", i)
    user_card.remove(i)
    print("已经匹配的选手已从匹配池中删除")


user_card = []
main_code()


'''
import random


class Matcher:
    _registry = {}
    _matched = []

    def register(self, username, group=None):
        group = group or "野人"
        if username in self._registry:
            print("User already existed in %s@%s" % (username, group))
            return
        self._registry[username] = group
        print("Succeed to register %s@%s" % (username, group))
        return

    def unregister(self, username):
        if username in self._registry:
            del self._registry[username]

    def do_match(self):
        user_names = list(self._registry.keys())
        random.shuffle(user_names)
        matched = []
        pair = []
        while True:
            if len(pair) >= 2:
                matched.append(pair)
                pair = []
            else:
                pair.append(user_names.pop())
            if len(user_names) <= 0:
                break
        if len(pair) > 0:
            print("发现孤儿: %s" % pair[0])
        self._matched = matched
        return matched

    def fmt_matched(self):
        tpl = "{} -> {}"
        out = []
        for pair in self._matched:
            rendered_text = tpl.format(*pair)
            out.append(rendered_text)
        out = "\n".join(out)
        return out


def main():
    print("匹配名单录入开始啦")
    matcher = Matcher()
    while True:
        ret = input(
            "请输入名字和骑士团名字，用空格隔开，回车键确认, 输入'--' 终止输入, 会输出匹配结果，如果是野人，请只输出名字即可："
        )
        ret = ret.strip()
        if ret == "--":
            break
        ret = ret.split()
        if len(ret) <= 0:
            print("没有任何输入，请重新输入")
            continue
        elif len(ret) == 1:
            matcher.register(ret[0])
        elif len(ret) == 2:
            matcher.register(ret[0], ret[1])
        else:
            print("输入不合法, 请重新输入")
            continue
    print("匹配结果")
    matcher.do_match()
    print(matcher.fmt_matched())
    input("按任意键退出")


if __name__ == '__main__':
    main()
'''