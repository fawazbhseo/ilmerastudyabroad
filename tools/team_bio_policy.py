"""Exact Phase 24b owner-approved biography contexts, not institutional endorsements."""
ZAHEER = "Zaheer KJ is the Chief Financial Officer of ILMERA Study Abroad and a digital marketer with a certification from Adrex Media School. He manages ILMERA's finance and paperwork, including documentation."
FAWAZ = "Fawaz BH is the Chief Marketing Officer of ILMERA Study Abroad and an independent SEO, AEO and GEO consultant based in Kushal Nagar, Kodagu, Karnataka. He runs his own practice at fawazbhseo.in and has worked in SEO since early 2025. His credentials include Ahrefs Academy and Semrush certifications and an Advanced Diploma in Digital Marketing from Adrex Media School."
APPROVED_BIOS = (ZAHEER, FAWAZ)
FAWAZ_SAME_AS = ['https://fawazbhseo.in/', 'https://www.linkedin.com/in/fawazbh']

# Phase 25 card-only exceptions. Never add these to APPROVED_BIOS: that tuple
# authorizes exact full-bio training-institute contexts, not shortened schema/LLMs.
SHORT_CARD_BIOS = {
    'Jabir KJ': 'Jabir KJ is the Founder of ILMERA Study Abroad. He is responsible for university research, admissions and application guidance.',
    'Zaheer KJ': "Zaheer KJ is the Chief Financial Officer of ILMERA Study Abroad and a digital marketer. He manages ILMERA's finance and paperwork.",
    'Fawaz BH': 'Fawaz BH is the Chief Marketing Officer of ILMERA Study Abroad and an independent SEO, AEO and GEO consultant based in Kodagu.'
}

def card_bio_allowed(text, route, in_team_card):
    return route in ('/', '/about') and in_team_card and text in SHORT_CARD_BIOS.values()

def validate_bio_contexts(text, route, published=True):
    """Short bios only in six actual card paragraphs; full data still mandatory."""
    import html,json,pathlib,re
    team_area=re.search(r'<section\b[^>]*id="team"[^>]*>.*?</section>',text,re.S)
    # Unit fixtures without a section use only their explicitly supplied card area.
    card_area=team_area[0] if team_area else text
    cards=re.findall(r'<article\b[^>]*class="(?:team-card|testi-card[^\"]*)"[^>]*>.*?</article>',card_area,re.S)
    expected_cards=3 if route in ('/','/about') else 0
    assert len(cards)==expected_cards,(route,'Team card count/context')
    names=[]
    for card in cards:
        bio=re.search(r'<p\b[^>]*class="(?:team-bio|testi-text)"[^>]*>(.*?)</p>',card,re.S)
        assert bio is not None,(route,'Missing card bio')
        value=html.unescape(bio[1]);assert card_bio_allowed(value,route,True),(route,'Unapproved short bio')
        name=next(n for n,b in SHORT_CARD_BIOS.items() if b==value);names.append(name)
        assert name in card,(route,'Bio/card identity mismatch')
    if expected_cards:assert set(names)==set(SHORT_CARD_BIOS),(route,'Duplicate/missing member')
    remaining=text
    for card in cards:remaining=remaining.replace(card,'',1)
    for bio in SHORT_CARD_BIOS.values():
        # A short text cannot replace a Person description, FAQ, prose or metadata.
        assert bio not in html.unescape(remaining),(route,'Card-only wording escaped its context')
    if published:
        team=json.loads((pathlib.Path(__file__).resolve().parents[1]/'data/team.json').read_text())['members']
        nodes=[]
        def walk(v):
            if isinstance(v,dict):
                nodes.append(v)
                for x in v.values():walk(x)
            elif isinstance(v,list):
                for x in v:walk(x)
        for g in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S):walk(json.loads(g))
        for member in team:
            people=[n for n in nodes if n.get('@type')=='Person' and n.get('name')==member['name']]
            assert people==[member],(route,'Full canonical Person description/properties required')
        if route=='/about':
            for member in team[1:]:
                assert member['description'] in html.unescape(re.sub(r'<script\b.*?</script>','',remaining,flags=re.S)),(route,'Full About bio/FAQ required')
    return True
