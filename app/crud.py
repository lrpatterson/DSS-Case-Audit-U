from sqlalchemy.orm import Session
from . import models, schemas

def get_all_adult_medicad_cases(db: Session):
    return db.query(models.Adult_Medicaid_SP).filter(models.Adult_Medicaid_SP.DELETED != 1).all()

def get_all_deleted_adult_medicad_cases(db: Session):
    return db.query(models.Adult_Medicaid_SP).filter(models.Adult_Medicaid_SP.DELETED != 0).all()

def get_adult_medicad_case(db: Session, id: int):
    return db.query(models.Adult_Medicaid_SP).filter(models.Adult_Medicaid_SP.ID == id).first()



def create_am_case(db: Session, caseData: schemas.AdultMedicadCreate):
    data = models.Adult_Medicaid_SP(
            CASE_WORKERS_NAME = caseData.CASE_WORKERS_NAME,
            SUPERVISOR_LEADWORKER = caseData.SUPERVISOR_LEADWORKER,
            DATE_OF_REVIEW = caseData.DATE_OF_REVIEW,
            AID_PROGRAM_CATEGORY = caseData.AID_PROGRAM_CATEGORY,
            CLIENT_NAME = caseData.CLIENT_NAME,
            ISA_ISC = caseData.ISA_ISC,
            CASE_TYPE = caseData.CASE_TYPE,
            CASE_ISSUE_STATUS = caseData.CASE_ISSUE_STATUS,
            DELETED = 0,

    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data



def update_am_case(db: Session, id: id, caseData: schemas.AdultMedicadCreate):
    update_payload = db.query(models.Adult_Medicaid_SP).filter(models.Adult_Medicaid_SP.ID == id).first()
    update_payload.CASE_WORKERS_NAME = caseData.CASE_WORKERS_NAME
    update_payload.SUPERVISOR_LEADWORKER = caseData.SUPERVISOR_LEADWORKER
    update_payload.DATE_OF_REVIEW = caseData.DATE_OF_REVIEW
    update_payload.AID_PROGRAM_CATEGORY = caseData.AID_PROGRAM_CATEGORY
    update_payload.CLIENT_NAME = caseData.CLIENT_NAME
    update_payload.ISA_ISC = caseData.ISA_ISC
    update_payload.CASE_TYPE = caseData.CASE_TYPE
    update_payload.CASE_ISSUE_STATUS = caseData.CASE_ISSUE_STATUS



    db.add(update_payload)
    db.commit()
    db.refresh(update_payload)
    return update_payload

def delete_am_case(db: Session, id: id):
    update_payload = db.query(models.Adult_Medicaid_SP).filter(models.Adult_Medicaid_SP.ID == id).first()
    update_payload.DELETED = 1
    db.add(update_payload)
    db.commit()
    db.refresh(update_payload)
    return update_payload

def restore_am_case(db: Session, id: id):
    update_payload = db.query(models.Adult_Medicaid_SP).filter(models.Adult_Medicaid_SP.ID == id).first()
    update_payload.DELETED = 0
    db.add(update_payload)
    db.commit()
    db.refresh(update_payload)
    return update_payload




def create_fc_case(db: Session, caseData: schemas.FamilyChildCreate):
    data = models.Family_Children_SP(
        CASE_NAME = caseData.CASE_NAME,
        CASE_WORKER = caseData.CASE_WORKER,
        DATE_OF_REVIEW = caseData.DATE_OF_REVIEW,
        COUNTY_CASE_NUMBER = caseData.COUNTY_CASE_NUMBER,
        QUALITY_REVIEW_ACTION = caseData.QUALITY_REVIEW_ACTION,
        SUPERVISOR_OR_LEADWORKER = caseData.SUPERVISOR_OR_LEADWORKER,
        PROGRAM = caseData.PROGRAM,
        CASE_ISSUE_STATUS = caseData.CASE_ISSUE_STATUS,
        DELETED = 0,

    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def update_fc_case(db: Session, id: id, caseData: schemas.FamilyChildCreate):
    update_payload = db.query(models.Family_Children_SP).filter(models.Family_Children_SP.ID == id).first()
    update_payload.CASE_NAME = caseData.CASE_NAME
    update_payload.CASE_WORKER = caseData.CASE_WORKER
    update_payload.DATE_OF_REVIEW = caseData.DATE_OF_REVIEW
    update_payload.COUNTY_CASE_NUMBER = caseData.COUNTY_CASE_NUMBER
    update_payload.QUALITY_REVIEW_ACTION = caseData.QUALITY_REVIEW_ACTION
    update_payload.SUPERVISOR_OR_LEADWORKER = caseData.SUPERVISOR_OR_LEADWORKER
    update_payload.PROGRAM = caseData.PROGRAM
    update_payload.CASE_ISSUE_STATUS = caseData.CASE_ISSUE_STATUS


    db.add(update_payload)
    db.commit()
    db.refresh(update_payload)
    return update_payload


def delete_fc_case(db: Session, id: id):
    update_payload = db.query(models.Family_Children_SP).filter(models.Family_Children_SP.ID == id).first()
    update_payload.DELETED = 1
    db.add(update_payload)
    db.commit()
    db.refresh(update_payload)
    return update_payload

def restore_fc_case(db: Session, id: id):
    update_payload = db.query(models.Family_Children_SP).filter(models.Family_Children_SP.ID == id).first()
    update_payload.DELETED = 1
    db.add(update_payload)
    db.commit()
    db.refresh(update_payload)
    return update_payload



def get_all_family_children_cases(db: Session):
    return db.query(models.Family_Children_SP).filter(models.Family_Children_SP.DELETED != 1).all()

def get_all_deleted_family_children_cases(db: Session):
    return db.query(models.Family_Children_SP).filter(models.Family_Children_SP.DELETED != 0).all()


def get_family_children_case(db: Session, id: int):
    return db.query(models.Family_Children_SP).filter(models.Family_Children_SP.ID == id).first()