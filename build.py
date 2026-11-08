import os, json, html

OUT = os.path.dirname(os.path.abspath(__file__))  # pages are written next to this script
DOMAIN = "https://www.yashpackersgn.in"
PHONE_DISPLAY = "+91 98XXX XXXXX"           # TODO replace with the one verified number
PHONE_TEL = "+919800000000"                  # TODO replace (digits only after +)
WA_NUMBER = "919800000000"                   # TODO replace: country code + number, no spaces
EMAIL = "sales@yashpackersgn.in"             # suggested address, create it or replace
ADDRESS = "Plot No. J-5, Site-5, Kasna Industrial Area (UPSIDA), Greater Noida 201308, Gautam Buddha Nagar, Uttar Pradesh"
GST = "09IGLPS4346Q1Z6"

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;800&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">'
FAVICON = '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 64 64%22%3E%3Crect width=%2264%22 height=%2264%22 rx=%228%22 fill=%22%230F2A4A%22/%3E%3Ctext x=%2232%22 y=%2243%22 font-family=%22Arial%22 font-weight=%22800%22 font-size=%2230%22 fill=%22%23fff%22 text-anchor=%22middle%22%3EYP%3C/text%3E%3C/svg%3E">'

NAV = [("index.html", "Home"), ("products.html", "Products"), ("industries.html", "Industries"), ("about.html", "Manufacturing"), ("resources.html", "Resources"), ("contact.html", "Contact")]

WA_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.5 3.5A11.8 11.8 0 0 0 12.1 0C5.6 0 .3 5.3.3 11.8c0 2.1.5 4.1 1.6 5.9L0 24l6.4-1.7a11.8 11.8 0 0 0 5.7 1.4c6.5 0 11.8-5.3 11.8-11.8 0-3.2-1.2-6.1-3.4-8.4zM12.1 21.7c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.8 1 1-3.7-.2-.4a9.8 9.8 0 0 1-1.5-5.2c0-5.4 4.4-9.8 9.8-9.8 2.6 0 5.1 1 6.9 2.9a9.7 9.7 0 0 1 2.9 6.9c0 5.4-4.4 9.9-9.7 9.9zm5.4-7.3c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1l-.9 1.1c-.2.2-.3.2-.6.1-.3-.1-1.2-.5-2.4-1.5-.9-.8-1.5-1.8-1.6-2.1-.2-.3 0-.5.1-.6l.4-.5.3-.5c.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4z"/></svg>'

def head(title, desc, path, jsonld=None, og=True):
    canonical = f"{DOMAIN}/{'' if path == 'index.html' else path}"
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in (jsonld or []))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
{FONTS}
{FAVICON}
<link rel="stylesheet" href="assets/styles.css">
{ld}
</head>
<body>
<div id="preview-banner">Concept redesign prepared for Yash Packers. Photographs, phone number and technical figures are placeholders to be confirmed before launch.</div>
<div class="topline"><div class="wrap"><span>Kasna Industrial Area, Greater Noida (UPSIDA) · GST {GST}</span><span><a href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a> &nbsp;·&nbsp; <a href="mailto:{EMAIL}">{EMAIL}</a></span></div></div>
"""

def header(active):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{l}</a>' for h, l in NAV)
    return f"""<header class="site"><div class="wrap">
<a class="brand" href="index.html"><span class="mark">YP</span><span><span class="name">Yash Packers</span><span class="tag">EPS thermocol &amp; EPE foam packaging</span></span></a>
<button class="menu-btn" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mainnav">☰</button>
<nav class="main" id="mainnav" aria-label="Main">{links}<a class="btn primary sm" href="contact.html#rfq">Request a quote</a></nav>
</div></header>
<main>
"""

def footer():
    return f"""</main>
<a class="wa-float" href="https://wa.me/{WA_NUMBER}?text=Hello%20Yash%20Packers%2C%20I%20need%20a%20quotation%20for%20packaging." target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{WA_ICON}<span>WhatsApp</span></a>
<footer class="site"><div class="wrap">
<div class="cols">
<div><h4>Yash Packers</h4><p>Manufacturer of customised EPS thermocol packaging, EPE foam packaging and insulation products. Established 2020 in Greater Noida, serving manufacturers across Delhi NCR and India.</p><p class="small">{ADDRESS}</p><p class="small">GST {GST}</p></div>
<div><h4>Products</h4><ul><li><a href="eps-thermocol-packaging.html">EPS thermocol packaging</a></li><li><a href="eps-thermocol-sheets.html">EPS thermocol sheets</a></li><li><a href="eps-insulated-boxes.html">EPS insulated boxes</a></li><li><a href="epe-foam-packaging.html">EPE foam packaging</a></li><li><a href="other-eps-products.html">Pipe sections, pillars and more</a></li></ul></div>
<div><h4>Industries</h4><ul><li><a href="industry-electronics-packaging.html">Electronics and appliances</a></li><li><a href="industry-motor-packaging.html">Motors and electrical equipment</a></li><li><a href="industries.html#automotive">Automotive components</a></li><li><a href="industries.html#pharma">Pharma and cold chain</a></li><li><a href="industries.html#consumer">Glassware and consumer goods</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="about.html">Manufacturing and quality</a></li><li><a href="resources.html">Packaging guides</a></li><li><a href="contact.html">Contact and quotation</a></li><li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
</div>
<div class="legal"><span>© Yash Packers. All rights reserved.</span><span><a href="sitemap.xml">Sitemap</a></span></div>
</div></footer>
<script src="assets/main.js"></script>
</body>
</html>
"""

def crumbs(items):
    lis = "".join(f'<li><a href="{h}">{t}</a></li>' if h else f'<li aria-current="page">{t}</li>' for t, h in items)
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": t, "item": f"{DOMAIN}/{h}" if h else None} for i, (t, h) in enumerate(items)]}
    return f'<nav class="crumbs wrap" aria-label="Breadcrumb"><ol>{lis}</ol></nav>', ld

def rfq_form(compact=False):
    return f"""<form class="rfq" id="rfq" data-wa="{WA_NUMBER}" data-email="{EMAIL}">
