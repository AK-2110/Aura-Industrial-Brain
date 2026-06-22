# Aura | Industrial Brain

A unified asset and operations intelligence platform built for asset-intensive industries. Aura serves as an "Industrial Knowledge Copilot," ingesting fragmented engineering schematics (P&IDs), OEM manuals, and maintenance work orders to create a live, interactive 3D Knowledge Graph and a conversational RAG AI.

## Features

- **Universal Document Ingestion:** Drag-and-drop file processing simulating Gemini 3.1 Pro entity extraction.
- **3D Knowledge Graph:** Interactive, dynamic 3D physics engine visualization of the plant ontology (Equipment, Documents, Sensors, Alerts).
- **Expert Copilot:** Multimodal RAG conversational interface that explains uploaded P&ID schematics, diagnoses anomalies, and generates automated Root Cause Analyses.
- **Premium Industrial UI:** Glassmorphism, animated transitions, and an immersive dark-mode aesthetic.

## Tech Stack

- **Frontend:** Next.js 15, React 19, Tailwind CSS v4, Framer Motion, react-force-graph-3d, Three.js, Lucide React
- **Backend:** Python, FastAPI, Uvicorn

## How to Run the Project Locally

This project uses a decoupled architecture. You will need to run the frontend and backend servers separately.

### 1. Start the Backend Server (FastAPI)

1. Open a terminal and navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
3. Install the dependencies (if not already installed):
   ```bash
   pip install fastapi uvicorn pydantic
   ```
4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
   The backend will be running at `http://localhost:8000`.

### 2. Start the Frontend Server (Next.js)

1. Open a new terminal and navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install the Node.js dependencies:
   ```bash
   npm install
   ```
3. Start the Next.js development server:
   ```bash
   npm run dev
   ```
   The frontend will be running at `http://localhost:3000`.

### 3. Using the App

- Open `http://localhost:3000` in your browser.
- Use the **Ingestion** tab to upload the sample files located in the `/sample_data` directory.
- Switch to the **3D Knowledge Graph** to interact with the parsed ontology.
- Open the **Expert Copilot** to chat with Aura. Try uploading the `Pump101_PID_Schematic.png` and asking it to explain the drawing!

---
*Built with Next.js and FastAPI.*
