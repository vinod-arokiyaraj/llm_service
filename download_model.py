from huggingface_hub import snapshot_download

MODEL_NAME = "facebook/bart-large-cnn"
MODEL_PATH = "./model/facebook/bart-large-cnn"

def download_model():
    print(f"Downloading '{MODEL_NAME}' to '{MODEL_PATH}' ...")
    snapshot_download(repo_id=MODEL_NAME, local_dir=MODEL_PATH, local_dir_use_symlinks=False)
    print(f"Model downloaded successfully at {MODEL_PATH} ✅")

if __name__ == "__main__":
    download_model()
