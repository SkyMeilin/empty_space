import os
import torch
from huggingface_hub import hf_hub_download

# 1. Access Token aus den HF Secrets / Umgebungsvariablen auslesen
HF_TOKEN = os.getenv("HF_TOKEN")

def load_skyos_model(repo_id: str = "sky-meilin/skyos-model-weights", filename: str = "model.pth"):
    print(f"Lade Modell-Gewichte von '{repo_id}' ({filename})...")
    
    # 2. Checkpoint aus dem Hugging Face Hub herunterladen
    try:
        checkpoint_path = hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            token=HF_TOKEN  # Erforderlich für private Repos
        )
        print(f"Pfad zur lokal gecachten Datei: {checkpoint_path}")
    except Exception as e:
        print(f"Fehler beim Herunterladen der Gewichte: {e}")
        return None

    # 3. Das PyTorch-Modell instanziieren (hier deine Modell-Klasse einfügen)
    # model = SimpleLLM()  # Ersetze dies durch deine eigentliche Modell-Architektur
    
    # 4. Gewichte sicher in das Modell laden
    # Device festlegen (CPU oder GPU, falls verfügbar)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # Checkpoint laden (weights_only=True schützt vor schädlichem Code beim Unpickling)
    state_dict = torch.load(checkpoint_path, map_location=device, weights_only=True)
    
    # model.load_state_dict(state_dict)
    # model.to(device)
    # model.eval()
    
    print("Modell-Gewichte erfolgreich geladen!")
    return state_dict

# Ausführen
if __name__ == "__main__":
    weights = load_skyos_model()
