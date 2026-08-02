#!/usr/bin/env node
/**
 * Kie.ai — GPT Image ("gptimage") generator
 * ------------------------------------------------------------
 * Генерира ВЕРТИКАЛНО 9:16 изображение на новинарска емисия:
 *   • синя тематика
 *   • стил на филма "ParaNorman" (stop-motion / claymation, LAIKA)
 *   • САМО ЕДИН водещ — мъж
 *   • четлив надпис в правоъгълника (chyron): "Решение за сладките изкушения"
 *
 * Използва официалния Kie.ai Jobs API (createTask + recordInfo polling).
 *
 * Употреба:
 *   export KIE_API_KEY="твоят_ключ"
 *   node generate.mjs
 *
 * По желание (env override):
 *   KIE_MODEL   – моделът в Kie (по подразбиране "gpt-image-1")
 *   KIE_SIZE    – съотношение / размер (по подразбиране "2:3" — най-близкото вертикално към 9:16)
 *   OUT_DIR     – къде да се запише файлът (по подразбиране текущата папка)
 * ------------------------------------------------------------
 */

import { writeFile } from "node:fs/promises";
import { join } from "node:path";

// ---------- Config ----------
const API_KEY = process.env.KIE_API_KEY;
const MODEL = process.env.KIE_MODEL || "gpt-image-1";
const SIZE = process.env.KIE_SIZE || "2:3"; // GPT Image портрет; 9:16 се задава и в промпта
const OUT_DIR = process.env.OUT_DIR || process.cwd();

const BASE = "https://api.kie.ai/api/v1";
const CREATE_URL = `${BASE}/jobs/createTask`;
const INFO_URL = `${BASE}/jobs/recordInfo`;

// ---------- Промпт ----------
// Точният надпис за правоъгълника — държим го кратък и в кавички за максимална четливост.
const BANNER_TEXT = "Решение за сладките изкушения";

const PROMPT = `A vertical 9:16 portrait television NEWS BROADCAST scene, rendered in the distinctive handcrafted STOP-MOTION CLAYMATION style of the LAIKA film "ParaNorman": textured clay / porcelain skin with visible sculpt marks and fingerprints, slightly exaggerated caricatured features, large expressive eyes, quirky whimsical-gothic mood, soft cinematic lighting, shallow depth of field, subtle film grain.

Scene: EXACTLY ONE male news anchor — a single presenter, no co-host, no second person — sitting at a modern glossy news desk, centered, facing the camera, wearing a dark suit and tie, calm professional expression.

Color theme: an overall COOL BLUE studio — blue backdrop panels with a soft glow, blue ambient lighting, blue reflective desk surface, blue graphics.

Lower third: at the bottom of the frame there is a clean rectangular news banner (chyron / lower-third graphic). It displays large, crisp, perfectly LEGIBLE Cyrillic text that reads EXACTLY, correctly spelled, word for word:
"${BANNER_TEXT}"
White high-contrast lettering on a blue banner, sharp and easy to read, no misspellings, no garbled or duplicated letters.

Framing: vertical 9:16, broadcast composition, professional TV graphics, high detail, cinematic.`;

// ---------- Helpers ----------
function assert(cond, msg) {
  if (!cond) {
    console.error(`\n❌ ${msg}\n`);
    process.exit(1);
  }
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function api(url, opts) {
  const res = await fetch(url, opts);
  const text = await res.text();
  let json;
  try {
    json = JSON.parse(text);
  } catch {
    throw new Error(`Non-JSON response (${res.status}): ${text.slice(0, 500)}`);
  }
  if (!res.ok) {
    throw new Error(`HTTP ${res.status}: ${JSON.stringify(json).slice(0, 500)}`);
  }
  return json;
}

// ---------- Main ----------
async function main() {
  assert(API_KEY, "Липсва KIE_API_KEY. Изпълни: export KIE_API_KEY=\"твоят_ключ\"");

  const headers = {
    Authorization: `Bearer ${API_KEY}`,
    "Content-Type": "application/json",
  };

  console.log("🎬 Създавам задача в Kie.ai…");
  console.log(`   модел: ${MODEL} | размер: ${SIZE}`);

  const createBody = {
    model: MODEL,
    input: {
      prompt: PROMPT,
      // Различните модели използват различни имена за размера — подаваме и двете,
      // непознатите полета обикновено се игнорират.
      image_size: SIZE,
      size: SIZE,
      aspect_ratio: "9:16",
      n: 1,
    },
  };

  const created = await api(CREATE_URL, {
    method: "POST",
    headers,
    body: JSON.stringify(createBody),
  });

  // Kie връща { code, msg, data: { taskId } }
  const taskId = created?.data?.taskId || created?.data?.task_id || created?.taskId;
  assert(taskId, `Не получих taskId. Отговор: ${JSON.stringify(created)}`);
  console.log(`✅ Задача създадена: ${taskId}`);

  // ---------- Polling ----------
  console.log("⏳ Изчаквам генерирането…");
  const maxTries = 120; // ~10 мин при 5 сек интервал
  let imageUrl = null;

  for (let i = 0; i < maxTries; i++) {
    await sleep(5000);
    const info = await api(`${INFO_URL}?taskId=${encodeURIComponent(taskId)}`, {
      method: "GET",
      headers,
    });

    const d = info?.data || {};
    // Kie state: "waiting" | "queuing" | "generating" | "success" | "fail"
    const state = (d.state || d.status || "").toString().toLowerCase();
    process.stdout.write(`   [${i + 1}] статус: ${state || "неизвестен"}\r`);

    if (["success", "succeeded", "completed"].includes(state)) {
      imageUrl = extractUrl(d);
      break;
    }
    if (["fail", "failed", "error"].includes(state)) {
      throw new Error(`Генерирането се провали: ${d.failMsg || d.failMessage || JSON.stringify(d)}`);
    }
  }

  console.log("");
  assert(imageUrl, "Времето изтече — не получих готово изображение.");

  console.log(`🖼️  Готово изображение: ${imageUrl}`);

  // ---------- Download ----------
  const res = await fetch(imageUrl);
  assert(res.ok, `Неуспешно сваляне: HTTP ${res.status}`);
  const buf = Buffer.from(await res.arrayBuffer());
  const stamp = new Date().toISOString().replace(/[:.]/g, "-");
  const outPath = join(OUT_DIR, `news-paranorman-${stamp}.png`);
  await writeFile(outPath, buf);

  console.log(`💾 Записано: ${outPath}`);
}

// Резултатът може да е на различни места според модела/версията.
function extractUrl(d) {
  if (typeof d.resultUrls === "string") return d.resultUrls;
  if (Array.isArray(d.resultUrls) && d.resultUrls[0]) return d.resultUrls[0];
  if (d.resultJson) {
    try {
      const parsed = typeof d.resultJson === "string" ? JSON.parse(d.resultJson) : d.resultJson;
      const arr = parsed?.resultUrls || parsed?.images || parsed?.urls;
      if (Array.isArray(arr) && arr[0]) return typeof arr[0] === "string" ? arr[0] : arr[0]?.url;
      if (typeof arr === "string") return arr;
    } catch {}
  }
  if (Array.isArray(d.images) && d.images[0]) return d.images[0]?.url || d.images[0];
  if (typeof d.imageUrl === "string") return d.imageUrl;
  return null;
}

main().catch((err) => {
  console.error(`\n❌ Грешка: ${err.message}\n`);
  process.exit(1);
});