<h3>Request a packaging quotation</h3>
<p class="small muted">Tell us what you need to pack. We reply with a design proposal and price, usually within one working day.</p>
<div class="grid">
<div><label for="f-product">What do you need?</label><select id="f-product" name="product" required><option value="">Select a product type</option><option>Custom EPS thermocol packaging box or insert</option><option>EPS thermocol sheets</option><option>EPS insulated / ice box</option><option>EPE foam box or insert</option><option>EPS pipe section, pillar or other</option><option>Not sure, need advice</option></select></div>
<div><label for="f-qty">Quantity required</label><input id="f-qty" name="quantity" placeholder="e.g. 5,000 pieces per month" required></div>
<div><label for="f-dims">Product or box dimensions</label><input id="f-dims" name="dimensions" placeholder="Length × Width × Height (mm or inches)"></div>
<div><label for="f-industry">Your industry</label><input id="f-industry" name="industry" placeholder="e.g. electrical motors, electronics, pharma"></div>
<div class="full"><label for="f-notes">What are you packing, and any special requirements?</label><textarea id="f-notes" name="notes" placeholder="Product weight, fragility, transit conditions, temperature control, branding, delivery location..."></textarea></div>
<div><label for="f-name">Your name</label><input id="f-name" name="name" required></div>
<div><label for="f-company">Company</label><input id="f-company" name="company" required></div>
<div><label for="f-phone">Phone / WhatsApp</label><input id="f-phone" name="phone" type="tel" required></div>
<div><label for="f-email">Email</label><input id="f-email" name="email" type="email"></div>
</div>
<div class="actions"><button class="btn primary" type="submit">Send on WhatsApp</button><button class="btn" type="button" id="rfq-email">Send by email instead</button></div>
<p class="note">Have a drawing or a photo of the product? Attach it in the WhatsApp chat or email after sending this form. No file is uploaded through this website.</p>
</form>"""

# ---------------- data ----------------
CATS = [
  dict(slug="eps-thermocol-packaging", name="EPS thermocol packaging", img="eps-packaging.svg",
       short="Custom-moulded boxes, inserts and buffers that fit the product exactly.",
       title="EPS Thermocol Packaging Boxes and Inserts | Custom Moulded | Yash Packers",
       desc="Custom EPS thermocol packaging boxes, inserts and buffers moulded to your product's shape. For motors, electronics, glassware and industrial components. Made in Greater Noida.",
       intro="Expanded polystyrene (EPS, commonly called thermocol) is light, rigid and absorbs impact, which makes it the standard material for protecting industrial and consumer products in transit. Yash Packers moulds EPS packaging to the exact shape of your product, so it cannot move inside the carton and arrives in the condition it left your line.",
       products=[("Custom EPS packaging boxes", "A two-part or multi-part box moulded around your product's outline. Replaces loose fill and corrugated inserts with a single fitted piece."),
                 ("Industrial component packaging", "Inserts for pumps, valves, compressors, gearboxes and machined parts. Cavities located to carry weight on the strongest faces of the part."),
                 ("Heavy motor packaging boxes", "Base and top sets for electric motors and alternators, with recesses for shafts and terminal boxes and higher-density EPS for the load."),
                 ("Electronics and electrical component packaging", "Precision cavities for control panels, meters, inverters, set-top boxes and printed circuit assemblies, with clearance for cables and connectors."),
                 ("Glassware and mug packaging", "Nested cavities for mugs, bottles, lamp shades and ceramic items so pieces do not touch each other in the carton."),
                 ("Vaccine and cold-chain boxes", "Thick-walled insulated boxes with close-fitting lids for vaccines and temperature-sensitive goods. Can be supplied with gel-pack recesses."),
                 ("Carom board and sports goods packaging", "Edge and corner protection for boards, frames and flat items that are easily chipped in transit."),
                 ("Thermocol buffers and corner pads", "Standalone corner protectors and edge buffers for appliances, furniture and sheet goods packed in cartons or on pallets.")],
       specs=[("Material", "Expanded polystyrene (EPS), virgin grade"),
              ("Density", "Selected to suit the product weight and drop height; typical industrial packaging uses low to medium density. Exact range to be confirmed with Yash Packers."),
              ("Dimensions", "Fully customisable. Standard boxes also available."),
              ("Colour", "White"),
              ("Customisation", "Custom moulds developed from your drawing, sample or product"),
              ("Minimum order quantity", "Depends on the mould; confirm at quotation"),
              ("Lead time", "Sampling and production times quoted per job")],
       faqs=[("Can you make packaging for a product you have never seen?", "Yes. Send a drawing, a 3D file or the physical product. The engineering team designs the cavity, produces a sample for fit approval, and only then starts the production run."),
             ("What is the difference between EPS and thermocol?", "None. Thermocol is the common Indian trade name for expanded polystyrene (EPS). Both words refer to the same material."),
             ("How do I choose density?", "Heavier or more fragile products need a higher density so the foam does not compress permanently on impact. Tell us the product weight and how it will be shipped and we will recommend a grade."),
             ("Do you supply the outer carton as well?", "We supply the EPS packaging. We are happy to work with your carton supplier so the insert and carton are sized together, or to recommend one.")]),
  dict(slug="eps-thermocol-sheets", name="EPS thermocol sheets", img="eps-sheets.svg",
       short="Insulation and packaging sheets in standard and custom thicknesses.",
       title="EPS Thermocol Sheets, 30mm and 50mm Insulation Sheets | Yash Packers",
       desc="EPS thermocol sheets for insulation and packaging in 30mm, 50mm and custom thicknesses, cut to size. Manufacturer in Greater Noida supplying Delhi NCR.",
       intro="EPS sheets are used wherever a flat, light and insulating layer is needed: between pallet layers, as cold-room and roof insulation, behind cladding, or cut into dividers and spacers. Yash Packers cuts sheets to your size and thickness from moulded blocks, so you are not restricted to catalogue dimensions.",
       products=[("30 mm thermocol sheets", "A common thickness for interleaving packed goods and light insulation. Supplied in standard sheet sizes or cut to your dimensions."),
                 ("50 mm thermocol sheets", "For roof and wall insulation, cold storage and heavier packaging duty."),
                 ("Insulation sheets", "Selected density for thermal performance in cold rooms, ducting, prefab panels and roofing. Thickness and density to suit the application."),
                 ("Packaging sheets and dividers", "Interleaving sheets, pallet layer pads and dividers for glass, tiles, appliances and sheet metal."),
                 ("Custom cut sheets", "Any thickness within block limits, slotted, grooved or shaped on request.")],
       specs=[("Material", "Expanded polystyrene (EPS)"),
              ("Thickness", "30 mm and 50 mm standard; other thicknesses on request"),
              ("Sheet size", "Standard sizes and custom cuts; confirm available block dimensions at quotation"),
              ("Density", "Multiple grades available; recommend based on load and insulation duty"),
              ("Colour", "White"),
              ("Minimum order quantity", "Confirm at quotation")],
       faqs=[("Which thickness do I need for insulation?", "It depends on the temperature difference you need to hold and the space available. 50 mm is a common starting point for cold rooms and roofs; tell us the application and we will recommend."),
             ("Can sheets be cut to shape?", "Yes. Slots, grooves, holes and irregular outlines can be cut for ducting, panel fitting and packaging layouts."),
             ("Do you deliver in Delhi NCR?", "Yes. We are in Kasna Industrial Area, Greater Noida, and supply Noida, Ghaziabad, Delhi, Faridabad and Gurugram regularly, as well as other states by transport.")]),
  dict(slug="eps-insulated-boxes", name="EPS insulated boxes", img="eps-icebox.svg",
       short="Ice boxes, fish boxes and cold-chain boxes with tight-fitting lids.",
       title="EPS Thermocol Ice Boxes and Insulated Cold Chain Boxes | Yash Packers",
       desc="EPS thermocol ice boxes, fish boxes and insulated cold-chain boxes with lids, from 10 litres upward. Manufacturer in Greater Noida, Delhi NCR.",
       intro="A closed EPS box holds temperature for hours because the material is almost entirely trapped air. Yash Packers makes insulated boxes for food, seafood, dairy, pharma and anything else that needs to stay cold (or hot) between dispatch and delivery.",
       products=[("10 litre ice boxes", "A compact box with lid for samples, small seafood consignments, ice cream and chilled deliveries."),
                 ("Fish and seafood boxes", "Larger boxes with drainage considerations and stacking lids for fish markets, aquaculture and exporters."),
                 ("Temperature-controlled shipping boxes", "Thick-walled boxes sized to your payload and transit time, with recesses for ice packs or gel packs."),
                 ("Vaccine and pharma carriers", "Insulated boxes for vaccines, reagents and samples, with an inner carton or secondary container where required.")],
       specs=[("Material", "Expanded polystyrene (EPS)"),
              ("Capacity", "10 litres and larger; custom volumes available"),
              ("Wall thickness", "Specified to the required holding time; confirm at quotation"),
              ("Lid", "Fitted lid; strap or tape closure"),
              ("Colour", "White"),
              ("Minimum order quantity", "Confirm at quotation")],
       faqs=[("How long will a box keep contents cold?", "It depends on wall thickness, how much ice or gel pack is used, ambient temperature and how often the box is opened. We can advise a wall thickness and coolant quantity for your route."),
             ("Are the boxes food safe?", "EPS is widely used for food and seafood packaging. Tell us the product and we will confirm the grade and any secondary liner you may need."),
             ("Can I print or brand the box?", "Labels and stickers are the usual approach. Ask about options when you request a quote.")]),
  dict(slug="epe-foam-packaging", name="EPE foam packaging", img="epe-foam.svg",
       short="Soft, flexible foam boxes, inserts and fitments for scratch-sensitive goods.",
       title="EPE Foam Packaging Boxes, Inserts and Fitments | Manufacturer | Yash Packers",
       desc="EPE foam packaging boxes, inserts, fitments and sheets for electronics, glass and finished goods. Flexible, non-abrasive cushioning made in Greater Noida.",
       intro="Expanded polyethylene (EPE) is a closed-cell foam that is softer and more flexible than EPS. It does not crumble, it is non-abrasive, and it recovers after compression, which makes it the right choice for polished surfaces, repeat-use packaging and products with delicate finishes.",
       products=[("EPE foam boxes", "Die-cut and glued boxes that cushion the whole product, often used for electronics, instruments and gift packaging."),
                 ("EPE foam inserts", "Layered or routed inserts with cavities shaped to the product. Can be laminated with cloth or film for a premium finish."),
                 ("Custom EPE fitments", "Corner pads, edge channels, end caps and spacers made to your drawing."),
                 ("EPE sheets and rolls", "Sheet foam in a range of thicknesses for wrapping, interleaving and surface protection.")],
       specs=[("Material", "Expanded polyethylene (EPE), closed cell"),
              ("Thickness", "Sheet and layered thicknesses to suit; confirm at quotation"),
              ("Colour", "White standard; other colours on request"),
              ("Construction", "Die-cut, routed, laminated or glued"),
              ("Customisation", "From drawing or physical sample"),
              ("Minimum order quantity", "Confirm at quotation")],
       faqs=[("EPS or EPE: which should I use?", "EPS is rigid, cheaper and better for heavy loads and insulation. EPE is soft, flexible and kinder to finished surfaces. Many packs use both: an EPS outer for structure and EPE where it touches the product. See the guide in Resources."),
             ("Is EPE reusable?", "Yes. EPE recovers its shape after compression, so it suits returnable trays and packaging that is opened and closed many times."),
             ("Can the foam be laminated or coloured?", "Yes, within the options available at the time of order. Ask when requesting a quote.")]),
  dict(slug="other-eps-products", name="Pipe sections, pillars and other EPS products", img="other-products.svg",
       short="Pipe insulation sections, decorative pillars, beans and round forms.",
       title="EPS Pipe Sections, Thermocol Pillars, Beans and Round Thermocol | Yash Packers",
       desc="EPS pipe insulation sections, thermocol pillars, thermocol beans and round thermocol forms manufactured in Greater Noida.",
       intro="Beyond packaging, EPS is used for pipe insulation, event and display construction, void forming and loose-fill cushioning. These products are made in the same facility to the same material standards.",
       products=[("EPS pipe sections", "Half-round insulation sections for chilled water, refrigeration and HVAC pipework, cut to pipe diameter and length."),
                 ("Thermocol pillars", "Lightweight pillars and columns for exhibitions, events, stage sets and décor, in standard and custom profiles."),
                 ("Thermocol beans", "Loose-fill EPS beads for void filling, bean bags and cushioning in mixed cartons."),
                 ("White round thermocol", "Discs, rings and cylinders for craft, display and industrial spacers."),
                 ("Thermocol box and buffer sets", "Protective sets for appliances and furniture where full moulded packaging is not required.")],
       specs=[("Material", "Expanded polystyrene (EPS)"),
              ("Dimensions", "Pipe sections to pipe OD; pillars and rounds to drawing"),
              ("Density", "Selected per application"),
              ("Colour", "White"),
              ("Minimum order quantity", "Confirm at quotation")],
       faqs=[("Can pipe sections be supplied with cladding?", "We supply the EPS section. Cladding or jacketing is applied by the insulation contractor; we can match standard cladding dimensions."),
             ("Do you make one-off decorative pieces?", "Yes, for events and displays. Lead time depends on complexity.")]),
]

INDUSTRIES = [
  ("automotive", "Automotive components", "Fitted EPS and EPE packaging for castings, lamps, mirrors, bumpers, instrument clusters and aftermarket parts moving between tier suppliers and plants.", "industries.html#automotive"),
  ("electronics", "Electronics and appliances", "Precision cavities for set-top boxes, inverters, meters, panels, printers and small appliances, with space for cables and accessories.", "industry-electronics-packaging.html"),
  ("motors", "Motors and electrical equipment", "Heavy-duty base and top sets for electric motors, pumps, alternators and switchgear, including shaft and terminal recesses.", "industry-motor-packaging.html"),
  ("pharma", "Pharma and cold chain", "Insulated vaccine boxes, sample carriers and temperature-controlled shippers for pharmaceutical and diagnostic distribution.", "industries.html#pharma"),
  ("consumer", "Glassware, ceramics and consumer goods", "Nested cavities for mugs, bottles, lamps, cookware and gift items so pieces never touch each other in transit.", "industries.html#consumer"),
  ("food", "Food and seafood", "Ice boxes and fish boxes for seafood, dairy, meat, ice cream and chilled delivery.", "industries.html#food"),
  ("construction", "Construction and HVAC", "Insulation sheets, pipe sections and void formers for cold rooms, roofing, prefab panels and chilled-water lines.", "industries.html#construction"),
]

# ---------------- pages ----------------
def page_home():
    jsonld = [{
        "@context": "https://schema.org", "@type": "LocalBusiness", "additionalType": "https://schema.org/Manufacturer",
        "name": "Yash Packers", "url": DOMAIN + "/", "telephone": PHONE_TEL, "email": EMAIL, "foundingDate": "2020",
        "description": "Manufacturer of customised EPS thermocol packaging, EPE foam packaging and insulation products in Greater Noida, India.",
        "address": {"@type": "PostalAddress", "streetAddress": "Plot No. J-5, Site-5, Kasna Industrial Area (UPSIDA)", "addressLocality": "Greater Noida", "addressRegion": "Uttar Pradesh", "postalCode": "201308", "addressCountry": "IN"},
        "areaServed": ["Greater Noida", "Noida", "Ghaziabad", "Delhi", "Faridabad", "Gurugram", "India"],
        "vatID": GST
    }]
    tiles = "".join(f'<a class="tile" href="{c["slug"]}.html"><div class="pic"><img src="assets/img/{c["img"]}" alt="{html.escape(c["name"])} illustration" loading="lazy" width="300" height="190"></div><h3>{c["name"]}</h3><p>{c["short"]}</p><span class="more">See products and specifications</span></a>' for c in CATS)
    inds = "".join(f'<a href="{h}" id="home-{k}"><h3>{n}</h3><p>{d}</p></a>' for k, n, d, h in INDUSTRIES)
    body = f"""
