from typing import List, Optional, Dict
from pydantic import BaseModel
from datetime import date


class AdultMedicadBase(BaseModel):
    CASE_WORKERS_NAME: str
    SUPERVISOR_LEADWORKER: str
    DATE_OF_REVIEW: date
    AID_PROGRAM_CATEGORY: str
    CLIENT_NAME: str
    ISA_ISC: str
    CASE_TYPE: str
    CASE_ISSUE_STATUS: str


class AdultMedicadCreate(AdultMedicadBase):
    CASE_WORKERS_NAME: str
    SUPERVISOR_LEADWORKER: str
    DATE_OF_REVIEW: date
    AID_PROGRAM_CATEGORY: str
    CLIENT_NAME: str
    ISA_ISC: str
    CASE_TYPE: str
    CASE_ISSUE_STATUS: str

class AdultMedicadDeleted(BaseModel):
    DELETED: int



class Adult_Medicaid_SP(AdultMedicadBase):
    ID: int
    DELETED: int

    class Config:
        orm_mode = True



class FamilyChildBase(BaseModel):
    CASE_NAME: str
    CASE_WORKER: str
    DATE_OF_REVIEW: date
    COUNTY_CASE_NUMBER: str
    QUALITY_REVIEW_ACTION: str
    SUPERVISOR_OR_LEADWORKER: str
    PROGRAM: str
    CASE_ISSUE_STATUS: str


class FamilyChildCreate(FamilyChildBase):
    CASE_NAME: str
    CASE_WORKER: str
    DATE_OF_REVIEW: date
    COUNTY_CASE_NUMBER: str
    QUALITY_REVIEW_ACTION: str
    SUPERVISOR_OR_LEADWORKER: str
    PROGRAM: str
    CASE_ISSUE_STATUS: str

class FamilyChildDeleted(BaseModel):
    DELETED: int


class Family_Children_SP(FamilyChildBase):
    ID: int
    DELETED: int

    class Config:
        orm_mode = True



class QuestionQRBase(BaseModel):
    QR_QUESTION: str
    ASSOCIATED_FORM: int

class QuestionQRCreate(QuestionQRBase):
    pass

class Questions_QR(QuestionQRBase):
    ID: int
    DELETED: int

    class Config:
        orm_mode = True



class FormQRBase(BaseModel):
    FORM_COMMON_NAME: str

class FormQRCreate(FormQRBase):
    pass

class Forms_QR(FormQRBase):
    ID: int
    DELETED: int

    class Config:
        orm_mode = True



class CommentsQRBase(BaseModel):
    COMMENT: str

class CommentsQRCreate(CommentsQRBase):
    pass

class Comments_QR(CommentsQRBase):
    ID: int
    DELETED: int
    CASE_ID: int
    

    class Config:
        orm_mode = True



class AnswersQRBase(BaseModel):
    ANSWERS: int
    QUEST: int

class AnswersQRCreate(AnswersQRBase):
    pass

class Answers_QR(AnswersQRBase):
    ID: int
    DELETED: int
    MASTER_ID: int
    MASTER_REC_ID: int

    class Config:
        orm_mode = True