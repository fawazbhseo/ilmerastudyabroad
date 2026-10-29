#!/usr/bin/env node
// Encode the mobile still from the existing approved WebP without changing its content.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const sharp = require('sharp');
const ROOT = path.resolve(__dirname, '../..');
const source = path.join(ROOT, 'assets/images/hero-still-720.webp');
const output = path.join(ROOT, 'assets/images/hero-still-640.webp');
(async () => {
  await sharp(source)
    .resize({ width: 640, height: 800, fit: 'cover' })
    .webp({ quality: 64, effort: 6, smartSubsample: true })
    .toFile(output);
  const bytes = fs.readFileSync(output);
  const metadata = await sharp(output).metadata();
  const desktop = path.join(ROOT, 'assets/images/hero-still-1440.webp');
  const desktopMeta = await sharp(desktop).metadata();
  const record = {
    phase: 32,
    method: 'sharp WebP quality 64, effort 6, smart subsampling; resized from the approved 720x900 mobile source to matching 640x800 aspect ratio',
    mobile: {
      path: 'assets/images/hero-still-640.webp',
      width: metadata.width,
      height: metadata.height,
      bytes: bytes.length,
      sha256: crypto.createHash('sha256').update(bytes).digest('hex'),
      limit_bytes: 14000,
      size_gate: bytes.length <= 14000 ? 'PASS' : 'FAIL'
    },
    desktop: {
      path: 'assets/images/hero-still-1440.webp',
      width: desktopMeta.width,
      height: desktopMeta.height,
      bytes: fs.statSync(desktop).size,
      sha256: crypto.createHash('sha256').update(fs.readFileSync(desktop)).digest('hex'),
      limit_bytes: 40000,
      reused_without_reencoding: true,
      size_gate: fs.statSync(desktop).size <= 40000 ? 'PASS' : 'FAIL'
    },
    visual_review: {
      viewports: [360, 768, 1280],
      under_dark_overlay: 'PENDING browser render review'
    },
    no_new_wording_or_visual_artwork: true
  };
  if (record.mobile.size_gate !== 'PASS' || record.desktop.size_gate !== 'PASS') {
    throw new Error('A still exceeds the owner size limit');
  }
  fs.writeFileSync(path.join(ROOT, 'reports/phase-32-hero-assets.json'), JSON.stringify(record, null, 2) + '\n');
  console.log(JSON.stringify(record, null, 2));
})().catch(error => { console.error(error); process.exit(1); });