<section class="hero"><div class="wrap">
<div>
<h1>Custom EPS thermocol and EPE foam packaging, manufactured in Greater Noida</h1>
<p>Yash Packers designs and moulds protective packaging around your product: boxes, inserts, buffers, insulated boxes and sheets for manufacturers across Delhi NCR and India.</p>
<div class="cta"><a class="btn primary" href="contact.html#rfq">Request a quote</a><a class="btn light" href="products.html">Explore products</a></div>
<div class="facts"><div><strong>Since 2020</strong>Manufacturing in Kasna Industrial Area</div><div><strong>EPS and EPE</strong>Both materials under one roof</div><div><strong>Custom moulds</strong>Designed from your drawing or sample</div></div>
</div>
<figure class="art"><img src="assets/img/hero-insert.svg" alt="Engineering drawing of a custom EPS packaging insert with dimension lines" width="520" height="372"><figcaption>Every insert starts as a drawing. Send yours, or send the product and we draw it.</figcaption></figure>
</div></section>

<section class="block"><div class="wrap">
<div class="sec-head"><h2>What we make</h2><p>Five product families, all manufactured at our Greater Noida facility. Everything can be made to your dimensions.</p></div>
<div class="tiles">{tiles}</div>
</div></section>

<section class="block field"><div class="wrap">
<div class="split">
<div><div class="sec-head"><h2>How a custom pack is made</h2><p>Most enquiries are for a product that has never been packed in EPS before. This is the route from enquiry to production.</p></div>
<a class="btn" href="about.html">See manufacturing capabilities</a></div>
<ol class="process">
<li><div><h4>Share the product</h4><p>A drawing, 3D file, photos with dimensions, or the physical item couriered to us.</p></div></li>
<li><div><h4>Design the cavity</h4><p>We decide wall thickness, density and split lines so the pack protects the product and fits your carton.</p></div></li>
<li><div><h4>Make the mould</h4><p>A production mould is manufactured for the design. Mould cost is quoted up front and is a one-time charge.</p></div></li>
<li><div><h4>Approve a sample</h4><p>You test the fit and, if needed, a drop test. Changes are made before any volume is produced.</p></div></li>
<li><div><h4>Produce and deliver</h4><p>Production runs to your schedule, with delivery across Delhi NCR and by transport across India.</p></div></li>
</ol>
</div>
</div></section>

