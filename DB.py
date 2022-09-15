from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import registry, Session

# 데이터베이스 연결 
engine = create_engine(
    "mysql+pymysql://root:chocolate52@localhost:3306/board_study?charset=utf8mb4",
    echo=True,
    future=True,
)
Base = declarative_base()

# 테이블 생성
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    menu = Column(String(255))

    def __init__(self, menu):
        self.menu = menu

    def __repr__(self):
        return "<User('%s')>" % (self.menu)

Base.metadata.create_all(engine)

# 데이터 추가해보기
# session = Session(engine)
# # session.add(User(menu="김치"))
# # session.commit()

# 데이터 조회해보기
# for instance in session.query(User).order_by(User.id):
#     print(instance.menu)

#------repository---------------------------

class Repo(object):
    def __init__(self):
        self.engine = create_engine(
            "mysql+pymysql://root:chocolate52@localhost:3306/board_study?charset=utf8mb4",
            echo=True,
            future=True,
        )

        self.mapper_registry = registry()
        self.Base = self.mapper_registry.generate_base()
        self.session = Session(self.engine)


    #데이터 추가
    def add_crawling_data(self, menu: str):
        self.session.add(User(menu=menu))
        self.session.commit()


    #데이터 조회
    def get_crawling_data(self, menu: str):
        query = self.session.query(User)
        for instance in self.session.query(User).order_by(User.id):
            print(instance.menu)