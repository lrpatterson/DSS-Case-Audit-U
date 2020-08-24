from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base

class Adult_Medicaid_SP(Base):
    __tablename__ = 'DSSCASEAUDITOR_ADULT_MEDICAID_SECOND_PARTY'

    ID = Column(Integer, primary_key=True, index=True)
    DELETED = Column(Boolean)
    CASE_WORKERS_NAME = Column(String)
    SUPERVISOR_LEADWORKER = Column(String)
    DATE_OF_REVIEW = Column(DateTime, default=datetime.today().strftime('%Y-%m-%d'))
    AID_PROGRAM_CATEGORY = Column(String)
    CLIENT_NAME = Column(String)
    ISA_ISC = Column(String)
    CASE_TYPE = Column(String)
    CASE_ISSUE_STATUS = Column(String)
    FORM_TYPE = Column(Integer, index=True, default=2)

class Family_Children_SP(Base):
    __tablename__ = 'DSSCASEAUDITOR_FAMILY_AND_CHILDREN'
    
    ID = Column(Integer, primary_key=True, index=True)
    DELETED = Column(Boolean, default=False)
    CASE_NAME = Column(String)
    CASE_WORKER = Column(String)
    DATE_OF_REVIEW = Column(DateTime, default=datetime.today().strftime('%Y-%m-%d'))
    COUNTY_CASE_NUMBER = Column(String)
    QUALITY_REVIEW_ACTION = Column(String)
    SUPERVISOR_OR_LEADWORKER = Column(String)
    PROGRAM = Column(String)
    CASE_ISSUE_STATUS = Column(String)
    FORM_TYPE = Column(Integer, index=True, default=1)

class Questions_QR(Base):
    __tablename__ = 'DSSCASEAUDITOR_DSSCASE_QR_QUESTIONS'

    ID = Column(Integer, primary_key=True, index=True)
    DELETED = Column(Boolean)
    QR_QUESTION = Column(String)
    ASSOCIATED_FORM = Column(Integer)

class Forms_QR(Base):
    __tablename__ = 'DSSCASEAUDITOR_DSSCASE_QR_FORMS'

    ID = Column(Integer, primary_key=True, index=True)
    DELETED = Column(Boolean)
    FORM_COMMON_NAME = Column(String)

class Comments_QR(Base):
    __tablename__ = 'DSSCASEAUDITOR_DSSCASE_QR_COMMENTS'

    ID = Column(Integer, primary_key=True, index=True)
    DELETED = Column(Boolean)
    COMMENT = Column(String)
    CASE_ID = Column(Integer)

class Answers_QR(Base):
    __tablename__ = 'DSSCASEAUDITOR_DSSCASE_QR_ANSWERS'

    ID = Column(Integer, primary_key=True, index=True)
    DELETED = Column(Boolean, default=False)
    MASTER_ID = Column(Integer)
    MASTER_REC_ID = Column(Integer)
    ANSWERS = Column(Integer)
    QUEST = Column(Integer)