<section class="block"><div class="wrap">
<div class="sec-head"><h2>Industries we pack for</h2><p>The same materials, engineered differently for each product and transit route.</p></div>
<div class="industries">{inds}</div>
</div></section>

<section class="block field"><div class="wrap">
<div class="sec-head"><h2>Why manufacturers work with Yash Packers</h2></div>
<div class="reasons">
<div><h3>Packaging designed, not just supplied</h3><p>We engineer the cavity, density and split lines for your product rather than selling you a standard box that nearly fits.</p></div>
<div><h3>EPS and EPE in one place</h3><p>Rigid thermocol for structure and insulation, soft EPE where it touches the finished surface, from a single supplier.</p></div>
<div><h3>Sample before volume</h3><p>Every new design is approved on a physical sample so the production run is right the first time.</p></div>
<div><h3>Delhi NCR delivery</h3><p>Based in Kasna Industrial Area, Greater Noida, within easy reach of Noida, Ghaziabad, Delhi, Faridabad and Gurugram plants.</p></div>
</div>
</div></section>

<section class="block navy" id="quote"><div class="wrap">
<div class="split">
<div class="contact-side"><h2>Get a quotation</h2><p>Send the product details and we come back with a packaging proposal and price. If you are not sure what you need, say so and we will advise.</p>
<p><strong>Phone / WhatsApp</strong><a href="tel:{PHONE_TEL}" style="color:#fff">{PHONE_DISPLAY}</a></p>
<p><strong>Email</strong><a href="mailto:{EMAIL}" style="color:#fff">{EMAIL}</a></p>
<p><strong>Factory</strong>{ADDRESS}</p></div>
{rfq_form()}
</div>
</div></section>
"""
    return head("Yash Packers | EPS Thermocol & EPE Foam Packaging Manufacturer, Greater Noida",
                "Yash Packers manufactures customised EPS thermocol packaging boxes, EPE foam packaging, insulation sheets and insulated boxes in Greater Noida, India. Request a quotation.",
                "index.html", jsonld) + header("index.html") + body + footer()

def page_products():
    crumb_html, crumb_ld = crumbs([("Home", "index.html"), ("Products", None)])
    tiles = "".join(f'<a class="tile" href="{c["slug"]}.html"><div class="pic"><img src="assets/img/{c["img"]}" alt="{html.escape(c["name"])} illustration" loading="lazy" width="300" height="190"></div><h3>{c["name"]}</h3><p>{c["short"]}</p><span class="more">See products and specifications</span></a>' for c in CATS)
    body = f"""{crumb_html}
