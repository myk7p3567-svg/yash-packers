"""Generates simple isometric line-art SVGs for the Yash Packers concept site."""
import math, os

NAVY = "#0F2A4A"; TOP = "#FFFFFF"; LEFT = "#E6ECF4"; RIGHT = "#CBD5E2"; AMBER = "#E8900C"
C30, S30 = math.cos(math.radians(30)), math.sin(math.radians(30))

def iso(x, y, z, ox=0, oy=0, s=1):
    return (ox + (x - y) * C30 * s, oy + (x + y) * S30 * s - z * s)

def pts(p):
    return " ".join(f"{a:.1f},{b:.1f}" for a, b in p)

def box(x, y, z, w, d, h, ox, oy, s=1, stroke=NAVY, top=TOP, left=LEFT, right=RIGHT, sw=1.6):
    """Draw a cuboid with origin corner (x,y,z), size w (x), d (y), h (z)."""
    P = lambda a, b, c: iso(a, b, c, ox, oy, s)
    topf = [P(x, y, z + h), P(x + w, y, z + h), P(x + w, y + d, z + h), P(x, y + d, z + h)]
    leftf = [P(x, y + d, z), P(x + w, y + d, z), P(x + w, y + d, z + h), P(x, y + d, z + h)]
    rightf = [P(x + w, y, z), P(x + w, y + d, z), P(x + w, y + d, z + h), P(x + w, y, z + h)]
    j = f'stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"'
    return (f'<polygon points="{pts(leftf)}" fill="{left}" {j}/>'
            f'<polygon points="{pts(rightf)}" fill="{right}" {j}/>'
            f'<polygon points="{pts(topf)}" fill="{top}" {j}/>')

def cavity(x, y, z, w, d, depth, ox, oy, s=1):
    """A rectangular recess cut into a top face at height z."""
    P = lambda a, b, c: iso(a, b, c, ox, oy, s)
    rim = [P(x, y, z), P(x + w, y, z), P(x + w, y + d, z), P(x, y + d, z)]
    floor = [P(x, y, z - depth), P(x + w, y, z - depth), P(x + w, y + d, z - depth), P(x, y + d, z - depth)]
    back_l = [P(x, y, z), P(x + w, y, z), P(x + w, y, z - depth), P(x, y, z - depth)]
    back_r = [P(x, y, z), P(x, y + d, z), P(x, y + d, z - depth), P(x, y, z - depth)]
    j = f'stroke="{NAVY}" stroke-width="1.4" stroke-linejoin="round"'
    return (f'<polygon points="{pts(back_l)}" fill="{RIGHT}" {j}/>'
            f'<polygon points="{pts(back_r)}" fill="{LEFT}" {j}/>'
            f'<polygon points="{pts(floor)}" fill="#DCE4EE" {j}/>'
            f'<polygon points="{pts(rim)}" fill="none" {j}/>')

def svg(body, w, h, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">'
            f'<title>{label}</title>{body}</svg>')

def dim_line(p1, p2, text, offset=(0, 0)):
    (x1, y1), (x2, y2) = p1, p2
    mx, my = (x1 + x2) / 2 + offset[0], (y1 + y2) / 2 + offset[1]
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{AMBER}" stroke-width="1.4"/>'
            f'<circle cx="{x1:.1f}" cy="{y1:.1f}" r="2.4" fill="{AMBER}"/><circle cx="{x2:.1f}" cy="{y2:.1f}" r="2.4" fill="{AMBER}"/>'
            f'<text x="{mx:.1f}" y="{my:.1f}" font-family="IBM Plex Sans, Arial, sans-serif" font-size="12" fill="{AMBER}" text-anchor="middle">{text}</text>')

