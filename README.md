# 🌍 AeroBRICS: Federated Cross-Border & Hyper-Local Air Quality Intelligence Platform

> **AI-Powered Federated Climate Action Platform for BRICS Nations**  
> Uniting citizen-sourced edge vision, hyper-local IoT sensors, Sentinel-5P/MODIS satellite remote sensing, and sovereign federated learning for trans-boundary air quality defense.

---

## 🎯 Hackathon Problem & Executive Summary

### The Problem
Major BRICS metropolitan regions (Delhi-NCR, Beijing-Tianjin-Hebei, São Paulo Metro, Highveld/Gauteng, Urals) monitor macro-level air quality through sparse official monitoring stations placed high atop government headquarters. These stations **consistently miss hyper-local, low-altitude emissions** (illegal brick kilns, suburban crop stubble burning, localized flaring, diesel freight clusters) and **cannot predict cross-border trans-boundary pollution plumes**. 

Furthermore, **national data sovereignty** prevents nations from uploading raw municipal sensor data, surveillance footage, or industrial monitoring feeds to foreign cloud providers, stalling collaborative climate action and resulting in $2.4 Trillion in annual healthcare and economic damages across 3.2 billion citizens.

### The AeroBRICS Solution
AeroBRICS introduces a **4-Layer Hybrid AI & Federated Governance Platform**:
1. **Citizen Edge AI & Handheld IoT**: Citizen smartphone photos analyzed via dark-channel prior and optical contrast analysis to compute smoke probability, haze index, and ground PM2.5 within seconds.
2. **Satellite Remote Sensing Fusion**: Real-time correlation with Sentinel-5P TROPOMI (NO2, CO, Aerosol Optical Depth) and MODIS/VIIRS thermal anomalies.
3. **Lagrangian-Gaussian Corridor Dispersion Forecaster**: 24-hour hour-by-hour cross-border inflow modeling driven by surface wind vectors to alert downstream authorities *before* smog plumes arrive.
4. **Sovereign Federated Learning (FedAvg + Differential Privacy)**: 5 sovereign edge nodes (India CPCB, China MEE, Brazil IBAMA, South Africa DFFE, Russia Roshydromet) collaboratively improve predictive dispersion models via secure weight exchange with calibrated Laplace/Gaussian differential privacy ($\epsilon=1.20$). **Zero raw telemetry leaves sovereign borders.**
5. **Rapid Intervention Center**: Automatically dispatches anti-smog mist cannon units, agricultural bio-decomposer crews, and factory output curtailment directives with quantifiable PM2.5 reduction targets.

---

## 🏗️ Architecture & Tech Stack

```
                   +------------------------------------------------+
                   |           AeroBRICS Web Command Center         |
                   |      React 18 + Vite + Tailwind + Leaflet      |
                   +------------------------------------------------+
                                          |
                     RESTful JSON APIs & Static SPA Serving
                                          |
                   +------------------------------------------------+
                   |                 FastAPI Backend                |
                   |               (Python 3.14 Async)              |
                   +------------------------------------------------+
                    /          |                     |            \
       +------------+   +------+------+       +------+-----+   +---+------------+
       | Vision AI  |   | Dispersion  |       | Federated  |   | SQLite3 DB     |
       | Engine     |   | Engine      |       | Aggregator |   | (aerobrics.db) |
       | (Optical   |   | (Gaussian / |       | (FedAvg +  |   | 7 Relational   |
       | Haze &     |   | Lagrangian  |       | SecAgg +   |   | Schemas)       |
       | Smoke)     |   | Plume)      |       | DiffPriv)  |   +----------------+
       +------------+   +-------------+       +------------+
```

| Layer | Technologies Used |
|---|---|
| **Backend** | Python 3.14, FastAPI, Uvicorn, Pydantic, NumPy, Pillow, python-multipart |
| **Database** | SQLite3 (`aerobrics.db`) with relational schemas & seeded BRICS economic corridors |
| **Frontend** | React 18, Vite 5, Tailwind CSS, Lucide Icons, Leaflet Dark Matter Mapping |
| **AI / ML** | Computer Vision (Dark-channel prior haze calculation), Lagrangian Plume Dispersion Engine, Federated Averaging (`FedAvg-SecAgg+DP`) |
| **Design** | Figma-inspired High-Tech Dark Cyber/Climate Defense Command Center |

---

## ⚡ Quick Start: Running the Prototype

### Prerequisites
- Python 3.10+ (Python 3.14 pre-tested)
- Node.js runtime (pre-configured in the project scratch environment)

### Launch in 1 Command
From the project directory:
```bash
# 1. Run the unified prototype launcher
py start_prototype.py
```