<section class="page-head wrap"><h1>Products</h1><p class="lede">Every product below is manufactured at our Greater Noida facility and can be made to your dimensions. Open a category for the product list, specifications and common questions.</p></section>
<section class="block" style="padding-top:20px"><div class="wrap"><div class="tiles">{tiles}</div></div></section>
<section class="block field"><div class="wrap"><div class="split"><div><h2>Not sure which material you need?</h2><p>EPS is rigid, insulating and economical. EPE is soft, flexible and protects finished surfaces. The two are often combined. Read the short guide or ask us.</p><div class="cta" style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn" href="eps-vs-epe-foam-packaging.html">EPS vs EPE guide</a><a class="btn primary" href="contact.html#rfq">Ask for a recommendation</a></div></div></div></div></section>
"""
    return head("Products | EPS Thermocol Packaging, Sheets, Insulated Boxes, EPE Foam | Yash Packers",
                "Browse Yash Packers' product range: custom EPS thermocol packaging, thermocol sheets, insulated ice boxes, EPE foam packaging and EPS pipe sections. Manufactured in Greater Noida.",
                "products.html", [crumb_ld]) + header("products.html") + body + footer()

def page_category(c):
    crumb_html, crumb_ld = crumbs([("Home", "index.html"), ("Products", "products.html"), (c["name"], None)])
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faqs"]]}
    plist = "".join(f'<article><div class="photo">Product photograph<br>(to be supplied)</div><h3>{n}</h3><p>{d}</p><a class="btn sm" href="contact.html#rfq">Request a quote</a></article>' for n, d in c["products"])
    spec = "".join(f'<tr><th scope="row">{k}</th><td>{v}</td></tr>' for k, v in c["specs"])
    faqs = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in c["faqs"])
    others = "".join(f'<li><a href="{o["slug"]}.html">{o["name"]}</a></li>' for o in CATS if o["slug"] != c["slug"])
    body = f"""{crumb_html}
<section class="page-head wrap"><h1>{c["name"]}</h1><p class="lede">{c["intro"]}</p><div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:18px"><a class="btn primary" href="contact.html#rfq">Request a quote</a><a class="btn" href="https://wa.me/{WA_NUMBER}" target="_blank" rel="noopener">Ask on WhatsApp</a></div></section>
<section class="block" style="padding-top:28px"><div class="wrap"><h2>Products in this range</h2><div class="plist">{plist}</div></div></section>
<section class="block field"><div class="wrap"><div class="split">
<div><h2>Specifications</h2><p>Only figures the factory can stand behind are published here. Density, exact sheet sizes and minimum quantities are confirmed on each quotation.</p><div class="tbl-wrap"><table class="spec">{spec}</table></div></div>
<div><h2>Common questions</h2><div class="faq">{faqs}</div></div>
</div></div></section>
<section class="block"><div class="wrap"><div class="split"><div><h2>Other product families</h2><ul>{others}</ul></div><div><h2>Need this for a specific industry?</h2><p>See how we pack for <a href="industry-electronics-packaging.html">electronics</a>, <a href="industry-motor-packaging.html">motors and electrical equipment</a>, and <a href="industries.html">other industries</a>.</p></div></div></div></section>
"""
    return head(c["title"], c["desc"], f'{c["slug"]}.html', [crumb_ld, faq_ld]) + header("products.html") + body + footer()

def page_industries():
    crumb_html, crumb_ld = crumbs([("Home", "index.html"), ("Industries", None)])
    detail = {
        "automotive": ["Headlamps, mirrors, bumpers and trims arrive with scratches and cracks when they are packed in loose material. A moulded EPS or EPE cavity holds each part on its strongest surfaces and keeps finished faces clear of contact.", "Typical products: EPS inserts for lamps and clusters, EPE fitments for painted parts, returnable EPE trays for line-side delivery, corner buffers for bulk cartons."],
        "pharma": ["Vaccines, reagents and samples need a known holding time between dispatch and delivery. Wall thickness and coolant quantity are matched to the route and ambient conditions.", "Typical products: insulated vaccine boxes with lids, sample carriers, gel-pack recesses, secondary cartons sized to the box."],
        "consumer": ["Mugs, bottles, lamps, cookware and gift sets break when pieces touch each other. Nested cavities separate every item.", "Typical products: multi-cavity EPS trays, two-part gift boxes, EPE inserts for premium finishes."],
        "food": ["Seafood, dairy, meat and ice cream need insulation and, sometimes, drainage and stacking.", "Typical products: 10 litre ice boxes, fish boxes with stacking lids, custom shippers for chilled delivery."],
        "construction": ["Insulation and void forming where a light, rigid, moisture-resistant material is needed.", "Typical products: 30 mm and 50 mm insulation sheets, half-round pipe sections cut to pipe diameter, void formers and spacers."],
    }
    sections = ""
    for k, n, d, h in INDUSTRIES:
        if k in ("electronics", "motors"):
            sections += f'<section class="block" id="{k}" style="padding:28px 0"><div class="wrap"><div class="split"><div><h2>{n}</h2><p>{d}</p><a class="btn" href="{h}">Read the {n.lower()} page</a></div></div></div></section>'
        else:
            p1, p2 = detail[k]
            sections += f'<section class="block" id="{k}" style="padding:28px 0"><div class="wrap"><div class="split"><div><h2>{n}</h2><p>{p1}</p></div><div><p>{p2}</p><a class="btn sm" href="contact.html#rfq">Request a quote for {n.lower()}</a></div></div></div></section>'
    body = f"""{crumb_html}
<section class="page-head wrap"><h1>Industries we pack for</h1><p class="lede">The material is the same; the engineering is different for every product and route. Below is what we typically make for each sector. If yours is not listed, the process is the same: send the product and we design around it.</p></section>
{sections}
<section class="block navy"><div class="wrap"><div class="split"><div><h2>Send us the product</h2><p>A drawing, photos with dimensions, or the physical item. We reply with a proposal and price.</p><a class="btn primary" href="contact.html#rfq">Request a quote</a></div></div></div></section>
"""
    return head("Industries Served | Automotive, Electronics, Motors, Pharma, Food Packaging | Yash Packers",
                "EPS thermocol and EPE foam packaging for automotive components, electronics, electric motors, pharma cold chain, glassware, seafood and construction. Manufacturer in Greater Noida.",
                "industries.html", [crumb_ld]) + header("industries.html") + body + footer()

def page_industry_landing(slug, name, title, desc, h1, intro, packs, caps, faqs, related):
    crumb_html, crumb_ld = crumbs([("Home", "index.html"), ("Industries", "industries.html"), (name, None)])
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    packs_html = "".join(f'<article><div class="photo">Product photograph<br>(to be supplied)</div><h3>{n}</h3><p>{d}</p></article>' for n, d in packs)
    caps_html = "".join(f'<tr><th scope="row">{k}</th><td>{v}</td></tr>' for k, v in caps)
    faq_html = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs)
    body = f"""{crumb_html}
