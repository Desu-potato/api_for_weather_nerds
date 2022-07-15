from cgitb import text
from h11 import Data
from pydantic import EmailStr
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from ..database import Base


class Weather(Base):
    __tablename__ = "weather"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    createdAt = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    deleatedAt = Column(TIMESTAMP(timezone=True), nullable=True)
    location_town = Column(String, nullable=False)
    location_country = Column(String, nullable=False)
    weather = Column(String, nullable=False)

class Role(Base):
    __tablename__ = "role"

    id = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    createdAt = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    deleatedAt = Column(TIMESTAMP(timezone=True), nullable=True)
    roletype = Column(String, primary_key=True, nullable=False)
    rolevalue = Column(Integer, nullable=False)



# associationTableUserRole = Table(
#     "user_role",
#     Base.metadata,
#     Column("weather", ForeignKey("role.id")),
#     Column("userId", ForeignKey("user.id")),
# )

# associationTableWeatherUser = Table(
#     "weather_user",
#     Base.metadata,
#     Column("weatherRecordId", ForeignKey("weather.id")),
#     Column("userId", ForeignKey("user.id")),
# )

class User(Base):
    __tablename__  = "user"
    id = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    createdAt = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    deleatedAt = Column(TIMESTAMP(timezone=True), nullable=True)
    email = Column(String, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    # userrole = relationship("user_role", secondary=associationTableUserRole)
    # weatherrole = relationship("weather_user", secondary=associationTableWeatherUser)


