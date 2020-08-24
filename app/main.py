from typing import List
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from . import crud, models, schemas
from fastapi.security import APIKeyCookie
# from .api import adultmedsp, famchildsp
from .database import SessionLocal, engine
from starlette.responses import Response
from .settings import settings
import os
import sys
import app.SAML_Interface as SAML_Interface
import uuid
import xmltodict
import json
from datetime import datetime

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

cookie_sec = APIKeyCookie(name="session")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# app.include_router(adultmedsp.router, tags=["Adult Medicad SP"])
# app.include_router(famchildsp.router, tags=["Family and Children SP"])

def saml_requests(req):
    pass

def get_current_user(session: str = Depends(cookie_sec)):
    pass


@app.post('/')
async def index(i: str = Depends(get_current_user)):
    return '{}'.format(i)

@app.get("/acs")
@app.post("/acs")
async def acs(request: Request, response: Response):
    try:
        form = await request.form()
        samlResponse = form["SAMLResponse"]
        #ACS URL listed here:
        strAcsUrl = 'http://localhost:6321/acs'
        userId = SAML_Interface.SAML_Response.ParseSAMLResponse(strAcsUrl,samlResponse)[1]
        
        if SAML_Interface.SAML_Response.ParseSAMLResponse(strAcsUrl,samlResponse)[0]:
            userId = SAML_Interface.SAML_Response.ParseSAMLResponse(strAcsUrl,samlResponse)[1]
            return userId
            # user_data = dict(
            #     userId = SAML_Interface.SAML_Response.ParseSAMLResponse(strAcsUrl,samlResponse)[1],
            #     year = datetime.now().year
            # )


        else:
            raise HTTPException(status_code=401, detail="Incorrect username or password")
    except KeyError:
        raise HTTPException(status_code=401, detail="Incorrect username or password")



@app.on_event("startup")
@app.get("/login")
@app.post("/login")
def login():
    

    strAcsUrl = 'http://localhost:6321/acs'
    #Issuer URL listed here:
    strIssuer = 'https://aad0380.my.idaptive.app/d726607b-09b3-4fe7-bfd7-68181aa71dce'
    #Sign In URL listed here:
    strSingleSignOnURL = 'https://aad0380.my.idaptive.app/applogin/appKey/d726607b-09b3-4fe7-bfd7-68181aa71dce/customerId/AAD0380'  
    return RedirectResponse('{uIDPUrl}?{bParams}'.format(uIDPUrl = strSingleSignOnURL, bParams = SAML_Interface.SAML_Request.GetSAMLRequest(strAcsUrl, strIssuer)))




@app.get('/api/v1/cases/2/', response_model=List[schemas.Adult_Medicaid_SP])
def read_all_adult_medicad(db: Session = Depends(get_db)):
    adultmedcases = crud.get_all_adult_medicad_cases(db)
    return adultmedcases

@app.get('/api/v1/cases/2/deleted', response_model=List[schemas.Adult_Medicaid_SP])
def read_all_deleted_adult_medicad(db: Session = Depends(get_db)):
    adultmedcases_deleted = crud.get_all_deleted_adult_medicad_cases(db)
    return adultmedcases_deleted

@app.get('/api/v1/cases/2/{id}', response_model=schemas.Adult_Medicaid_SP)
def read_all_adult_medicad(id: int, db: Session = Depends(get_db)):
    am_case = crud.get_adult_medicad_case(db, id=id)
    if am_case is None:
        raise HTTPException(status_code=404, detail="Case not found")
    return am_case




@app.put('/api/v1/cases/2/{id}/case', response_model=schemas.Adult_Medicaid_SP)
def update_Adult_Medicad(caseData: schemas.AdultMedicadCreate, id: int, db: Session = Depends(get_db)):
    am_case = crud.update_am_case(db, caseData=caseData, id=id)
    return am_case

@app.patch('/api/v1/cases/2/{id}/delete', response_model=schemas.Adult_Medicaid_SP)
def delete_Adult_Medicad(caseData: schemas.AdultMedicadDeleted, id: int, db: Session = Depends(get_db)):
    am_case = crud.delete_am_case(db, id=id)
    return am_case

@app.patch('/api/v1/cases/2/{id}/restore', response_model=schemas.Adult_Medicaid_SP)
def restore_Adult_Medicad(caseData: schemas.AdultMedicadDeleted, id: int, db: Session = Depends(get_db)):
    am_case = crud.restore_am_case(db, id=id)
    return am_case

@app.post("/api/v1/cases/2/", response_model=schemas.Adult_Medicaid_SP)
def create_adult_medicad_case(caseData: schemas.AdultMedicadCreate, db: Session = Depends(get_db)):
    am_new_case = crud.create_am_case(db=db, caseData=caseData)
    return am_new_case



@app.get('/api/v1/cases/1/', response_model=List[schemas.Family_Children_SP])
def read_all_family_chidren(db: Session = Depends(get_db)):
    famchildcases = crud.get_all_family_children_cases(db)
    return famchildcases

@app.get('/api/v1/cases/1/deleted', response_model=List[schemas.Family_Children_SP])
def read_all_deleted_family_chidren(db: Session = Depends(get_db)):
    famchildcases = crud.get_all_deleted_family_children_cases(db)
    return famchildcases


@app.get('/api/v1/cases/1/{id}', response_model=schemas.Family_Children_SP)
def read_all_family_chidren(id: int, db: Session = Depends(get_db)):
    fc_case = crud.get_family_children_case(db, id=id)

    if fc_case is None:
        raise HTTPException(status_code=404, detail="Case not found")
    return fc_case

@app.post("/api/v1/cases/1", response_model=schemas.Family_Children_SP)
def create_family_child_case(caseData: schemas.FamilyChildCreate, db: Session = Depends(get_db)):
    fc_case_new = crud.create_fc_case(db=db, caseData=caseData)
    return fc_case_new

@app.patch('/api/v1/cases/1/{id}/delete', response_model=schemas.Family_Children_SP)
def delete_family_child(caseData: schemas.FamilyChildDeleted, id: int, db: Session = Depends(get_db)):
    fc_case = crud.delete_fc_case(db, id=id)
    return fc_case

@app.patch('/api/v1/cases/1/{id}/restore', response_model=schemas.Family_Children_SP)
def restore_family_child(caseData: schemas.FamilyChildDeleted, id: int, db: Session = Depends(get_db)):
    fc_case = crud.restore_fc_case(db, id=id)
    return fc_case

@app.put('/api/v1/cases/1/{id}/case', response_model=schemas.Family_Children_SP)
def update_family_children(caseData: schemas.FamilyChildCreate, id: int, db: Session = Depends(get_db)):
    fc_case = crud.update_fc_case(db, caseData=caseData, id=id)
    return fc_case


