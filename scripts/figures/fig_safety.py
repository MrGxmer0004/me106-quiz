from figlib import Fig


def signs():
    f = Fig('safety/signs', 760, 300, 'Safety sign shapes and colours',
            'Four safety signs drawn by shape and colour only: a red ring with a bar, a yellow triangle with an exclamation mark, a solid blue circle and a green rectangle with a cross',
            ask={'p': 'What does sign {L} indicate?', 'w': 'Which sign is used for a {P}?'})
    f.raw('<circle cx="110" cy="160" r="70" fill="#ffffff" stroke="#e03131" stroke-width="14"/><line x1="62" y1="112" x2="158" y2="208" stroke="#e03131" stroke-width="14"/>')
    f.raw('<polygon points="300,90 380,230 220,230" fill="#fcc419" stroke="#212529" stroke-width="6" stroke-linejoin="round"/>')
    f.raw('<text x="300" y="200" font-size="60" font-weight="700" text-anchor="middle" fill="#212529">!</text>')
    f.raw('<circle cx="490" cy="160" r="70" fill="#1971c2"/>')
    f.raw('<rect x="600" y="100" width="140" height="120" rx="8" fill="#2f9e44"/><rect x="655" y="125" width="30" height="70" fill="#ffffff"/><rect x="635" y="145" width="70" height="30" fill="#ffffff"/>')
    f.panel('A', 40, 60, 'Prohibition (do not)', 'Red ring with a diagonal bar: forbids an action', 'SAF-F024')
    f.panel('B', 230, 60, 'Warning (caution)', 'Yellow triangle with black border: warns of a hazard', 'SAF-F024')
    f.panel('C', 420, 60, 'Mandatory instruction (must do)', 'Solid blue circle: something you must do, e.g. wear goggles', 'SAF-F024')
    f.panel('D', 610, 60, 'Safe condition / first aid', 'Green rectangle: first aid, emergency exit, safe condition', 'SAF-F024')
    return f


FIGS = [signs]
