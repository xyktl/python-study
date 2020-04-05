# 在Python中，最有名的ORM框架：Object-Relational Mapping，把关系数据库的表结构映射到对
# 象上是SQLAlchemy。我们来看看SQLAlchemy的用法。

from sqlalchemy import Column, String, create_engine, ForeignKey, Integer
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()
# 初始化数据库连接  ：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine("mysql+mysqlconnector://root:c1635976271@localhost:3306/runoob_db")

# 定义User对象


# 定义两张表，user和book，user中的id是主键，book中的id是主键，并且book中定义user_id外键(user_id=user.id)
class User(Base):
        # 表的名称
    __tablename__ = "user"
    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    books = relationship("Book")


class Book(Base):
    __tablename__ = "book"
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    user_id = Column(String(20), ForeignKey("user.id"))


# 创建user和book表
Base.metadata.create_all(engine)


# 创建DBSession基类  ，DBSession对象可视为当前数据库连接
DBSession = sessionmaker(bind=engine)
# 创建session对象
session = DBSession()
# new_user = User(id="5", name="Mike")
# session.add(new_user)
# session.commit()
# user 要是一个table对象 不然会报错
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user1 = session.query(User).filter(User.id == "5").one()
# user = session.query(User).filter(User.books)
print("type:", type(user1))
print("name:", user1.name)
# 遍历查询表的数据
result = session.query(User).all()
for i in result:
    print(i.id, i.name)

session.close()
