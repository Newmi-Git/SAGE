# SAGE


#Description

WIP AI that helps to manage PC and do advanced functions on users PC
ROADMAP:

PHASE 0 — Foundation (v0.1)
 ├── Project scaffolding (FastAPI backend + Vue/Tauri shell, even if empty)
 ├── System monitor (CPU, RAM, disk, network via psutil)
 └── SQLite schema for logs/history (build this early, not later)

PHASE 1 — Observability (v0.2)
 ├── Process list (sortable, filterable)
 ├── Find biggest RAM/CPU users
 └── Basic action log (every "thing" the app does gets written down)

PHASE 2 — Manual Control, No AI Yet (v0.3)
 ├── Kill process / restart process (manual, via UI button)
 ├── Basic subprocess command execution
 └── First-pass permission model:
       - Read-only actions = no confirmation
       - Destructive actions (kill, delete, modify) = confirmation dialog
     (You want this UX pattern established before AI is the one requesting actions)

PHASE 3 — Tool Architecture (v0.4)
 ├── Define a Tool interface/schema (name, description, params, risk level)
 ├── Tool registry (so adding a tool = registering it, not editing a router)
 ├── Refactor v0.1–v0.3 features into this tool format
 └── This is the point where "Python tool → Windows → Result" becomes formalized

PHASE 4 — Local LLM Integration (v0.5)
 ├── Ollama integration, pick a function-calling-capable model
     (Qwen2.5, Llama 3.1/3.2, or Mistral — test tool-call reliability, don't assume)
 ├── Prompt → tool selection loop (no execution yet — just log what it WOULD call)
 └── Evaluate: does the model reliably pick the right tool with right params?
     (This is where you'll spend more time than expected — budget for it)

PHASE 5 — AI-Driven Execution (v0.6)
 ├── Connect LLM tool calls to actual execution
 ├── Risk-tiered confirmation (low-risk auto-runs, high-risk asks user)
 ├── Conversation/session memory (short-term context, not just single-shot prompts)
 └── Guardrails against prompt injection via tool outputs
     (e.g. if a process name or file content gets fed back to the LLM,
     it shouldn't be able to smuggle new instructions)

PHASE 6 — Desktop UI (v0.7)
 ├── Vue 3 + Tauri shell wired to FastAPI backend
 ├── Chat interface + system dashboard in one view
 ├── System tray integration (background-capable, not just foreground window)
 └── Real-time updates (WebSocket, not polling, for monitor + chat)

PHASE 7 — Safety & Permissions, Properly (v0.8)
 ├── Formal permission tiers per tool (read / modify / destructive / system-level)
 ├── Per-tool user-configurable auto-approve settings
 ├── Full audit log UI (searchable history of every action + who approved it)
 └── "Dry run" mode — AI explains what it would do before doing it

PHASE 8 — Polish & Ship (v1.0)
 ├── Error handling & graceful degradation (Ollama not running, tool fails, etc.)
 ├── Settings persistence (SQLite-backed config)
 ├── Installer + auto-update (Tauri has a built-in updater — use it)
 └── Windows code signing (unsigned .exe = instant SmartScreen red flag)

POST v1.0 — Advanced
 ├── PyTorch — custom fine-tuning or local embedding models
 ├── Multi-step planning (chains of tool calls, not just one-shot)
 ├── File system search / semantic search over user files
 └── Plugin system (let power users write their own tools)



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
