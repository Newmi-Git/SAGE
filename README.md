# SAGE


#Description

WIP AI that helps to manage PC and do advanced functions on users PC
ROADMAP:

CORE v0.1
 └── System monitor

CORE v0.2
 ├── System monitor
 └── Process list

CORE v0.3
 ├── System monitor
 ├── Process list
 └── Find biggest RAM users

CORE v0.4
 ├── System monitor
 ├── Process list
 ├── RAM analysis
 └── Basic commands

CORE v0.5
 ├── Everything above
 └── Local LLM

CORE v1.0
 ├── AI
 ├── PC monitoring
 ├── Tool/function calling
 ├── Desktop UI
 └── Safety/permissions



AI architecture:

User
 ↓
CORE AI
 ↓
"Which tool should I use?"
 ↓
Python tool
 ↓
Windows
 ↓
Result
 ↓
CORE AI
 ↓
User


Tech Stack:

##AI
Python
PyTorch — eventually
Ollama — easy way to run the local LLM on the user's PC

##Backend / PC control
Python
FastAPI — backend/API
psutil — CPU, RAM, disk, processes, network
subprocess — execute system commands
Windows APIs / pywin32 — deeper Windows control
SQLite — local settings, history, logs

##Frontend / Desktop app
Vue 3 — UI
Tauri — packages Vue into a proper desktop application
