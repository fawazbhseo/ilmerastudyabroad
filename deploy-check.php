<?php
// TEMPORARY owner upload check. Delete this file immediately after one use.
const ILMERA_DEPLOY_CHECK_KEY = '596b2f06f047c76730364c34857c6b47d03b019b21f8818960752a42fe104d9f';
// Valid through 2026-11-15 UTC; fails closed from 2026-11-16 00:00:00 UTC.
const ILMERA_DEPLOY_CHECK_EXPIRES_AT = 1794787200;
header('X-Robots-Tag: noindex, nofollow, nosnippet');
header('Cache-Control: no-store, max-age=0');
header('Pragma: no-cache');
header('Expires: 0');
header('Referrer-Policy: no-referrer');
header('X-Content-Type-Options: nosniff');
header("Content-Security-Policy: default-src 'none'; frame-ancestors 'none'; base-uri 'none'; form-action 'none'");
$query = $_SERVER['QUERY_STRING'] ?? '';
$key = $_GET['key'] ?? null;
if (($_SERVER['REQUEST_METHOD'] ?? 'GET') !== 'GET'
    || time() >= ILMERA_DEPLOY_CHECK_EXPIRES_AT
    || count($_GET) !== 1 || !is_string($key)
    || !preg_match('/\Akey=[a-f0-9]{64}\z/D', $query)
    || !hash_equals(ILMERA_DEPLOY_CHECK_KEY, $key)) {
    http_response_code(404);
    header('Content-Type: text/plain; charset=UTF-8');
    echo 'Not found';
    exit;
}
// Exact fixed allowlist. No filesystem discovery, directory listing or file input.
// .htaccess entries are exists-only and are NEVER opened or hashed.
$files = [
    '.htaccess' => ['660f6611834716f7befe4a29ff4c1e69832934cfc9764f3eab517a0b5e9351cb', false],
    '404.php' => ['2f9fc981044bb92f68e794bb0f5b43cf5e8164473273eba802ebe6cca5550b94', false],
    'about.php' => ['bb5460d63aa98a63b001d956b251326d856a0bed72adbe1f091d3d5358e173ba', false],
    'all-pages.php' => ['a388cc951cc9dd627383d550ef310abbcefd5cdc4ff91726cc70aa36be9dfc7e', false],
    'assets/css/visual-system.css' => ['2f7086f6124c68f5ab7a5fbc864e61b2b25b29219914de06119231aa248cf71f', true],
    'assets/fonts/.htaccess' => ['abbda2062f1e1c57c9771a8b50a002ba3f239fa04d20f0efaf714ce0264d41e8', false],
    'assets/fonts/cormorant-garamond-OFL.txt' => ['732f37009943e7f4378cf37113c9bcc4716af002a8583511aa91ed5d37683e73', true],
    'assets/fonts/cormorant-garamond-latin.woff2' => ['0ee72c59334ef2ffee83ebb314be26d74fcae1be428c9e1035eaf60ee293f3b4', true],
    'assets/fonts/cormorant-garamond-reference-400.woff2' => ['727acdbfd81848bcc9a5c2a6c64ba1b97ba93c69515382785483ce0cc068be08', true],
    'assets/fonts/cormorant-garamond-reference-700.woff2' => ['949a2a601dd37c9aeb888b1ce6ce17383173aaea128af4a16df45e77e6fcd903', true],
    'assets/fonts/outfit-OFL.txt' => ['0e5fcef5d93bfcae273c11c00f0bb453d3b5491860e1ac8b658767b7577c938f', true],
    'assets/fonts/outfit-latin.woff2' => ['db614390b3f3ac79f7731a50d6ff2494c818aaf788475322b83c3ff9faa9e854', true],
    'assets/fonts/outfit-reference-300.woff2' => ['ef88e74f63ce75b54cce4d5a4087c6f180750b9ebae6ab6e5bf2a9939bf6958f', true],
    'assets/fonts/outfit-reference-400.woff2' => ['71f028fd2349990b3f8aa643abe767e82e0f596be407ae66f0004ff164121bdb', true],
    'assets/fonts/outfit-reference-500.woff2' => ['fc9bff941def6d924a71632bd8a93190528872eae6414844f3c367ff948d92fd', true],
    'assets/fonts/outfit-reference-600.woff2' => ['8cfe15c2c6de6ef8efff3eedbd52a383ac9ef23d6c23f6cd9f9b838f5f37dc36', true],
    'assets/fonts/outfit-reference-700.woff2' => ['5d5e3734089a74707292ce8a3e186def34cd63e33879f9ac3689a8d8da9d0706', true],
    'assets/images/fawazbh-192.webp' => ['fc27a85edaa4ec5dbd231b51d28f20cacdcce2bdc3cb7ed27c17fa68eca3ba76', true],
    'assets/images/fawazbh-384.webp' => ['a3c401504f579ac5add974098560858fb8718993007318029278f31ae6488f3b', true],
    'assets/images/ilmera.logo.png' => ['6fd63c7cfdc05ca354237b98f0869cccbde222bf4b0b5dc55233ef7b9e097fc6', true],
    'assets/images/jabirkj.png' => ['b4d2e443f8677081c2f8e330cb286144df00c256cd9fbedde718722ebb3d445b', true],
    'assets/images/jabirkj.webp' => ['88069b124c6df86c5c598fecd88c1ecdc2173ef136f49d137448027422b63ac9', true],
    'assets/images/zaheer.png' => ['cfda6caaed6238aa1f0fbd8b1b68274f761e40f0c97088f42095824fb8c84d0f', true],
    'assets/images/zaheer.webp' => ['47bb651aad0f070eac57f0ce88c9ed937f85342f77b669d5976b558db65ff4db', true],
    'blog/cost-of-studying-abroad-for-indian-students.php' => ['9d7d4ab680ffb1d01688c1433f3f7a87bf3093cf1b0a085139c159c5936e2d06', false],
    'blog/documents-needed-to-study-abroad-from-india.php' => ['e8ba9efc53a5a72f4aa0c1531e9c42355b8a2887b265513a6e472181c14e6d48', false],
    'blog/how-to-choose-study-abroad-consultant-karnataka.php' => ['7a3381505ba28a1cc1ec6839863c53ee244166a2ad6fdafd35697e2ff6a8b8b4', false],
    'blog/index.php' => ['68fa591ced9d5eb936cf9aea565f4a573562846aaa6c4e59aa42827414cbbe4e', false],
    'blog/italy-dsu-scholarship-eligibility.php' => ['fd3806921210beafcd7a97ffc8aa69e1fb8f608735afa4e87e14a051bd146faa', false],
    'blog/scholarships-for-indian-students-study-abroad.php' => ['7fb048f05eb66c3cad82978acb5c39c484910f1dab52a04542a78a020ce46bce', false],
    'blog/study-abroad-counselling-from-coorg.php' => ['3947b7fb08218a29f5e5db90cff5138d07dd807b6e39716f6f2ed346d0464c58', false],
    'blog/study-abroad-with-academic-backlogs.php' => ['91ac6545badec32b3e21c0404f6a75522f32af9acf698a198e8ee8319cae1d2e', false],
    'blog/study-in-germany-free-aps-certificate.php' => ['b7ee7ebb27d577e1dba58133475234bfbb0f7f4db1d3ac46c5f6778faa0c2550', false],
    'contact.php' => ['634697a2ee0b1c9bcea2c7bff958f2bee0affc7a052a8a485a2c4e3a4ae29ac2', false],
    'data/.htaccess' => ['4aaacd52bae18883060e4b3fa64b2cd1bf5010262940e61683d7c1f9e7604163', false],
    'data/answer-map.json' => ['d70fd5794091ed2d1a6af4f5c15c89bcf986989616dedccd36e748c8b3626f74', true],
    'data/entity.json' => ['81fbda98cfd8a54dd58fc5cb475e676a26c10dd43494d3b0f1bfeb44ce600340', true],
    'data/payment-disclosure.json' => ['1abfeaae9d046025bb6bd77ab71df83a28cb9ea51aea6abe359ad3d27b285ea8', true],
    'data/proof.php' => ['ecefe4ef7c4f55ebaf9b3e3f29e4f2a11d8528d934fa8dfd5fcb1323884fee08', true],
    'data/seo-map.json' => ['a1f8e62a2ef238e6812ff6e64d4f6192aceb21452fc90f1ed444b810f62e5276', true],
    'data/service-scope.json' => ['47dcdba726c5dbcd17897d94b4b0a861f114e6ec515b4e0535db89d53c1521b3', true],
    'data/team.json' => ['35cb45fc1222d47dd39c2b022addea6c2a7cb8765cfcc01115e3f3ff7a8f9ca4', true],
    'destinations/.htaccess' => ['4aaacd52bae18883060e4b3fa64b2cd1bf5010262940e61683d7c1f9e7604163', false],
    'destinations/czech-republic.php' => ['cf0407523240d008916a1e5a6a289421ea92c5e476e8874e8fc4f597ef172bda', true],
    'destinations/gcc.php' => ['6db58df85f2d6d21dd1419572e5e846b0e599d51e666bf734c192a72ef2d4cd6', true],
    'destinations/germany.php' => ['2aa14f954c8937be695e664b1fc9ed9a3759e2986ddc15d6889beb896429e370', true],
    'destinations/italy.php' => ['31b1d68973a9af9d558bc11ce6b32e086e057a75aa559712604a05686b843296', true],
    'destinations/latvia.php' => ['f4a13cae2465636b2ea36a7a0cc796c0e355a644b1f7b8ebc5f7ec5976d9a0f4', true],
    'destinations/lithuania.php' => ['a8c636c9fc7abd0470b137594b94d3fb7949f20f4a2e0059fa3b70a90e2d3ad4', true],
    'destinations/russia.php' => ['b7344b9b6614c0321999a61bc5716bfa83d2870d4e9fb6ea55b33d00989de899', true],
    'destinations/slovakia.php' => ['3e8cac1ca1821edb7941cd4ed613bfa63182927afa8865cb64e70b19c7890bf3', true],
    'destinations/uk.php' => ['c61a8263e579e2922684d76b835ee60983a8ce39deb2830fb823f7cedd781012', true],
    'favicon.ico' => ['d56f454c1b22b448f00503c856b9a8079475e9eec6b1efccc86b1fd58534b679', false],
    'google10fa7a4178242a1f.html' => ['ac24b3229f0855ab347e78ddf8588756f33479657459805addf802e201bfc92a', false],
    'includes/.htaccess' => ['4aaacd52bae18883060e4b3fa64b2cd1bf5010262940e61683d7c1f9e7604163', false],
    'includes/breadcrumbs.php' => ['d07ac0d14e6b6f87c4554ccdbd07db56464a676c8c4bfeef8c083ba473f1c139', true],
    'includes/destination-data.php' => ['fc17211f547b456343081b6dc7dfbf7ecc15d20fc54403f65370953bad8cdfe9', true],
    'includes/destination-page.php' => ['ff93a4f875b559d71c3115672684c98cc907b77b3bd944b5b0855154a884795d', true],
    'includes/entity.php' => ['a9d0b3e6b993db7c1c442f5e888abdebfd699e371b3101a592bd6b2aab288c9c', true],
    'includes/footer.php' => ['52c606828e1065acfbe62115fdbb4fa593ca0487081e454334fba5936550a240', true],
    'includes/header.php' => ['f1a5666aec8a7b80e25b743c19110950c367f1373242217099e4d21760bdb63e', true],
    'includes/links.php' => ['886bbefc854f85a652d382e5caeef32fbe575fe2b50b3398aa95df2e7841435e', true],
    'includes/payment-disclosure.php' => ['258847ed695eec19d0a4fa791be49f4e1c12478fcac2be9f713a570c3174c949', true],
    'includes/place-data.php' => ['9ecce15409d5ac6348c479c496e292c7138e973db3dc00c3337cc493b7e3333e', true],
    'includes/place-page.php' => ['6020d83eeeac11f4b72e41eacd49940c6f83bb34a8ef4b536d47b19d769ec7b2', true],
    'includes/posts.php' => ['fe3f312e467e9d7b9d46b3d667da4350d6a20a0ae9b3b87f9ec112552a39c40e', true],
    'includes/proof.php' => ['13a0285a4a0495f0492cbeb305e0fbbeef885314b0f9a849231918f4a4aa7425', true],
    'includes/service-scope.php' => ['d4f09736d8ba9adb47f2dbc55785c420be9787b675f02b0d7d933d3c896fe10b', true],
    'includes/site-presentation.php' => ['6fc9c360bfbf3f72be029e47c6e2a8ff219d3684f85c10bade238b93a49f310c', true],
    'includes/sitemap-data.php' => ['13a1e920ea86620ad7404d9bcab665678d9c3b9991f40986e80185bca8bd05ad', true],
    'includes/visual-config.php' => ['f68570eb69bef74850f06c4d54b488fcdf1ec1a5a81f37d563eef53dab4e2c76', true],
    'includes/visual-system.php' => ['95858ce9008bebf54b58075d07a653441233cf7d5dc67b5815a790a62b6b9a6f', true],
    'index.php' => ['5ec4bcf5ca18b262588952150838d9e92985d68a5ae620e7579a9057eaa58b3a', false],
    'llms-full.txt' => ['097dc9abb2eeb8377a091843d0b20489c8f04141e81da757e8bfe852078e7299', false],
    'llms.txt' => ['ad99c63172bbf4029b2937a0fb824b21f422345b10f4a8764c5c172344db61d8', false],
    'phase14-article-review.json' => ['2d7a71ab15ff3167c5ea5d5dafb5de24b6a057576e677528a695f3711fcb519d', true],
    'phase14-location-review.json' => ['252510cfc9e60dc00bfe91255d85320d1b73c6f627866b20e9500d41a6ddbeab', true],
    'phase14-source-review.json' => ['80eb69b4a7a70f162a2cf270e0221a80b761d325c2685ceddb0c0e2cf4563fae', true],
    'places/.htaccess' => ['4aaacd52bae18883060e4b3fa64b2cd1bf5010262940e61683d7c1f9e7604163', false],
    'places/belagavi.php' => ['091c0653e3ef037bd7af0522bb98195c9751c2531b9fa9f50ba2423f6eba6d6d', true],
    'places/bengaluru.php' => ['a72348f273f40fed28312c64a412071223d0fa6bd9085778407cf75cb47df2d2', true],
    'places/chikkamagaluru.php' => ['69f23aa0174c56e2c4735639084dbb886a649b3b0f2ba700e0e950434f716380', true],
    'places/gonikoppal.php' => ['33d88d5b15d71bacaedbb1f283eb86d50afa1b28971070141e6b3f5a6f940867', true],
    'places/hassan.php' => ['b618383155075bb0c564a8b77a6454f78b49f00315d1e0e65f4fee670eb47fcf', true],
    'places/karnataka.php' => ['b42265c20440f1d92f7236f59036d748bdd76b7c9efcf8d2322405c3d5db96ac', true],
    'places/kodagu.php' => ['e7baab44e0c5903e821a873b2c5e55bacb697c68fb8af07b6225a5d9f67f4594', true],
    'places/kushalnagar.php' => ['a54a8caca296bc0baa8029943aab6b4edfddb3743b736156df30fa658dc757af', true],
    'places/madikeri.php' => ['373c9033c1b2aaec0dfb8ae9fe60886809ae221b832c690633cc6dd783b0cae9', true],
    'places/mangaluru.php' => ['86d74674ab9c6195e0cbd925d94f1118b1dbc476c8087a0f6468bfcc18076cbd', true],
    'places/mysuru.php' => ['3ea32edd15cd3681fd05a4070cc7a12b267942547c280b4cd011fa0591a1f2f3', true],
    'places/ponnampet.php' => ['8ffd85b53ea9bd3b1e8a40bac6ce6a8e51be5d4d8e8ad1cacab5d522635807aa', true],
    'places/shivamogga.php' => ['432420abf7fb9f6d1535e7150876e5935783c143adbed38417dff8f12ce588b7', true],
    'places/siddapura.php' => ['489d4601332a8846e4d592696aa6d05af058355dba43d0a2f9212b78514a649a', true],
    'places/somwarpet.php' => ['d6c30cbdc69175b0b69c194e6c2da38d2bfd17bc37344aacaa18e8317204b521', true],
    'places/udupi-manipal.php' => ['93658572dc0ed5ef6f9d2aded20653ec7fac115405b4075daecdfee1652b55ec', true],
    'places/virajpet.php' => ['14c8be5bc79b1da8d88a335fe1459b24132ef0863d246da7f40d0318104f5e92', true],
    'privacy-policy.php' => ['bcfe3e889f51a04c984f84232f6e2d72eeefb8f83ef2de9c5449d1239aa5e678', false],
    'reports/.htaccess' => ['4aaacd52bae18883060e4b3fa64b2cd1bf5010262940e61683d7c1f9e7604163', false],
    'robots.txt' => ['1547d6509231507a8e84350c975b45abc22cf79646dd93d6518ad6b62eb32a80', false],
    'services.php' => ['4da5d8b95fa68bb7f6be4a5ccf99fdc32a28947c9207104b5b8019f9b25888b1', false],
    'sitemap.php' => ['536a08d40515e0f819cf6c9418a4b0a5bb28b6e8c4c040a77b82d6da8ea7dd3d', false],
    'sitemap.xml' => ['de23394bfe3150db0a29d684f4f13187f644a4bba617beeabeaf0d19e769ddbb', false],
    'study-abroad-consultants-in-karnataka.php' => ['63d171436b94729fb1151caf697e09fdda57e8fc71c0e642f17f14e73beb03ed', false],
    'study-abroad-consultants-in-kodagu.php' => ['dc58ac2d5cf467846d5a5d88b7a602da913997a7399a23b7d1b990339a4a7a56', false],
    'study-abroad-counselling-belagavi.php' => ['8569ed1180f7569ef9edc19d1add9bc960295fc7f009105a40485f37fdf203ad', false],
    'study-abroad-counselling-bengaluru.php' => ['3bb7bd9b6ce2a0bded5925559528b1b3947d502c66b224cd016d416328d2ab54', false],
    'study-abroad-counselling-chikkamagaluru.php' => ['f4ddff551eaf30abfda7b6e6161bbb78018578daf46f30f1f7463dcbb691f3b2', false],
    'study-abroad-counselling-gonikoppal.php' => ['7b44b418650b3b405411c2b273533602f61dafe654f5102ce176ba321617491b', false],
    'study-abroad-counselling-hassan.php' => ['7861fc22b3a4a179bcdb80e29e9e85b32ea321e7da1b0a28188bbd9950f97086', false],
    'study-abroad-counselling-kushalnagar.php' => ['7cfdb76c5eff0c4041f7de5afd4aede9bf7c17e7c3137234d7be2f18b8992d3b', false],
    'study-abroad-counselling-madikeri.php' => ['0c725d6b405ac574c6913a05114192db0830376e5db0f77fffe5031f87006e50', false],
    'study-abroad-counselling-mangaluru.php' => ['c7f921cc379c99e186ba6581e9cfd6b41394e08f2297b76eef2bbdcd2ca588f5', false],
    'study-abroad-counselling-mysuru.php' => ['a33db2c6f60c418d76d977465cfa3d0c03ea1ab9448b7e757219f2282ef6eee7', false],
    'study-abroad-counselling-ponnampet.php' => ['9e562ce8f83b4a0f1fa2a310d05e90cbd8a287eb4b56cb6332d358c06622394d', false],
    'study-abroad-counselling-shivamogga.php' => ['628bdf9cd36de86a665d87948bbd9da319654fdae7bec680597da62d8b27f16b', false],
    'study-abroad-counselling-siddapura.php' => ['6c0f16d742f8df2a4be8d466d760feb6309ea7dca45ee008e47ab6d9481ef700', false],
    'study-abroad-counselling-somwarpet.php' => ['ffef272069a438522dc81fb3d552c241cce502e9bc7c3d220ba267176b51326d', false],
    'study-abroad-counselling-udupi-manipal.php' => ['3b86ac35796d52abd787e7481b1eeaa8400732589b42430f908daf0a9b56d259', false],
    'study-abroad-counselling-virajpet.php' => ['dcd586d6ef3b20e5b94d91bd552adf90b094fbe6851d7e12738da3be187c2099', false],
    'study-in-czech-republic.php' => ['4ae3173109a265f2e11bf88272f56615cfad4f166bb16979b3dcd27c2584f540', false],
    'study-in-gcc.php' => ['3a3dfb9bbf792dbfdeef1df1dd2b946ca56f26840977a183aba7f29135c09742', false],
    'study-in-germany.php' => ['55eac97163c432f303ec3adcfca71449f4564283cb8d1e21f8bcb95e08d25957', false],
    'study-in-italy.php' => ['43992ec2d013d4cd7578077f8878289144bc15a08738fb28834025f6e6292b98', false],
    'study-in-latvia.php' => ['967a8b00d4968c95e9f372ede5bec94ceb5f89ba10c16c82da9c605498b65ae1', false],
    'study-in-lithuania.php' => ['33461b00e923b7483d11ff72f9dec2631f4988c09dc821ffe1b5c4be16720b92', false],
    'study-in-russia.php' => ['1f3a264697834e81249a63090d494d08d12de8798bad69efc36bb4baf5a91ea3', false],
    'study-in-slovakia.php' => ['45e7a07ae40bf44d9c3c1d47cf56caecaedfa7695091ae1d8a1209c90d4bfede', false],
    'study-in-uk.php' => ['d541855e9b8895556c249538a60623b6f790912642210b003ab7370906ec52f8', false],
    'terms.php' => ['6ebc101e222a1a20c4db8418663ee7198038d5a111a792917930d4bcf1b7a7a7', false],
    'tools/.htaccess' => ['4aaacd52bae18883060e4b3fa64b2cd1bf5010262940e61683d7c1f9e7604163', false],
];
$rows = [];
$problems = [];
foreach ($files as $relative => $check) {
    $file = __DIR__ . '/' . $relative;
    $exists = @is_file($file) && !@is_link($file);
    $critical = $check[1] && basename($relative) !== '.htaccess';
    $readable = $exists && @is_readable($file);
    $size = $critical && $readable ? @filesize($file) : null;
    $hash = $critical && $readable ? @hash_file('sha256', $file) : false;
    $matches = $critical && $readable && is_string($hash) && hash_equals($check[0], $hash);
    if (!$exists) $problems[] = [$relative, 'MISSING'];
    elseif ($critical && !$readable) $problems[] = [$relative, 'UNREADABLE'];
    elseif ($critical && !$matches) $problems[] = [$relative, 'HASH MISMATCH'];
    $rows[] = [$relative, $exists, $critical, $readable, $size, $matches];
}
// Self-hashing would create a circular manifest. The temporary file checks only
// its own existence; its actual ZIP/manifest hash is verified by offline tooling.
$selfExists = @is_file(__DIR__ . '/deploy-check.php') && !@is_link(__DIR__ . '/deploy-check.php');
if (!$selfExists) $problems[] = ['deploy-check.php', 'MISSING'];
$rows[] = ['deploy-check.php (temporary; delete after use)', $selfExists, false, false, null, false];
$escape = static function ($value) { return htmlspecialchars((string)$value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'); };
header('Content-Type: text/html; charset=UTF-8');
echo '<!doctype html><html lang="en"><meta charset="UTF-8"><meta name="robots" content="noindex,nofollow,nosnippet"><title>Temporary upload check</title><body>';
echo '<h1>' . ($problems ? count($problems) . ' PROBLEMS FOUND' : 'ALL FILES OK') . '</h1>';
echo '<p>Temporary check. Delete deploy-check.php after sending the result.</p><table><tr><th>PHP version</th><td>' . $escape(PHP_VERSION) . '</td></tr></table>';
echo '<h2>FAIL</h2>';
if (!$problems) echo '<p>None.</p>';
else { echo '<ul>'; foreach ($problems as $problem) echo '<li>' . $escape($problem[0]) . ': ' . $escape($problem[1]) . '</li>'; echo '</ul>'; }
echo '<table border="1"><tr><th>Fixed payload path</th><th>Exists</th><th>Readable (critical)</th><th>Bytes (critical)</th><th>SHA-256 matches (critical)</th></tr>';
foreach ($rows as $row) {
    echo '<tr><td>' . $escape($row[0]) . '</td><td>' . ($row[1] ? 'YES' : 'MISSING') . '</td>';
    echo '<td>' . ($row[2] ? ($row[3] ? 'YES' : 'NO') : '-') . '</td>';
    echo '<td>' . ($row[2] ? ($row[4] === null ? '-' : $escape($row[4])) : '-') . '</td>';
    echo '<td>' . ($row[2] ? ($row[5] ? 'MATCH' : 'FAIL') : '-') . '</td></tr>';
}
echo '</table><p>Noncritical files and policies are existence-only. No .htaccess content is read. This is not native hosting, rewrite, cache, CSP, contact or performance certification.</p></body></html>';