<section class="page-head wrap"><h1>{h1}</h1><p class="lede">{intro}</p><div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:18px"><a class="btn primary" href="contact.html#rfq">Request a quote</a><a class="btn" href="{related}">See the product range</a></div></section>
<section class="block" style="padding-top:28px"><div class="wrap"><h2>What we typically make</h2><div class="plist">{packs_html}</div></div></section>
<section class="block field"><div class="wrap"><div class="split">
<div><h2>Capabilities for this sector</h2><div class="tbl-wrap"><table class="spec">{caps_html}</table></div></div>
<div><h2>Common questions</h2><div class="faq">{faq_html}</div></div>
</div></div></section>
<section class="block navy"><div class="wrap"><div class="split"><div><h2>Start with the product</h2><p>Send a drawing or photos with dimensions, or courier the item to the factory. We design the pack and send a sample for approval before production.</p><a class="btn primary" href="contact.html#rfq">Request a quote</a></div></div></div></section>
"""
    return head(title, desc, f"{slug}.html", [crumb_ld, faq_ld]) + header("industries.html") + body + footer()

def page_about():
    crumb_html, crumb_ld = crumbs([("Home", "index.html"), ("Manufacturing", None)])
    body = f"""{crumb_html}
<section class="page-head wrap"><h1>Manufacturing and quality</h1><p class="lede">Yash Packers is a proprietorship manufacturer established in 2020 at Plot J-5, Site-5, Kasna Industrial Area (UPSIDA), Greater Noida. We make EPS thermocol and EPE foam packaging for manufacturers in Delhi NCR and across India.</p></section>
<section class="block" style="padding-top:28px"><div class="wrap"><div class="split">
<div><h2>Facility</h2><p>Our factory is in the UPSIDA industrial estate at Kasna, Greater Noida, with road access to the Yamuna Expressway, Noida, Ghaziabad and Delhi. EPS moulding, block cutting and EPE conversion are done on site, so a custom pack that combines both materials is made under one roof.</p>
<div class="plist" style="grid-template-columns:1fr 1fr"><article><div class="photo">Factory exterior photograph<br>(to be supplied)</div></article><article><div class="photo">Moulding shop photograph<br>(to be supplied)</div></article><article><div class="photo">Block cutting photograph<br>(to be supplied)</div></article><article><div class="photo">Finished goods store photograph<br>(to be supplied)</div></article></div></div>
<div><h2>What happens on the floor</h2>
<ol class="process">
<li><div><h4>Pre-expansion</h4><p>Raw EPS beads are expanded with steam to the target density. Density is set here, so it is checked for every job.</p></div></li>
<li><div><h4>Moulding</h4><p>Expanded beads are fused in a shape mould or block mould under steam and pressure.</p></div></li>
<li><div><h4>Cutting and finishing</h4><p>Blocks are cut into sheets, pipe sections and profiles. Moulded parts are trimmed and inspected.</p></div></li>
<li><div><h4>EPE conversion</h4><p>EPE sheet is die-cut, routed, laminated and glued into boxes, inserts and fitments.</p></div></li>
<li><div><h4>Inspection and dispatch</h4><p>Dimensions, fit and finish are checked against the approved sample before packing for dispatch.</p></div></li>
</ol></div>
</div></div></section>
<section class="block field"><div class="wrap"><div class="split">
<div><h2>Quality</h2><p>Every new design is approved on a physical sample before a production run. Density is controlled at pre-expansion and checked on finished parts. Dimensional checks are made against the approved sample, and drop or compression tests can be arranged for critical products.</p>
<div class="tbl-wrap"><table class="spec"><caption>Certifications and registrations</caption><tr><th scope="row">GST</th><td>{GST}</td></tr><tr><th scope="row">ISO 9001</th><td>Certificate number and validity to be added here, with a downloadable copy. Publish only if the certificate is current and verifiable.</td></tr><tr><th scope="row">Other</th><td>Add any material test reports or customer approvals that can be shared.</td></tr></table></div></div>
<div><h2>Company facts</h2><div class="tbl-wrap"><table class="spec"><tr><th scope="row">Established</th><td>2020</td></tr><tr><th scope="row">Legal status</th><td>Proprietorship</td></tr><tr><th scope="row">Factory</th><td>{ADDRESS}</td></tr><tr><th scope="row">Registered office</th><td>C-430, Pocket P3, Greater Noida (confirm whether to publish)</td></tr><tr><th scope="row">Materials</th><td>EPS (expanded polystyrene), EPE (expanded polyethylene)</td></tr><tr><th scope="row">Capacity</th><td>Add verified monthly output here once confirmed</td></tr></table></div></div>
</div></div></section>
<section class="block"><div class="wrap"><div class="split"><div><h2>Customers and case studies</h2><p>This section should carry two or three short write-ups with the customer's permission: the product, the packaging problem, the pack we designed, and the result. One photograph each. It is the single strongest trust signal a procurement manager looks for.</p></div><div><h2>Team</h2><p>Add photographs and one line each for the proprietor, the engineer who designs cavities, and the production lead. Names and faces turn a supplier into people a buyer can call.</p></div></div></div></section>
"""
    return head("Manufacturing Facility and Quality | Yash Packers, Kasna Industrial Area, Greater Noida",
                "Yash Packers' EPS and EPE manufacturing facility in Kasna Industrial Area, Greater Noida: moulding, block cutting, EPE conversion, sample approval and quality checks. Established 2020.",
                "about.html", [crumb_ld]) + header("about.html") + body + footer()

def page_contact():
    crumb_html, crumb_ld = crumbs([("Home", "index.html"), ("Contact", None)])
    body = f"""{crumb_html}
