#!/usr/bin/env python3
"""
SkyOS / JoyAI Benchmark Suite
Führt automatisierte Evaluierungs-Durchläufe gegen die Inferenz-Engine durch
und persistiert die Ergebnisse im Test-Log-Speicher.
"""
import os
import sys
import json
import time
from datetime import datetime
from pathlib import Path

# Persistent Storage & Test-Logs
DATA_DIR = Path("/data")
LOGS_DIR = DATA_DIR / "test_logs" if DATA_DIR.exists() else Path("./test_logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "Qwen/Qwen2.5-Coder-7B-Instruct"

# Standardisierte Benchmark-Testfälle
BENCHMARK_SUITE = [
    {
        "id": "TC_01_SYNTAX_PARSING",
        "category": "Code Analysis",
        "system_prompt": "Du bist ein technischer Code-Auditor. Antworte präzise und strukturiert.",
        "prompt": "Analysiere folgenden Python-Code und nenne Zweck sowie potenzielle Schwachstellen:\n\n```python\ndef get_db_conn(user, pwd, host='localhost'):\n    import sqlite3\n    return sqlite3.connect('app.db')\n```",
        "max_tokens": 512,
        "temperature": 0.2
    },
    {
        "id": "TC_02_MCP_INTERFACE",
        "category": "Protocol Integration",
        "system_prompt": "Du bist ein KI-Architekt für FastMCP und verteilte Systeme.",
        "prompt": "Beschreibe kurz das Zusammenspiel zwischen einem FastMCP Server-Decorator `@mcp.tool()` und einem Gradio ChatInterface.",
        "max_tokens": 512,
        "temperature": 0.3
    },
    {
        "id": "TC_03_REFACTORING",
        "category": "Refactoring & Clean Code",
        "system_prompt": "Du bist ein Senior Python Entwickler.",
        "prompt": "Schreibe diese Funktion als List-Comprehension um:\n\n```python\nres = []\nfor x in range(20):\n    if x % 2 == 0:\n        res.append(x * 2)\n```",
        "max_tokens": 256,
        "temperature": 0.1
    }
]

def load_engine():
    """Initialisiert Tokenizer und Modell."""
    print(f"[INIT] Lade Tokenizer & Modell: {MODEL_ID} ...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    
    # Device-Erkennung: CUDA falls verfügbar, sonst CPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[INIT] Inferenz-Gerät: {device.upper()}")
    
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        dtype=torch.bfloat16 if device == "cuda" else torch.float32,
        low_cpu_mem_usage=True,
        device_map=device
    )
    return tokenizer, model, device

def run_single_test(tokenizer, model, device, test_case: dict) -> dict:
    """Führt einen einzelnen Testfall aus und misst Latenz und Token-Output."""
    messages = [
        {"role": "system", "content": test_case["system_prompt"]},
        {"role": "user", "content": test_case["prompt"]}
    ]
    
    model_inputs = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt",
        return_dict=True
    )
    
    input_ids = model_inputs["input_ids"].to(device)
    attention_mask = model_inputs.get("attention_mask", None)
    if attention_mask is not None:
        attention_mask = attention_mask.to(device)
        
    start_time = time.perf_counter()
    
    with torch.no_grad():
        output_tokens = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=test_case["max_tokens"],
            do_sample=test_case["temperature"] > 0,
            temperature=test_case["temperature"] if test_case["temperature"] > 0 else None,
            pad_token_id=tokenizer.eos_token_id
        )
        
    elapsed_seconds = round(time.perf_counter() - start_time, 3)
    
    # Generierte Tokens isolieren (Prompt abschneiden)
    input_len = input_ids.shape[-1]
    generated_ids = output_tokens[0][input_len:]
    response_text = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
    
    tokens_generated = len(generated_ids)
    tokens_per_sec = round(tokens_generated / elapsed_seconds, 2) if elapsed_seconds > 0 else 0.0

    return {
        "test_id": test_case["id"],
        "category": test_case["category"],
        "elapsed_seconds": elapsed_seconds,
        "tokens_generated": tokens_generated,
        "tokens_per_second": tokens_per_sec,
        "prompt": test_case["prompt"],
        "response": response_text
    }

def execute_suite():
    """Startet die gesamte Benchmark-Suite und erzeugt einen Gesamt-Report."""
    print("=" * 60)
    print("🚀 Starte JoyAI / SkyOS Inferenz-Benchmark")
    print("=" * 60)
    
    tokenizer, model, device = load_engine()
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = LOGS_DIR / f"benchmark_report_{timestamp_str}.json"
    
    results = []
    for idx, test_case in enumerate(BENCHMARK_SUITE, start=1):
        print(f"\n[{idx}/{len(BENCHMARK_SUITE)}] Führe aus: {test_case['id']} ({test_case['category']}) ...")
        res = run_single_test(tokenizer, model, device, test_case)
        results.append(res)
        print(f"       -> Dauer: {res['elapsed_seconds']}s | Tokens/s: {res['tokens_per_second']}")
    
    report_data = {
        "benchmark_id": f"BENCH_{timestamp_str}",
        "timestamp": datetime.now().isoformat(),
        "model_id": MODEL_ID,
        "device": device,
        "total_tests": len(results),
        "results": results
    }
    
    with open(report_filename, "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
        
    print("\n" + "=" * 60)
    print(f"✅ Benchmark erfolgreich abgeschlossen!")
    print(f"📄 Report gespeichert unter: {report_filename}")
    print("=" * 60)

if __name__ == "__main__":
    execute_suite()
