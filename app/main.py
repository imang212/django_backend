from fastapi import FastAPI

app = FastAPI()

@app.get("/api/tasks/")
def Vrat_seznam_ukolu():
    return {"message": "Hello, FastAPI in Docker!"}

@app.post("/api/tasks/")
def Vytvor_novy_ukol():
    ...

@app.get("/api/tasks/{id}/")
def Vrat_detaily_ukolu():
    ...

@app.put("/api/tasks/{id}/")
def Aktualizace_ukolu():
    ...

@app.delete("/api/tasks/{id}/")
def Smaz_ukol():
    ...

@app.get("/api/tasks/nearest-deadline/")
def Deadline():
    ...

#leetcode ukoly
@app.post("/api/leetcode/rotate-array/")
def Json_s_rotovanym_polem():
    ...

@app.post("/api/leetcode/kth-largest/")
def Json_s_k_tym_nejvetsim_prvkem():
    ...

@app.post("/api/leetcode/longest-increasing-path/")
def Matrix_s_nejdelsi_rostouci_cestou():
    ...