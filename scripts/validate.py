#!/usr/bin/env python3
"""Dependency-free release checks; vendor validators and OAuth smoke tests are separate."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return json.loads((ROOT / path).read_text())

def contained(base, value):
    path = (base / value).resolve()
    assert path.is_relative_to(base.resolve()) and path.exists(), value
    return path

codex = ROOT / 'plugins/processhub'
claude = ROOT / 'claude/processhub'
cm = read('plugins/processhub/.codex-plugin/plugin.json')
am = read('claude/processhub/.claude-plugin/plugin.json')
assert cm['name'] == am['name'] == 'processhub'
assert cm['version'] == am['version']
assert cm['version'].split('+')[0] == '0.1.0'
assert cm['author']['email'] == am['author']['email'] == 'hello@prgm.kz'
assert cm['interface']['privacyPolicyURL'] == 'https://processhub.kz/privacy'
assert cm['interface']['termsOfServiceURL'] == 'https://processhub.kz/terms'
assert len(cm['interface']['defaultPrompt']) <= 3
for prompt in cm['interface']['defaultPrompt']:
    assert len(prompt) <= 128
for root, manifest, client in [(codex, cm, 'processhub-codex'), (claude, am, 'processhub-claude-code')]:
    config = json.loads(contained(root, manifest['mcpServers']).read_text())
    assert set(config['mcpServers']) == {'processhub'}
    server = config['mcpServers']['processhub']
    assert set(server) == {'type', 'url', 'oauth'}
    assert server['type'] == 'http' and server['url'] == 'https://processhub.kz/mcp'
    assert server['oauth']['clientId'] == client
    assert set(server['oauth']) <= {'clientId', 'callbackPort', 'callbackUrl'}
    if root == codex:
        assert server['oauth']['callbackUrl'] == 'http://127.0.0.1/callback'
    else:
        assert server['oauth']['callbackPort'] == 39847
    assert contained(root, manifest['skills']).is_dir()
    assert not (root / 'hooks').exists() and not (root / 'scripts').exists()
for name in ['task-brief', 'implementation-plan', 'work-report', 'task-changes']:
    path = Path('skills') / name / 'SKILL.md'
    assert (codex / path).read_bytes() == (claude / path).read_bytes(), path
    text = (codex / path).read_text()
    assert text.startswith('---\nname: '+name+'\n') and 'description: ' in text
    assert 'untrusted data' in text and 'get_connection_context' in text
report = (codex / 'skills/work-report/SKILL.md').read_text()
for contract in ['PENDING_APPROVAL', 'SUCCEEDED', 'expectedRevision', 'idempotencyKey', 'approvalUrl', '6,000']:
    assert contract in report
for name in ['composerIcon', 'logo']:
    icon = contained(codex, cm['interface'][name])
    assert icon.read_bytes().startswith(b'\x89PNG\r\n\x1a\n')
market = read('.agents/plugins/marketplace.json')
entry = market['plugins'][0]
assert len(market['plugins']) == 1 and entry['name'] == cm['name']
assert entry['source'] == {'source':'local','path':'./plugins/processhub'}
assert entry['policy'] == {'installation':'AVAILABLE','authentication':'ON_INSTALL'}
assert entry['category'] == 'Productivity'
assert read('.claude-plugin/marketplace.json')['plugins'][0]['source'] == './claude/processhub'
cases = read('submission/test-cases.json')
assert len({c['id'] for c in cases}) == 12
assert sum(c['kind'] == 'positive' for c in cases) == 7
assert sum(c['kind'] == 'negative' for c in cases) == 5
allowed = {'.agents','.claude-plugin','.github','.git','.gitignore','plugins','claude','scripts','submission','README.md','SETUP.md','LICENSE'}
assert not {p.name for p in ROOT.iterdir()} - allowed
for path in ROOT.rglob('*'):
    if '.git' in path.parts or not path.is_file():
        continue
    assert not path.is_symlink(), path
    assert not path.name.startswith('.env') and path.suffix not in {'.pem','.key','.sqlite'}, path
print('PASS: both packages, MCP configuration, four mirrored skills, assets, marketplaces and twelve reviewer scenarios')
