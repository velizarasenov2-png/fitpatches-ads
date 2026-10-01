---
name: market-scan
description: Ежедневен скан на конкурентите в Meta Ads Library. Нови реклами, най-дълго въртящите, кой скалира, нови формати и оферти, плюс 3–5 адаптации за FitPatches, които отиват в симулацията. Обновява радара в играта FitPatches HQ. Използвай при „какво правят другите“, „конкуренти“, „нови формати“, „market scan“.
argument-hint: "[дата или фокус, напр. „лепенки“]"
---

# /market-scan: какво работи на пазара днес

1. Пусни агента `market-scout` с фокуса `$ARGUMENTS` (по подразбиране пълният ежедневен скан по `team/lab/intel/watchlist.json`). Той записва:
   - `team/lab/intel/ГГГГ-ММ-ДД.md` и `latest.json`;
   - `ads-seen.jsonl`, `format-trends.md`, `swipe-file.md`;
   - нови CB-### в `team/creative-backlog.md`.
2. Играта: `python3 lab/hq_sync.py radar` → ArtifactData `batch` към https://claude.ai/artifact/AzfuqaQVNWi6gkeD7SGVRZ (`hq/radar`, `agents/market-scout`, `quests/q-scan`, ред в `log/<днес>`).
3. Покажи на собственика блока „🛰️ ПАЗАРЪТ ДНЕС“ от скаута.
4. Ако има поне 2 силни адаптации, предложи `/ad-lab ideas <CB-…>`, за да минат през симулацията. Ако собственикът е пуснал `/daily-lab`, продължи директно.
5. Commit-ни `team/lab/intel/` и `team/creative-backlog.md`.
