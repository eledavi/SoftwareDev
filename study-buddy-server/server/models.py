from sqlalchemy import Column, Integer, Text, BigInteger, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):

    __tablename__ = "user"

    user_id = Column(Text, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    password = Column(Text)
    university = Column(Text)
    major = Column(Text)
    rating = Column(Float)
    courses = Column(Text, ForeignKey('course.course_id'))
    groups = Column(Text, ForeignKey('group.group_id'))
    is_leader_of = Column(Text, ForeignKey('group.group_id'))

    def toDict(self):
        return {
            "userId": self.user_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "university": self.university,
            "major": self.major,
            "rating": self.rating,
            "courses": self.courses,
            "groups": self.groups
        }


class Course(Base):

    __tablename__ = "course"

    course_id = Column(Text, primary_key=True)
    course_description = Column(Text)
    year = Column(Integer)
    semester = Column(Text)

    def toDict(self):
        return {
            "courseId": self.course_id,
            "courseDescription": self.course_description,
            "year": self.year,
            "semester": self.semester
        }


class Group(Base):

    __tablename__ = "group"

    group_id = Column(Text, primary_key=True)
    group_description = Column(Text)
    meet_time = Column(Text)
    meet_location = Column(Text)

    def toDict(self):
        return {
            'groupId': self.group_id,
            'groupDescription': self.group_description,
            'meetTime': self.meet_time,
            'meetLocation': self.meet_location
        }
