"""Only two exact historical Zaheer substitutions, never a broad wording waiver."""
import ast,json,pathlib,subprocess
from team_bio_policy import ZAHEER
BASE='b8719a4bd5aa8c4631c2cd1675f15063cb8f372f'
ROOT=pathlib.Path(__file__).resolve().parents[2]
def original(file):return subprocess.check_output(['git','show',BASE+':'+file],cwd=ROOT)
OLD_FULL=json.loads(original('data/team.json'))['members'][2]['description']
OLD_CARD=next(ast.literal_eval(n.value)['Zaheer KJ'] for n in ast.parse(original('tools/team_bio_policy.py').decode()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='SHORT_CARD_BIOS' for t in n.targets))
PUBLIC_FILES={'index.php','about.php','data/team.json','llms.txt','llms-full.txt'}
def upgrade(text):
    for before in (OLD_FULL,OLD_CARD):
        text=text.replace(before,ZAHEER)
        text=text.replace(before.replace("'",r'\u0027'),ZAHEER.replace("'",r'\u0027'))
    return text