<section class="page-head wrap"><h1>Contact and quotation</h1><p class="lede">The fastest route is the form below, which opens a WhatsApp message with your requirement filled in. You can also call, email, or visit the factory.</p></section>
<section class="block" style="padding-top:28px"><div class="wrap"><div class="split">
{rfq_form()}
<div class="contact-side">
<h2>Reach us directly</h2>
<p><strong>Phone / WhatsApp</strong><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
<p><strong>Email</strong><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p><strong>Factory</strong>{ADDRESS}</p>
<p><strong>Hours</strong>Monday to Saturday, 9:30 am to 6:30 pm (confirm)</p>
<p><strong>GST</strong>{GST}</p>
<iframe class="map" src="https://www.google.com/maps?q=Plot+J-5,+Site+5,+Kasna+Industrial+Area,+Greater+Noida+201308&output=embed" loading="lazy" title="Map showing Yash Packers factory in Kasna Industrial Area, Greater Noida" referrerpolicy="no-referrer-when-downgrade"></iframe>
</div>
</div></div></section>
"""
    return head("Contact Yash Packers | Request a Packaging Quotation | Greater Noida",
                "Request a quotation for EPS thermocol or EPE foam packaging from Yash Packers, Kasna Industrial Area, Greater Noida. WhatsApp, phone, email and factory address.",
                "contact.html", [crumb_ld]) + header("contact.html") + body + footer()

ARTICLES = [
  ("eps-vs-epe-foam-packaging.html", "EPS vs EPE foam: which is better for packaging?", "Rigid and economical, or soft and reusable. How to choose, and when to use both in one pack."),
  (None, "How to choose the right thermocol packaging box", "Weight, fragility, transit route and carton size: the four questions that decide the design."),
  (None, "Understanding EPS density and compression strength", "What density means, why it matters more than thickness, and how to specify it."),
  (None, "How thermocol packaging protects fragile electronics", "Cavity design, cable clearance and why the insert should never touch the display."),
  (None, "Choosing thermocol insulation sheet thickness", "30 mm or 50 mm? A practical guide for cold rooms, roofs and prefab panels."),
  (None, "Custom packaging for automotive components", "Returnable EPE trays, painted-part protection and line-side delivery packs."),
]

def page_resources():
    crumb_html, crumb_ld = crumbs([("Home", "index.html"), ("Resources", None)])
    teasers = "".join((f'<a href="{h}"><h3>{t}</h3><p>{d}</p></a>' if h else f'<a href="#" aria-disabled="true" style="opacity:.6"><h3>{t}</h3><p>{d}</p><p class="small muted" style="margin-top:8px">Coming soon</p></a>') for h, t, d in ARTICLES)
    body = f"""{crumb_html}
<section class="page-head wrap"><h1>Packaging guides</h1><p class="lede">Short, practical notes from the factory floor on choosing and specifying protective packaging. Written for procurement managers and engineers, not search engines.</p></section>
<section class="block" style="padding-top:28px"><div class="wrap"><div class="teasers">{teasers}</div></div></section>
"""
    return head("Packaging Guides | EPS, EPE and Thermocol Packaging Advice | Yash Packers",
                "Practical guides on choosing EPS thermocol and EPE foam packaging: EPS vs EPE, density and compression strength, insulation sheet thickness and protecting electronics in transit.",
                "resources.html", [crumb_ld]) + header("resources.html") + body + footer()

def page_article():
    crumb_html, crumb_ld = crumbs([("Home", "index.html"), ("Resources", "resources.html"), ("EPS vs EPE foam", None)])
    art_ld = {"@context": "https://schema.org", "@type": "Article", "headline": "EPS vs EPE foam: which is better for packaging?", "author": {"@type": "Organization", "name": "Yash Packers"}, "publisher": {"@type": "Organization", "name": "Yash Packers"}, "datePublished": "2026-11-08"}
    body = f"""{crumb_html}
<section class="page-head wrap"><h1>EPS vs EPE foam: which is better for packaging?</h1><p class="lede">Both are foams, both protect products in transit, and both are made at our factory. They behave very differently, and most packaging problems we see come from using one where the other belongs.</p></section>
<section class="block article wrap" style="padding-top:20px">
<h2>What each material is</h2>
<p><strong>EPS</strong> (expanded polystyrene, sold in India as thermocol) is made by expanding polystyrene beads with steam and fusing them in a mould. The result is rigid, light, and about 98% air. It holds its shape, insulates well, and is cheap per litre of volume.</p>
<p><strong>EPE</strong> (expanded polyethylene) is a closed-cell foam made in sheets. It is soft and flexible, does not crumble, and springs back after it is compressed. It costs more than EPS for the same volume.</p>
<h2>When EPS is the right choice</h2>
<ul><li>The product is heavy and needs a rigid cradle: motors, pumps, compressors, castings.</li><li>You need the pack to carry stacking load inside the carton.</li><li>Temperature matters: ice boxes, vaccine carriers, insulation sheets.</li><li>Volumes are high and cost per piece matters more than reuse.</li><li>The product's surface is not easily marked.</li></ul>
<h2>When EPE is the right choice</h2>
<ul><li>The surface is polished, painted, lacquered or printed and must not be scuffed.</li><li>The pack is opened and closed many times or returned for reuse: line-side trays, demo kits, instruments.</li><li>The product is light but fragile and needs a softer landing: glass, optics, electronics with displays.</li><li>You need a premium unboxing finish (EPE can be laminated with cloth or film).</li></ul>
<h2>Using both in one pack</h2>
<p>A common and economical design is an EPS outer for structure, insulation and stacking strength, with EPE pads or an EPE lining only where the foam touches a sensitive surface. You pay for EPE only where it earns its keep.</p>
<div class="tbl-wrap"><table class="spec"><caption>Quick comparison</caption>
<tr><th scope="row">Rigidity</th><td>EPS rigid; EPE flexible</td></tr>
<tr><th scope="row">Surface contact</th><td>EPS can abrade soft finishes; EPE is non-abrasive</td></tr>
<tr><th scope="row">Recovery after impact</th><td>EPS can crush permanently; EPE recovers</td></tr>
<tr><th scope="row">Insulation</th><td>EPS better</td></tr>
<tr><th scope="row">Cost per volume</th><td>EPS lower</td></tr>
<tr><th scope="row">Reuse</th><td>EPE better</td></tr>
</table></div>
<h2>Still not sure?</h2>
<p>Send us the product weight, a photo, and how it ships. We will tell you which material, what density, and what it will cost. <a href="contact.html#rfq">Request a quote</a>.</p>
</section>
"""
    return head("EPS vs EPE Foam: Which Is Better for Packaging? | Yash Packers",
                "The practical difference between EPS thermocol and EPE foam for protective packaging: rigidity, surface contact, insulation, cost and reuse, and when to combine both.",
                "eps-vs-epe-foam-packaging.html", [crumb_ld, art_ld]) + header("resources.html") + body + footer()

def page_404():
    body = """<section class="page-head wrap"><h1>Page not found</h1><p class="lede">The page you asked for is not here. It may have moved when the website was redesigned.</p><div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:18px"><a class="btn primary" href="products.html">See products</a><a class="btn" href="contact.html#rfq">Request a quote</a><a class="btn" href="index.html">Home</a></div></section>"""
    return head("Page not found | Yash Packers", "The page could not be found.", "404.html") + header("") + body + footer()

