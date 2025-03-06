import sys

text = 'Arma: Reforger\n'

with open(sys.argv[1], encoding='utf-8') as f:
    for line in f:
        strip = line.strip()
        if strip.startswith('m_sDeptName'):
            text += '\n' + strip.replace('m_sDeptName "','').replace('#AR-Credits_', '')[:-1] + '\n'
        elif strip.startswith('m_sPersonName'):
            text += strip.replace('m_sPersonName "','')[:-1] + '\n'
            
with open(sys.argv[1] + '_moby_wip.txt', 'w', newline='', encoding='utf-8') as f:
    f.write(text)