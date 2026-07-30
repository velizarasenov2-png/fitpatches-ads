---
name: skeleton-ad-style
description: Defines the visual/cinematographic design system for "skeleton"-style short-form video ads — the viral format built around a translucent 3D/X-ray anatomical skeleton character (popular on TikTok, YouTube Shorts, Reels). Use this skill whenever the user wants to design, prompt, or generate an advertisement, product demo, or short video clip in the "skeleton" visual style — translucent bone character, glowing X-ray anatomy, cinematic medical-visualization look — even if they call it "skeleton video", "x-ray ad", "anatomy style ad", "the skeleton trend", or just describe a see-through glowing skeleton character. Trigger this for requests about the LOOK of the video (character design, lighting, camera, color grade, materials, product integration, prompt keywords for Veo/Kling/Sora/Midjourney). This skill intentionally covers style only, not scripts, hooks, or storytelling — if the user also wants narrative/story help, say so explicitly rather than assuming it's covered here.
---

# Skeleton Ad Visual Style

This skill defines the *look* of "skeleton" short-form videos — the AI-native visual format where a translucent, X-ray-style 3D skeleton character carries the scene. It says nothing about what the ad is about, what happens, or what's said. It exists so that every clip in a campaign — regardless of product or scene — reads as unmistakably "the same skeleton universe," which matters a lot for ads: consistency is what makes a format recognizable and re-usable across many products.

Use it to write prompts for text-to-video models (Veo, Kling, Sora, Runway) or text-to-image models (Midjourney, Kie.ai, Ideogram) feeding an image-to-video pipeline. Drop the style block below onto *any* scene description the user gives you — do not invent a story, hook, or script; if they haven't described a scene/action, ask what the skeleton is doing/holding, then apply this style to it.

## Core visual identity

The character is a full or partial human skeleton rendered as **translucent, internally-lit anatomy** — not a flat cartoon prop and not a horror-movie prop. Three things make it read as "skeleton-ad style" rather than generic 3D skeleton:

1. **Translucency with glow** — bone reads as frosted/semi-transparent material (think frosted glass, blue-white resin, or bioluminescent bone) with an inner light source. Relevant organs, joints, or systems light up in a contrasting accent color when they're the focus of the shot.
2. **Medical-visualization rendering** — clean, hyper-realistic 3D render quality, like a cross between an anatomy textbook illustration and a AAA game cinematic. Not painterly, not low-poly, not cute/chibi.
3. **Cinematic studio lighting on a near-black stage** — the character is lit like a product photograph, not like a scene with ambient daylight. This is what makes it feel premium rather than gimmicky, and it's what makes any product placed with the skeleton look intentional rather than pasted in.

## Character design

- **Base material**: semi-transparent white/ice-blue bone, subsurface scattering so light bleeds through thin sections (ribs, skull, hands). Avoid matte, chalky, or fully-opaque bone — that reads as "medical model," not "skeleton-ad."
- **Accent glow**: pick one accent color per video for whatever anatomy is relevant to the product/scene (e.g. amber for digestion, cyan for nervous system, red for cardiovascular, violet for brain) — glowing from within, not painted on top.
- **Proportions**: anatomically correct, adult human proportions. Stylization is allowed in material/lighting, not in anatomy — accuracy is part of what sells the format.
- **Expression/posture**: skeletons can hold naturalistic human posture and gesture (holding a product, gesturing, reacting) without needing muscles or skin. Motion should feel weighted and physical, not floaty.
- **Product interaction**: when the ad features a product, the skeleton should physically hold, wear, point at, or stand beside it exactly as a human presenter would — full hand/finger articulation, correct grip. The product itself renders in normal, realistic material (not translucent) so it visually pops against the skeleton.

## Camera & composition

- **Format**: vertical 9:16, framed for mobile-first short-form (TikTok/Reels/Shorts).
- **Shot types**: favor tight/medium shots — chest-up or product-in-hand framing — with occasional macro push-ins on the glowing anatomy or the product's key detail.
- **Camera movement**: slow, deliberate moves only — gentle dolly-in, slow orbit, subtle parallax. No shaky/handheld, no whip pans. The stillness is what makes the glow and translucency read clearly.
- **Depth of field**: shallow, with the skeleton and product in crisp focus and the background falling into soft blur/darkness.

## Lighting & color grade

- **Key light**: cool white or pale blue rim/back light that traces the silhouette and lets translucency read.
- **Accent light**: the anatomy glow color doubles as a practical light source, casting a soft color bounce onto nearby surfaces (including the product) — this is what ties character and product together visually.
- **Background**: near-black or deep charcoal void by default. Avoid busy environments — the format's power is in the contrast between glowing figure and darkness. A subtle fog/haze layer adds depth without introducing a literal location.
- **Grade**: high contrast, deep blacks, desaturated overall except for the one accent color and the product's natural colors — the accent color and the product should be the only saturated things in frame.

## Motion & animation style

- **Idle motion**: slow breathing-like glow pulse in the lit anatomy, subtle bone/joint micro-movement — never fully static, never busy.
- **Highlight beats**: when a specific organ/system is "the point" of a moment, animate the glow intensifying or traveling to that area, synced to whatever beat/line lands there.
- **Transitions between shots**: prefer a light-flare wipe, a push through the glow, or a hard cut on a glow-pulse peak — avoid generic crossfades, which flatten the format's contrast-driven look.

## Prompt template

Append this style block to any scene/action/product description already provided — do not add plot, dialogue, or narrative beats here, that's out of scope for this skill:

```
[SCENE/ACTION DESCRIPTION HERE], translucent 3D anatomical skeleton character with frosted glass / ice-blue bone material, internal bioluminescent glow, [ACCENT COLOR] glowing highlight on [RELEVANT ANATOMY], hyper-realistic medical-visualization render, cinematic studio lighting, rim-lit silhouette, near-black void background with soft haze, shallow depth of field, vertical 9:16 composition, slow deliberate camera movement, high contrast desaturated grade with the glow and the product as the only saturated colors, product rendered in realistic opaque material held/worn naturally by the skeleton
```

**Quick keyword bank** (mix and match): translucent bone, frosted glass skeleton, bioluminescent anatomy, X-ray glow, subsurface scattering, medical visualization render, rim lighting, volumetric haze, near-black void, shallow depth of field, vertical cinematic, slow dolly, anatomically accurate, desaturated high-contrast grade, glowing organ highlight.

## What to avoid

- Cartoonish, low-poly, or "cute" skeleton designs (chibi, Halloween-prop, plastic toy look) — breaks the premium/medical read.
- Opaque, matte-white bone with no inner light — reads as a static medical model, not this format.
- Gore, exposed muscle/flesh, or horror framing — the format is clean and clinical, not scary.
- Busy or literal environments (offices, kitchens, outdoors) — keep the void-stage backdrop unless the user specifically asks to break format.
- Fast/shaky camera work — undermines the glow and translucency, which need stillness to read.
- Multiple accent colors competing in one shot — pick one per video/scene for a clean, legible highlight.

## Scope note

This skill is style-only. If the user asks for hooks, scripts, voiceover lines, or story structure for a skeleton-style ad, flag that this skill doesn't cover it and ask whether they want that handled separately.