MAIN_JS = r"""
(function () {
  var btn = document.querySelector('.menu-btn'), nav = document.getElementById('mainnav');
  if (btn && nav) btn.addEventListener('click', function () { var open = nav.classList.toggle('open'); btn.setAttribute('aria-expanded', open); btn.textContent = open ? '✕' : '☰'; });

  function fieldMessage(form) {
    var g = function (id) { var el = form.querySelector('#' + id); return el && el.value ? el.value.trim() : ''; };
    var lines = ['Quotation request from the website', '',
      'Product: ' + g('f-product'), 'Quantity: ' + g('f-qty'), 'Dimensions: ' + g('f-dims'), 'Industry: ' + g('f-industry'),
      'Details: ' + g('f-notes'), '', 'Name: ' + g('f-name'), 'Company: ' + g('f-company'), 'Phone: ' + g('f-phone'), 'Email: ' + g('f-email')];
    return lines.join('\n');
  }
  document.querySelectorAll('form.rfq').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var url = 'https://wa.me/' + form.dataset.wa + '?text=' + encodeURIComponent(fieldMessage(form));
      window.open(url, '_blank', 'noopener');
    });
    var em = form.querySelector('#rfq-email');
    if (em) em.addEventListener('click', function () {
      if (!form.reportValidity()) return;
      location.href = 'mailto:' + form.dataset.email + '?subject=' + encodeURIComponent('Quotation request: ' + (form.querySelector('#f-product').value || 'packaging')) + '&body=' + encodeURIComponent(fieldMessage(form));
    });
  });
})();
"""

def build():
    os.makedirs(OUT + "/assets", exist_ok=True)
    pages = {"index.html": page_home(), "products.html": page_products(), "industries.html": page_industries(),
             "about.html": page_about(), "contact.html": page_contact(), "resources.html": page_resources(),
             "eps-vs-epe-foam-packaging.html": page_article(), "404.html": page_404()}
    for c in CATS:
        pages[f'{c["slug"]}.html'] = page_category(c)
    pages["industry-electronics-packaging.html"] = page_industry_landing(
        "industry-electronics-packaging", "Electronics and appliances",
        "EPS Thermocol Packaging for Electronics and Appliances | Manufacturer | Yash Packers",
        "Custom EPS thermocol and EPE foam packaging for electronics and appliances: set-top boxes, inverters, meters, printers, panels and small appliances. Made in Greater Noida.",
        "EPS and EPE packaging for electronics and appliances",
        "Electronics fail in transit for three reasons: the product moves inside the carton, the insert presses on a display or connector, or the pack does not handle a corner drop. We design the cavity so the product is held on its housing, clear of screens, ports and cables, with crush zones where the carton takes the impact.",
        [("Set-top box and router inserts", "Two-part EPS with a recess for the unit and separate pockets for remote, adapter and cables."),
         ("Inverter and UPS packaging", "Heavier-density EPS base and top sets with handle clearance and corner reinforcement for units up to several kilograms."),
         ("Meter and panel packaging", "Multi-cavity trays for energy meters, controllers and instrument panels shipped in quantity."),
         ("Printer and small-appliance packs", "EPS corner and end-cap sets that lock the product in the carton without a full-body insert, reducing material and freight."),
         ("EPE inserts for displays and polished housings", "Soft EPE where the foam touches a screen, glass or high-gloss plastic.")],
        [("Materials", "EPS for structure and stacking; EPE where the pack touches sensitive surfaces"),
         ("Design inputs needed", "Product dimensions and weight, carton size if fixed, which faces must not be touched, accessories to be packed"),
         ("Testing", "Fit check on sample; drop test can be arranged for critical products"),
         ("Branding", "Labels and printed cartons via your carton supplier"),
         ("Volumes", "Production sized to your monthly schedule; confirm MOQ at quotation")],
        [("Will the insert mark a glossy surface?", "EPS can scuff a high-gloss or soft-touch finish over a long journey. Where the pack touches such a surface we add an EPE pad or line the cavity with EPE."),
         ("Can one insert hold the unit and all accessories?", "Yes. Separate pockets for the remote, adapter, cables and manuals are moulded into the same piece, which also stops accessories rattling against the unit."),
         ("How do we handle multiple models with similar housings?", "A single mould can sometimes serve several models with small interchangeable inserts. Send the range and we will check.")],
        "eps-thermocol-packaging.html")
    pages["industry-motor-packaging.html"] = page_industry_landing(
        "industry-motor-packaging", "Motors and electrical equipment",
        "Thermocol Packaging for Electric Motors and Electrical Equipment | Yash Packers",
        "Heavy-duty EPS thermocol packaging for electric motors, pumps, alternators and switchgear, with shaft and terminal-box recesses. Manufacturer in Greater Noida.",
        "Heavy-duty EPS packaging for motors and electrical equipment",
        "A motor is heavy, oddly shaped, and has a shaft that will punch through weak packaging. We mould base and top sets in a higher-density EPS, with the load carried on the motor frame and feet, a recess for the shaft and key, and clearance for the terminal box and eye bolt.",
        [("Motor base and top sets", "Two-piece sets sized to the frame; the base carries weight on the feet and frame, the top locks the unit in the carton."),
         ("Pump and compressor packaging", "Cavities for irregular castings with the mass centred over the strongest section of the insert."),
         ("Alternator and generator-set component packs", "Larger sets with reinforcing ribs and stacking faces for pallet shipment."),
         ("Switchgear and panel packaging", "Edge and corner protection with door and handle clearance for enclosures shipped upright."),
         ("Shaft and flange protectors", "Separate EPS caps for shafts and machined flanges where a full insert is not required.")],
        [("Density", "Higher-density EPS for loads; exact grade recommended per product weight"),
         ("Design inputs needed", "Frame size or drawing, weight, shaft diameter and length, terminal box position, carton or pallet pattern"),
         ("Load", "Insert designed to carry weight on frame and feet, never on the shaft or fan cover"),
         ("Stacking", "Stacking faces moulded in for palletised dispatch where required"),
         ("Volumes", "Production to your schedule; confirm MOQ at quotation")],
        [("Can the same set serve several frame sizes?", "Often two or three adjacent frame sizes can share a set with a different insert; larger jumps need their own mould. Send the frame list and we will group them."),
         ("What about rust protection?", "EPS does not absorb water, but it is not a vapour barrier. For export, combine the insert with a VCI bag or film; we can size the cavity to allow for it."),
         ("Do you make the pallet-level packaging too?", "We make the EPS components, including layer pads and corner buffers. Pallets and strapping are usually arranged by your dispatch team.")],
        "eps-thermocol-packaging.html")
    for name, content in pages.items():
        open(f"{OUT}/{name}", "w").write(content)
    open(f"{OUT}/assets/main.js", "w").write(MAIN_JS)
    urls = [p for p in pages if p != "404.html"]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{DOMAIN}/{'' if u == 'index.html' else u}</loc></url>\n" for u in urls) + "</urlset>\n"
    open(f"{OUT}/sitemap.xml", "w").write(sm)
    open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    open(f"{OUT}/.nojekyll", "w").write("")
    print("built", len(pages), "pages")

if __name__ == "__main__":
    build()