Open your browser to:
- **Unified Command Dashboard:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **FastAPI Interactive Swagger Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

*(Optional: If developing on the frontend with Vite Hot Reload, run `npm run dev` inside `frontend/` on port 5173).*

---

## 🌟 Interactive Features to Showcase in Hackathon Demo

### 1. 🗺️ Command Map Center
- Interactive dark-matter geographic map showing 5 BRICS economic corridors:
  - 🇮🇳 **Indo-Gangetic Plain Corridor** (Punjab/Haryana agricultural belt $\to$ Delhi-NCR)
  - 🇨🇳 **Jing-Jin-Ji Corridor** (Hebei/Tangshan steel belt $\to$ Beijing)
  - 🇧🇷 **Paraíba Valley Corridor** (Campinas/Paulínia petrochemicals $\to$ São Paulo)
  - 🇿🇦 **Highveld Coal Basin** (eMalahleni / Witbank power plants $\to$ Johannesburg)
  - 🇷🇺 **Urals Industrial Corridor** (Chelyabinsk smelters $\to$ Yekaterinburg)
- Toggle layers: Hyper-local micro-sensors, official macro stations, satellite thermal fire hotspots, citizen field reports, and wind dispersion vectors.

### 2. 📸 Citizen Science & Edge AI Photo Triage
- Click **"+ Report Ground Spike"** in the top navigation.
- Use one of the **Quick-Load Field Scenarios** (e.g. Punjab Stubble Fire, Tangshan Smelting, Brazil Refinery) or upload any custom photo.
- Real-time computer vision runs dark-channel prior analysis and contrast entropy extraction, outputting:
  - Optical Haze Index
  - Smoke / Plume Probability
  - Optical PM2.5 Estimation
  - Automated Source Attribution
- Persists instantly into the SQLite database and adds a live pin to the command map.

### 3. 💨 Trans-Boundary Corridor Forecasting & What-If Simulation
- Switch to **Corridor Sim** tab.
- Adjust the **Surface Wind Velocity** (5 km/h to 60 km/h) and **Wind Direction Azimuth** sliders.
- Inspect the interactive **24-Hour Predictive Dispersion Profile** chart:
  - Visualizes the ground-level PM2.5 spike arrival.
  - Decomposes the particulate concentration into trans-boundary inflow vs local background.
  - Displays source attribution breakdown (e.g., 54% Agricultural Stubble Burning, 21% Brick Kilns, 16% Vehicular).

### 4. 🧠 Federated Learning Sovereign Governance Hub
- Switch to **Federated Hub** tab.
- Displays 5 sovereign nodes operating within their home borders (India, China, Brazil, South Africa, Russia).
- Adjust the **Differential Privacy Noise** ($\epsilon$) slider.
- Click **"Execute Global FedAvg Round"**:
  - Simulates local node parameter training on newly submitted citizen data.
  - Aggregates weight vectors via Secure Aggregation.
  - Computes global loss and accuracy improvement without touching raw data.
  - Records the round into the immutable SQLite ledger.

### 5. 🚨 Rapid Climate Action & Emergency Intervention
- Switch to **Interventions** tab.
- View active actionable alerts generated by threshold breaches.
- Click **"Dispatch Intervention Units"** to order anti-smog mist cannon deployment or agricultural bio-decomposer teams.
- Click **"Mark Downwind Containment Verified"** to update deployment status.

### 6. 🏆 Hackathon Pitch & Architecture Deck
- Click **"Hackathon Pitch & Architecture"** in the top navigation bar at any time to open the built-in presentation deck designed specifically for judges.

---

## 📡 API Reference Summary

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/health` | System health check and sovereign node connectivity |
| `GET` | `/api/corridors` | List BRICS atmospheric corridors & meteorological baseline |
| `GET` | `/api/corridors/{id}/forecast` | 24-hour hour-by-hour dispersion forecast with what-if wind parameters |
| `GET` | `/api/sensors` | List macro government stations and hyper-local micro-sensors |
| `GET` | `/api/satellite` | Active Sentinel-5P AOD plumes and MODIS thermal fire anomalies |
| `POST` | `/api/reports` | Submit citizen report with photo and handheld sensor reading |
| `GET` | `/api/federated/nodes` | Status of sovereign edge nodes and privacy budgets |
| `POST` | `/api/federated/trigger-round` | Trigger global FedAvg round across BRICS nodes |
| `GET` | `/api/alerts` | Active emergency interventions and recommended actions |
| `POST` | `/api/alerts/action` | Dispatch or verify intervention mitigation units |

---

## 📜 License & Hackathon Acknowledgments
Built for the Global Climate & AI Hackathon. Designed for open interoperability across international environmental monitoring frameworks.
