# services/api/app/ml/uploader.py
import os
from pathlib import Path
import subprocess
import tarfile

UPLOAD_ROOT = Path("mlruns/code_uploads")

def save_and_extract_tarball(upload_file, run_id: str) -> str:
    """
    Save the uploaded tarball and extract it under a folder named after the run_id.
    Supports .tar, .tar.gz, .tgz, and .tar.zst.
    """
    dest_dir = UPLOAD_ROOT / run_id
    dest_dir.mkdir(parents=True, exist_ok=True)

    tar_path = dest_dir / upload_file.filename

    # Save the uploaded tarball
    with open(tar_path, "wb") as f:
        f.write(upload_file.file.read())

    # Extract based on extension
    if tar_path.suffix == ".zst" or tar_path.suffixes[-2:] == [".tar", ".zst"]:
        # Extract .tar.zst
        subprocess.run(
            ["tar", "-I", "zstd", "-xf", str(tar_path), "-C", str(dest_dir)],
            check=True
        )
    elif tar_path.suffix in [".gz", ".tgz"] or tar_path.suffixes[-2:] == [".tar", ".gz"]:
        with tarfile.open(tar_path, "r:gz") as tar:
            tar.extractall(path=dest_dir)
    else:
        with tarfile.open(tar_path, "r:") as tar:
            tar.extractall(path=dest_dir)

    return str(dest_dir)
