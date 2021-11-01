# 1.分析一个水杯的属性和功能，使用类描述并创建对象
# 高度，容积，颜色，材质
# 能存放液体


class water_cup:
    __height = 0
    __volume = 0
    __color = ""
    __material = ""

    def set_height(self, height):
        if height.isdigit():
            height = float(height)
            if height <= 30:
                self.__height = height
            else:
                print("这水杯也太高了吧！")
                return -1
        else:
            print("高度输入非法，别瞎输入！")
            return -1

    def get_height(self):
        return self.__height

    def set_volume(self, volume):
        if volume.isdigit():
            volume = float(volume)
            if volume <= 2000:
                self.__volume = volume
            else:
                print("这水杯也太大了吧？")
                return -1
        else:
            print("容量输入非法,别瞎输入！")
            return -1

    def get_volume(self):
        return self.__volume

    def set_color(self, color):
        if color == "":
            print("颜色输入非法,别瞎输入！")
            return -1
        else:
            self.__color = color

    def get_color(self):
        return self.__color

    def set_material(self, material):
        if material == "":
            print("材质输入非法，别瞎输入！")
            return -1
        else:
            self.__material = material

    def get_material(self):
        return self.__material

    # 放入液体
    def liquid(self, liquid):
        if liquid.isdigit():
            liquid = float(liquid)
            if liquid <= self.__volume:
                print("一个高%.2f厘米,容积%.2fml,%s颜色,用%s作材质的水杯,它正盛入%.2fml的水" %
                      (self.__height, self.__volume, self.__color, self.__material, liquid))
                return 1
            else:
                print("您的水杯装不了这么多水，别瞎弄！")
                return -1
        else:
            print("水的容积输入非法，别瞎输入！")
            return -1


# height = input("请输入水杯的高度cm：")
# volume = input("请输入水杯的容量ml：")
# color = input("请输入水杯的颜色：")
# material = input("请输入水杯的材质：")
# liquid = input("请输入水的容积：")
#
# cup = water_cup()
# cup.set_height(height)
# cup.set_volume(volume)
# cup.set_color(color)
# cup.set_material(material)
#
# cup.liquid(liquid)

# 有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
class computer:
    __screen = 0
    __price = 0
    __cpu = ""
    __ram = 0
    __bide = ""

    def set_screen(self, screen):
        if screen <= 0 or screen > 25:
            print("屏幕大小非法,别瞎输入！")
        else:
            self.__screen = screen

    def get_screen(self):
        return self.__screen

    def set_price(self, price):
        if price < 0 or price > 99999:
            print("你的电脑这么贵吗？")
        else:
            self.__price = price

    def get_price(self):
        return self.__price

    def set_cpu(self, cpu):
        if cpu == "":
            print("没有这种cpu,别瞎输入!")
        else:
            self.__cpu = cpu

    def get_cpu(self):
        return self.__cpu

    def set_ram(self, ram):
        if ram < 0 or ram > 20:
            print("什么个人笔记本电脑有这么大的内存，能推荐一下吗？")
        else:
            self.__ram = ram

    def get_ram(self):
        return self.__ram

    def set_bide(self, bide):
        if bide < 0 or bide > 120:
            print("电脑最长待机120分钟，别瞎输入！")
        else:
            self.__bide = bide

    def get_bide(self):
        return self.__bide

    def size(self):
        print('''本电脑的规格参数：
                                屏幕大小：{}英寸
                                价格：￥{}
                                cpu型号：{}
                                运行内存：{}G
                                设置待机时间：{}分钟'''.format(self.__screen, self.__price, self.__cpu, self.__ram, self.__bide))

    def typing(self, username, time, bide):
        if bide < self.__bide:
            print("%s花了￥%.2f买了本电脑,用本电脑打字，已经打了%d分钟,现在电脑正在待机中,已经待了%d分钟" % (username, self.__price, time, bide))
        else:
            print("%s花了￥%.2f买了本电脑,用本电脑打字，已经打了%d分钟,现在电脑已关机" % (username, self.__price, time))

    def game(self, username, game):
        print("%s买了花了￥%.2f买了本电脑,正在用本电脑玩%s,电脑cpu%s已经快要坚持不住了" % (username, self.__price, game, self.__cpu))

    def video(self, username, video, ram):
        print("%s花了￥%.2f买了本电脑,正在用本电脑看%s,电脑剩余空闲内存%dG" % (username, self.__price, video, self.__ram - ram))


com = computer()
com.set_screen(15.6)
com.set_price(6345.6)
com.set_cpu('i9-7900X')
com.set_ram(16)
com.set_bide(60)
com.size()
com.typing("张三", 188, 59)
com.game("李四", "吃鸡")
com.video("王五", "火影", 10)
