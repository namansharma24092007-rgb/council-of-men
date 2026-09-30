"""
AeroBRICS: Single Command Prototype Runner
Launches FastAPI backend (and serves unified React frontend)
"""
import subprocess
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(PROJECT_ROOT, "backend")
FRONTEND_DIR = os.path.join(PROJECT_ROOT, "frontend")
NODE_DIR = os.path.join(os.path.dirname(PROJECT_ROOT), "node")

def run():
    print("=" * 70)
    print("  [AeroBRICS] Federated Cross-Border & Hyper-Local Climate Action  ")
    print("=" * 70)
    print(f"Project Directory: {PROJECT_ROOT}")
    print(f"Backend Directory: {BACKEND_DIR}")
    print(f"Frontend Directory: {FRONTEND_DIR}\n")

    # Start FastAPI Backend via uvicorn
    print(">> Initializing SQLite database and launching FastAPI backend on http://127.0.0.1:8000...")
    backend_cmd = [sys.executable, "-m", "uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"]
    
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    if os.path.exists(NODE_DIR):
        env["PATH"] = f"{NODE_DIR};{env.get('PATH', '')}"

    backend_proc = subprocess.Popen(
        backend_cmd,
        cwd=BACKEND_DIR,
        env=env
    )

    print("\n" + "=" * 70)
    print("  >>> AeroBRICS Prototype is ACTIVE! <<<")
    print("  * Unified Web Dashboard:  http://127.0.0.1:8000")
    print("  * Interactive API Docs:   http://127.0.0.1:8000/docs")
    print("=" * 70)
    print("Press Ctrl+C to terminate.")

    try:
        backend_proc.wait()
    except KeyboardInterrupt:
        print("\nShutting down AeroBRICS prototype...")
        backend_proc.terminate()

if __name__ == "__main__":
    run()
