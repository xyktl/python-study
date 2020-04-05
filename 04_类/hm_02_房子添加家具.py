#创建家具类   包含  naem(民称)   area(面积)  属性
class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area
    def __str__(self):
        return "%s %.2fm²"%(self.name, self.area)


#创建房子类  包含  house_style  area(面积) free_area(剩余面积)   list  属性
#                add_item(添加家具)                       方法


class House:
    def __init__(self,house_style,area):
        self.house_style = house_style
        self.area = area
        self.free_area = area
        self.item_list = []
    def __str__(self):
        return ("户型：%s\n总面积：%s\n剩余面积：%s\n家具列表：%s"
                %(self.house_style,self.area,self.free_area,self.item_list))
    def add_item(self,item):
#判断面积面积是否可以添加家具
        if item.area >= self.free_area:
            print("房子面积不足，添加家具失败！")
            return
#添加家具
        self.item_list.append(item.name)
        self.free_area = self.area - item.area
        print("添加了一个%s"%(item.name))


def main():
    ximengsi = HouseItem("席梦思", 5)
    shuzhuo = HouseItem("书桌", 3.1555)
    bed = HouseItem("床", 200)
    my_house = House("两室一厅",100)
    my_house.add_item(shuzhuo)
    print(my_house)


if __name__ == "__main__":
    main()