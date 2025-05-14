from fastapi import FastAPI, Depends, HTTPException
from app.routes import (
    com_router,
    prod_router,
    # Processamento 
    processamento_viniferas,
    processamento_americanas,
    processamento_uvas_de_mesa,  
    processamento_sem_classificacao,
    # Exportação 
    export_espumantes_router,
    export_suco_de_uva_router,
    export_uvas_frescas_router,
    export_vinhos_de_mesa_router,
    # Importação 
    import_espumantes_router,
    import_suco_router,
    import_uvas_router,
    import_passadas_router,
    import_vinhos_router
)

app = FastAPI(title="API Embrapa", version="2.0")

# Rotas básicas
app.include_router(com_router)
app.include_router(prod_router)

# Processamento 
app.include_router(processamento_viniferas, prefix="/processamento", tags=["Processamento"])
app.include_router(processamento_americanas, prefix="/processamento", tags=["Processamento"])
app.include_router(processamento_uvas_de_mesa, prefix="/processamento", tags=["Processamento"])  
app.include_router(processamento_sem_classificacao, prefix="/processamento", tags=["Processamento"])

# Exportação 
app.include_router(export_espumantes_router, prefix="/exportacao", tags=["Exportação"])
app.include_router(export_suco_de_uva_router, prefix="/exportacao", tags=["Exportação"])
app.include_router(export_uvas_frescas_router, prefix="/exportacao", tags=["Exportação"])
app.include_router(export_vinhos_de_mesa_router, prefix="/exportacao", tags=["Exportação"])

# Importação 
app.include_router(import_espumantes_router, prefix="/importacao", tags=["Importação"])
app.include_router(import_suco_router, prefix="/importacao", tags=["Importação"])
app.include_router(import_uvas_router, prefix="/importacao", tags=["Importação"])
app.include_router(import_passadas_router, prefix="/importacao", tags=["Importação"])
app.include_router(import_vinhos_router, prefix="/importacao", tags=["Importação"])


from fastapi.security import OAuth2PasswordRequestForm
from app.services.auth import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, Token, get_current_user

@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not authenticate_user(form_data.username, form_data.password):
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")
    
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}