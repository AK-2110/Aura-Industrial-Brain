from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

app = FastAPI(title="Industrial Knowledge Intelligence API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Welcome to the Industrial Knowledge Brain API"}

@app.post("/api/upload")
async def upload_document(file: UploadFile = File(...)):
    # Simulate processing time
    time.sleep(2)
    
    # Mock extracted entities for demo purposes
    entities = [
        {"id": "pump-101", "type": "Equipment", "label": "Pump 101"},
        {"id": "valve-204", "type": "Component", "label": "Valve 204"},
        {"id": "manual-p101", "type": "Document", "label": "Pump 101 Manual"}
    ]
    
    relationships = [
        {"source": "pump-101", "target": "valve-204", "type": "CONNECTED_TO"},
        {"source": "pump-101", "target": "manual-p101", "type": "DOCUMENTED_IN"}
    ]
    
    return {
        "filename": file.filename,
        "status": "processed",
        "graph": {
            "nodes": entities,
            "edges": relationships
        }
    }

@app.get("/api/graph")
def get_knowledge_graph():
    # Return a larger mock graph for the UI
    nodes = [
        {"id": "pump-101", "group": "Equipment", "label": "Pump-101"},
        {"id": "valve-204", "group": "Component", "label": "Valve-204"},
        {"id": "motor-55", "group": "Component", "label": "Motor-55"},
        {"id": "doc-manual", "group": "Document", "label": "OEM Manual"},
        {"id": "wo-992", "group": "WorkOrder", "label": "WO-992: Seal Leak"},
        {"id": "tech-john", "group": "Personnel", "label": "John Doe"}
    ]
    
    links = [
        {"source": "pump-101", "target": "valve-204", "label": "HAS_COMPONENT"},
        {"source": "pump-101", "target": "motor-55", "label": "HAS_COMPONENT"},
        {"source": "pump-101", "target": "doc-manual", "label": "DESCRIBED_BY"},
        {"source": "wo-992", "target": "pump-101", "label": "MAINTAINS"},
        {"source": "tech-john", "target": "wo-992", "label": "ASSIGNED_TO"}
    ]
    
    return {"nodes": nodes, "links": links}

@app.post("/api/chat")
def chat_copilot(req: ChatRequest):
    time.sleep(1)
    
    # Simple keyword-based mock routing
    msg = req.message.lower()
    
    if "pump-101" in msg and "pressure" in msg:
        response = "According to the **OEM Manual** (Page 42), the standard operating pressure for **Pump-101** is 120 PSI. However, note that **WO-992** indicates a recent seal leak, so monitor for pressure drops."
        citations = ["OEM Manual", "WO-992"]
    elif "fail" in msg or "rca" in msg:
        response = "Based on historical data, **Pump-101** failure modes are strongly correlated with high vibration in **Motor-55**. I recommend inspecting the motor bearings."
        citations = ["Maintenance History", "Motor-55 Spec"]
    else:
        response = "I can help you with equipment specs, maintenance history, or operating procedures. Try asking about 'Pump-101 pressure'."
        citations = []
        
    return {
        "reply": response,
        "citations": citations
    }
