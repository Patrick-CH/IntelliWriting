from database import engine
from models import users, User, passages, Passage
from sqlalchemy.orm import Session

con = engine.connect()
# con.execute('''CREATE TABLE IF NOT EXISTS `users`(
#    `id` INT UNSIGNED AUTO_INCREMENT,
#    `name` VARCHAR(50) NOT NULL UNIQUE,
#    `email` VARCHAR(100) NOT NULL,
#    `passwd` VARCHAR(100) NOT NULL,
#    PRIMARY KEY ( `id` )
# )ENGINE=InnoDB DEFAULT CHARSET=utf8;''')
# con.execute(users.insert(), {"name":"cyk", "email": "cyk@qq.com", "passwd":"cykcykcyk"})

from sqlalchemy import select

# session = Session(engine)

# stmt = select(User).where(User.name == "cyk1")

# cyk = session.scalars(stmt).one()
# print(cyk)
# print(cyk.passwd)

# with Session(engine) as session:
#     # patrick = User(name="patrick", email="patrick@qq.com", passwd="patrickpatrickpatrick")
#     # session.add_all([patrick])
#     # session.commit()
#     stmt = select(User)
#     for user in session.scalars(stmt):
#         print(user)

# con.execute("DROP TABLE passages")

# con.execute('''CREATE TABLE IF NOT EXISTS `passages`(
#    `id` INT UNSIGNED AUTO_INCREMENT,
#    `title` VARCHAR(100) NOT NULL,
#    `abstract` VARCHAR(500) NOT NULL,
#    `content` VARCHAR(5000) NOT NULL,
#    `username` VARCHAR(50) NOT NULL,
#    PRIMARY KEY ( `id` )
# )ENGINE=InnoDB DEFAULT CHARSET=utf8;''')

con.execute("DELETE FROM passages WHERE title='test'")

# with Session(engine) as session:
#     # p = Passage(tile="test", abstract="test_abs", content="Today is a rainy day.", username="cyk")
#     # session.add_all([p])
#     # session.commit()

#     stmt = select(Passage)
#     for p in session.scalars(stmt):
#         print(p.img)