def make_all(out):
    os.makedirs(out, exist_ok=True)
    S = 1.0
    # 1. Custom EPS packaging box with two cavities
    b = box(0, 0, 0, 120, 90, 46, 150, 60, S) + cavity(14, 14, 46, 58, 62, 22, 150, 60, S) + cavity(84, 14, 46, 22, 62, 22, 150, 60, S)
    open(f"{out}/eps-packaging.svg", "w").write(svg(b, 300, 190, "Custom EPS thermocol packaging box with moulded cavities"))
    # 2. Sheets stack
    b = box(0, 0, 0, 150, 100, 10, 150, 58, S) + box(8, 8, 10, 150, 100, 10, 150, 58, S) + box(16, 16, 20, 150, 100, 10, 150, 58, S)
    open(f"{out}/eps-sheets.svg", "w").write(svg(b, 300, 190, "Stack of EPS thermocol sheets"))
    # 3. Insulated ice box with lid
    b = box(0, 0, 0, 110, 85, 48, 150, 58, S) + box(-5, -5, 48, 120, 95, 14, 150, 58, S)
    open(f"{out}/eps-icebox.svg", "w").write(svg(b, 300, 190, "EPS insulated ice box with lid"))
    # 4. EPE foam insert with round cavities
    b = box(0, 0, 0, 125, 95, 28, 150, 62, S, top="#F6F2EA", left="#EAE2D2", right="#D9CFBA")
    P = lambda a, c, z: iso(a, c, z, 150, 62, S)
    for (cx, cy) in [(30, 28), (62, 28), (94, 28), (30, 66), (62, 66), (94, 66)]:
        x, y = P(cx, cy, 28)
        b += f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="11" ry="6.3" fill="#D9CFBA" stroke="{NAVY}" stroke-width="1.4"/>'
    open(f"{out}/epe-foam.svg", "w").write(svg(b, 300, 190, "EPE foam insert with cushioned cavities"))
    # 5. Pipe section + pillar (other products)
    P = lambda a, c, z: iso(a, c, z, 150, 70, S)
    cx1, cy1 = P(40, 40, 0); cx2, cy2 = P(40, 40, 70)
    b = (f'<path d="M{cx1-34:.1f},{cy1:.1f} a34,19.6 0 1,0 68,0" fill="{RIGHT}" stroke="{NAVY}" stroke-width="1.6"/>'
         f'<rect x="{cx1-34:.1f}" y="{cy2:.1f}" width="68" height="{cy1-cy2:.1f}" fill="{LEFT}" stroke="none"/>'
         f'<line x1="{cx1-34:.1f}" y1="{cy2:.1f}" x2="{cx1-34:.1f}" y2="{cy1:.1f}" stroke="{NAVY}" stroke-width="1.6"/>'
         f'<line x1="{cx1+34:.1f}" y1="{cy2:.1f}" x2="{cx1+34:.1f}" y2="{cy1:.1f}" stroke="{NAVY}" stroke-width="1.6"/>'
         f'<ellipse cx="{cx2:.1f}" cy="{cy2:.1f}" rx="34" ry="19.6" fill="{TOP}" stroke="{NAVY}" stroke-width="1.6"/>'
         f'<ellipse cx="{cx2:.1f}" cy="{cy2:.1f}" rx="19" ry="11" fill="{RIGHT}" stroke="{NAVY}" stroke-width="1.4"/>')
    b += box(110, 20, 0, 34, 34, 95, 150, 70, S)
    open(f"{out}/other-products.svg", "w").write(svg(b, 300, 190, "EPS pipe section and thermocol pillar"))
    # Hero: large EPS insert with dimension lines
    ox, oy, s = 250, 112, 1.6
    body = box(0, 0, 0, 150, 110, 44, ox, oy, s)
    body += cavity(16, 16, 44, 70, 78, 24, ox, oy, s) + cavity(96, 16, 44, 38, 36, 20, ox, oy, s) + cavity(96, 60, 44, 38, 34, 20, ox, oy, s)
    P = lambda a, c, z: iso(a, c, z, ox, oy, s)
    body += dim_line(P(0, 118, 0), P(150, 118, 0), "Length (custom)", (0, 30))
    body += dim_line(P(158, 0, 0), P(158, 110, 0), "Width", (46, 6))
    body += dim_line(P(-8, 110, 0), P(-8, 110, 44), "Height", (-42, 0))
    lx, ly = P(16, 16, 44)
    body += (f'<line x1="{lx+30:.1f}" y1="{ly+12:.1f}" x2="{lx+30:.1f}" y2="30" stroke="{AMBER}" stroke-width="1.2"/>'
             f'<circle cx="{lx+30:.1f}" cy="{ly+12:.1f}" r="2.4" fill="{AMBER}"/>'
             f'<text x="{lx+30:.1f}" y="20" font-family="IBM Plex Sans, Arial, sans-serif" font-size="12" fill="{AMBER}" text-anchor="middle">Cavity moulded to the product shape</text>')
    open(f"{out}/hero-insert.svg", "w").write(svg(body, 520, 372, "Engineering drawing of a custom EPS packaging insert with dimension lines"))

if __name__ == "__main__":
    make_all(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "img"))
    print("ok")
