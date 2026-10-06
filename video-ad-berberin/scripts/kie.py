"""Minimal kie.ai client: file upload, task creation, polling, download.

API key is read from the KIE_API_KEY environment variable (never commit it).
"""
import json
import os
import sys
import time

import requests

API = "https://api.kie.ai"
UPLOAD = "https://kieai.redpandaai.co/api/file-stream-upload"
KEY = os.environ["KIE_API_KEY"]
H = {"Authorization": f"Bearer {KEY}"}


def credits():
    r = requests.get(f"{API}/api/v1/chat/credit", headers=H, timeout=30)
    return r.json()["data"]


def upload(path, upload_path="fitpatches/refs"):
    with open(path, "rb") as f:
        r = requests.post(
            UPLOAD,
            headers=H,
            files={"file": (os.path.basename(path), f)},
            data={"uploadPath": upload_path, "fileName": os.path.basename(path)},
            timeout=120,
        )
    j = r.json()
    if not j.get("success") and j.get("code") != 200:
        raise RuntimeError(f"upload failed: {j}")
    return j["data"]["downloadUrl"]


def create(model, inp):
    r = requests.post(
        f"{API}/api/v1/jobs/createTask",
        headers={**H, "Content-Type": "application/json"},
        json={"model": model, "input": inp},
        timeout=60,
    )
    j = r.json()
    if j.get("code") != 200:
        raise RuntimeError(f"createTask failed: {j}")
    return j["data"]["taskId"]


def status(task_id):
    r = requests.get(
        f"{API}/api/v1/jobs/recordInfo", headers=H, params={"taskId": task_id}, timeout=30
    )
    return r.json()["data"]


def wait(task_id, every=10, timeout=1800):
    t0 = time.time()
    while time.time() - t0 < timeout:
        d = status(task_id)
        if d["state"] in ("success", "fail"):
            return d
        time.sleep(every)
    raise TimeoutError(task_id)


def result_urls(d):
    return json.loads(d["resultJson"] or "{}").get("resultUrls", [])


def download(url, path):
    r = requests.get(url, timeout=300)
    r.raise_for_status()
    with open(path, "wb") as f:
        f.write(r.content)
    return path


def create_character(description, image_urls, name=None):
    body = {"descriptions": description, "image_urls": image_urls}
    if name:
        body["character_name"] = name
    r = requests.post(
        f"{API}/api/v1/omni/character/create",
        headers={**H, "Content-Type": "application/json"},
        json=body,
        timeout=120,
    )
    j = r.json()
    if j.get("code") != 200:
        raise RuntimeError(f"character create failed: {j}")
    return j["data"]


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "credits":
        print(credits())
    elif cmd == "upload":
        print(upload(sys.argv[2]))
    elif cmd == "status":
        print(json.dumps(status(sys.argv[2]), indent=2, ensure_ascii=False))
