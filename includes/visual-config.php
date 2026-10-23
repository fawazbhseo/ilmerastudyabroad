<?php
/** Phase25 Stage2: template-scoped presentation; reference pages excluded. */
/** One sitewide scene switch. Set false for plain reference-palette heroes. */
if (!defined('ILMERA_SCENES_ENABLED')) define('ILMERA_SCENES_ENABLED', true);



/** Stage2 groups are enabled in separately checked task commits. */
if (!defined('ILMERA_VISUAL_TEMPLATE_GROUPS')) define('ILMERA_VISUAL_TEMPLATE_GROUPS', ['destination','place','article','blog','legal','utility']);
/** Only templates failing the fixed font budget may use the inline fallback. */
if (!defined('ILMERA_VISUAL_INLINE_FONT_TEMPLATES')) define('ILMERA_VISUAL_INLINE_FONT_TEMPLATES', ['destination']);
/** Performance fallback is a plain colour, never a generated image. */
if (!defined('ILMERA_VISUAL_PLAIN_HERO_TEMPLATES')) define('ILMERA_VISUAL_PLAIN_HERO_TEMPLATES', ['destination']);
