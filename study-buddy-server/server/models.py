from sqlalchemy import Column, Integer, Text, BigInteger, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

user_groups = Table(
    'user_groups', Base.metadata,
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('group_id', ForeignKey('group.id'), primary_key=True)
)

user_courses = Table(
    'user_courses', Base.metadata,
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('course_id', ForeignKey('course.id'), primary_key=True)
)


class User(Base):

    __tablename__ = "user"

    id = Column(Text, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    password = Column(Text)
    university = Column(Text)
    major = Column(Text)
    rating = Column(Float)
    email = Column(Text)
    groupsThatILead = relationship('Group', back_populates='myLeader')

    groups = relationship('Group', secondary=user_groups,  back_populates='myMembers')

    courses = relationship('Course', secondary=user_courses,  back_populates='myUsers')

    def toDict(self):
        return {
            "userId": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "university": self.university,
            "major": self.major,
            "rating": self.rating,
            "groupsThatILead": [p.id for p in self.groupsThatILead],
            "groups": [p.id for p in self.groups],
            "courses": [p.id for p in self.courses],
            "email": self.email,
            "password": self.password
        }


class Group(Base):

    __tablename__ = "group"

    id = Column(Text, primary_key=True)
    group_description = Column(Text)
    meet_time = Column(Text)
    meet_location = Column(Text)
    user_id = Column(Text, ForeignKey('user.id'))
    myLeader = relationship("User", back_populates="groupsThatILead")

    myMembers = relationship('User', secondary=user_groups, back_populates='groups')

    course_id = Column(Text, ForeignKey('course.id'))
    myCourse = relationship("Course", back_populates="groups")

    def toDict(self):
        return {
            'groupId': self.id,
            'groupDescription': self.group_description,
            'meetTime': self.meet_time,
            'meetLocation': self.meet_location,
            'groupLeader': self.myLeader.id,
            'members': [p.id for p in self.myMembers],
        }


class Course(Base):

    __tablename__ = "course"

    id = Column(Text, primary_key=True)
    course_description = Column(Text)
    year = Column(Integer)
    semester = Column(Text)
    groups = relationship('Group', back_populates='myCourse')

    myUsers = relationship('User', secondary=user_courses, back_populates='courses')

    def toDict(self):
        return {
            "courseId": self.id,
            "courseDescription": self.course_description,
            "year": self.year,
            "semester": self.semester,
            "groups": self.groups,
            "myUsers": [p.id for p in self.myUsers],
        }
