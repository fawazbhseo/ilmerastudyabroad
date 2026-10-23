<?php
/** Phase 25 Stage 1: opt-in only, never a template-wide rollout. */
if (!defined('ILMERA_VISUAL_PILOTS_ENABLED')) define('ILMERA_VISUAL_PILOTS_ENABLED', true);
/** One sitewide scene switch. Set false for plain reference-palette heroes. */
if (!defined('ILMERA_SCENES_ENABLED')) define('ILMERA_SCENES_ENABLED', true);

/** Hard performance gate: failing pilots drop to a palette-only hero. */
if (!defined('ILMERA_PILOT_SCENE_TIERS')) define('ILMERA_PILOT_SCENE_TIERS', ['destination'=>'plain','place'=>'plain','article'=>'plain','blog'=>'plain']);

/** Stage2 groups are enabled in separately checked task commits. */
if (!defined('ILMERA_VISUAL_TEMPLATE_GROUPS')) define('ILMERA_VISUAL_TEMPLATE_GROUPS', ['destination','place']);
/** Only templates failing the fixed font budget may use the inline fallback. */
if (!defined('ILMERA_VISUAL_INLINE_FONT_TEMPLATES')) define('ILMERA_VISUAL_INLINE_FONT_TEMPLATES', []);
/** Performance fallback is a plain colour, never a generated image. */
if (!defined('ILMERA_VISUAL_PLAIN_HERO_TEMPLATES')) define('ILMERA_VISUAL_PLAIN_HERO_TEMPLATES', []);
