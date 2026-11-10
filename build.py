#!/usr/bin/env python3
"""Render the Damla site into docs/.  Python standard library only, deterministic.

    python3 build.py

Inputs : site.config.json (every owner-specific value), templates/*.html, content/*.md, assets/*, static/*
Output : docs/   (committed, because GitHub Pages serves it)
"""
import html
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "docs"
CFG = json.loads((ROOT / "site.config.json").read_text(encoding="utf-8"))
# Translated legal pages: content/i18n/<lang>/<page>.md, added only after a native reader has approved them. A language with no file for a page
# is simply not offered for that page, so nothing half-translated is ever published.
LANGS = {
    "en": {"name": "English", "dir": "ltr", "skip": "Skip to content", "privacy": "Privacy", "terms": "Terms", "switch": "Language",
           "note": "{app} gives information, not financial advice.",
           "desc": {"privacy": "How {app} handles your data: no accounts, no analytics, data on your phone.",
                    "terms": "The terms for using {app}, including the financial disclaimer."}},
    "tr": {"name": "T\u00fcrk\u00e7e", "dir": "ltr", "skip": "\u0130\u00e7eri\u011fe ge\u00e7", "privacy": "Gizlilik", "terms": "Ko\u015fullar", "switch": "Dil",
           "note": "{app} finansal tavsiye de\u011fil, bilgi verir.",
           "desc": {"privacy": "{app} verilerinizi nas\u0131l ele al\u0131r: hesap yok, analiz yok, veriler telefonunuzda.",
                    "terms": "{app} kullan\u0131m ko\u015fullar\u0131 ve finansal sorumluluk reddi."}},
    "fr": {"name": "Fran\u00e7ais", "dir": "ltr", "skip": "Aller au contenu", "privacy": "Confidentialit\u00e9", "terms": "Conditions", "switch": "Langue",
           "note": "{app} fournit des informations, pas des conseils financiers.",
           "desc": {"privacy": "Comment {app} traite vos donn\u00e9es : pas de compte, pas d\u2019analyse, donn\u00e9es sur votre t\u00e9l\u00e9phone.",
                    "terms": "Les conditions d\u2019utilisation de {app}, y compris l\u2019avertissement financier."}},
    "ar": {"name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629", "dir": "rtl", "skip": "\u062a\u062c\u0627\u0648\u0632 \u0625\u0644\u0649 \u0627\u0644\u0645\u062d\u062a\u0648\u0649",
           "privacy": "\u0627\u0644\u062e\u0635\u0648\u0635\u064a\u0629", "terms": "\u0627\u0644\u0634\u0631\u0648\u0637", "switch": "\u0627\u0644\u0644\u063a\u0629",
           "note": "\u062a\u0642\u062f\u0651\u0645 {app} \u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0648\u0644\u064a\u0633\u062a \u0646\u0635\u064a\u062d\u0629 \u0645\u0627\u0644\u064a\u0629.",
           "desc": {"privacy": "\u0643\u064a\u0641 \u062a\u062a\u0639\u0627\u0645\u0644 {app} \u0645\u0639 \u0628\u064a\u0627\u0646\u0627\u062a\u0643: \u0628\u0644\u0627 \u062d\u0633\u0627\u0628\u0627\u062a \u0648\u0644\u0627 \u062a\u062d\u0644\u064a\u0644\u0627\u062a\u060c \u0648\u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a \u0639\u0644\u0649 \u0647\u0627\u062a\u0641\u0643.",
                    "terms": "\u0634\u0631\u0648\u0637 \u0627\u0633\u062a\u062e\u062f\u0627\u0645 {app} \u0645\u0639 \u0625\u062e\u0644\u0627\u0621 \u0627\u0644\u0645\u0633\u0624\u0648\u0644\u064a\u0629 \u0627\u0644\u0645\u0627\u0644\u064a\u0629."}},
}
LEGAL_PAGES = ("privacy", "terms")

# Interface words around the translated pages. English is the source; each language is a plain translation of these few labels.
CHROME = {
    "en": {"guide": "Guide", "support": "Support", "browse": "Browse the guide", "all": "All topics", "onpage": "On this page",
           "unclear": "Something unclear or missing? Write to {email} and say which page.", "search": "Search the guide",
           "ph": "for example: forecast, card, backup", "none": "Nothing found. Try another word.", "prevnext": "Previous and next",
           "gtitle": "{app} guide", "gsuffix": "{app} guide", "glead": "What every part of {app} does and how to use it, in plain words, with worked examples. Every example uses invented people and numbers.",
           "gdesc": "A detailed guide to {app}: what each feature does, how to use it, and worked examples.", "gpagetitle": "{app} guide: how to use every feature",
           "store_soon": "Coming to the App Store", "store_btn": "View on the App Store",
           "home_title": "{app}: cash-flow app for iPhone", "home_desc": "{app} is a cash-flow app for your household that runs on your iPhone, keeps your data on the phone, and shows what is safe to spend.",
           "support_title": "Support - {app}", "support_desc": "How to contact support for {app}, and answers to common questions.",
           "callouts": {"tip": "Tip", "note": "Note", "careful": "Careful", "example": "Example", "limit": "Limit"}},
    "tr": {"guide": "K\u0131lavuz", "support": "Destek", "browse": "K\u0131lavuzda gezin", "all": "T\u00fcm konular", "onpage": "Bu sayfada",
           "unclear": "Anla\u015f\u0131lmayan ya da eksik bir \u015fey mi var? {email} adresine yaz\u0131n ve hangi sayfa oldu\u011funu belirtin.", "search": "K\u0131lavuzda ara",
           "ph": "\u00f6rne\u011fin: tahmin, kart, yedek", "none": "Sonu\u00e7 bulunamad\u0131. Ba\u015fka bir s\u00f6zc\u00fck deneyin.", "prevnext": "\u00d6nceki ve sonraki",
           "gtitle": "{app} k\u0131lavuzu", "gsuffix": "{app} k\u0131lavuzu", "glead": "{app} uygulamas\u0131n\u0131n her b\u00f6l\u00fcm\u00fcn\u00fcn ne yapt\u0131\u011f\u0131 ve nas\u0131l kullan\u0131laca\u011f\u0131, sade s\u00f6zlerle ve \u00e7al\u0131\u015f\u0131lm\u0131\u015f \u00f6rneklerle. Her \u00f6rnekte uydurma ki\u015filer ve rakamlar kullan\u0131l\u0131r.",
           "gdesc": "{app} i\u00e7in ayr\u0131nt\u0131l\u0131 k\u0131lavuz: her \u00f6zelli\u011fin ne yapt\u0131\u011f\u0131, nas\u0131l kullan\u0131laca\u011f\u0131 ve \u00e7al\u0131\u015f\u0131lm\u0131\u015f \u00f6rnekler.", "gpagetitle": "{app} k\u0131lavuzu: her \u00f6zellik nas\u0131l kullan\u0131l\u0131r",
           "store_soon": "App Store\u2019a geliyor", "store_btn": "App Store\u2019da g\u00f6r\u00fcnt\u00fcle",
           "home_title": "{app}: iPhone i\u00e7in nakit ak\u0131\u015f\u0131 uygulamas\u0131", "home_desc": "{app}, haneniz i\u00e7in iPhone\u2019unuzda \u00e7al\u0131\u015fan, verilerinizi telefonda tutan ve harcaman\u0131n g\u00fcvenli oldu\u011fu tutar\u0131 g\u00f6steren bir nakit ak\u0131\u015f\u0131 uygulamas\u0131d\u0131r.",
           "support_title": "Destek - {app}", "support_desc": "{app} i\u00e7in destekle nas\u0131l ileti\u015fime ge\u00e7ilece\u011fi ve s\u0131k sorulan sorular\u0131n yan\u0131tlar\u0131.",
           "callouts": {"tip": "\u0130pucu", "note": "Not", "careful": "Dikkat", "example": "\u00d6rnek", "limit": "S\u0131n\u0131r"}},
    "fr": {"guide": "Guide", "support": "Assistance", "browse": "Parcourir le guide", "all": "Tous les sujets", "onpage": "Sur cette page",
           "unclear": "Quelque chose n\u2019est pas clair ou manque ? \u00c9crivez \u00e0 {email} en indiquant la page.", "search": "Rechercher dans le guide",
           "ph": "par exemple : pr\u00e9vision, carte, sauvegarde", "none": "Aucun r\u00e9sultat. Essayez un autre mot.", "prevnext": "Pr\u00e9c\u00e9dent et suivant",
           "gtitle": "Guide de {app}", "gsuffix": "guide de {app}", "glead": "Ce que fait chaque partie de {app} et comment l\u2019utiliser, en mots simples, avec des exemples chiffr\u00e9s. Tous les exemples utilisent des personnes et des chiffres invent\u00e9s.",
           "gdesc": "Un guide d\u00e9taill\u00e9 de {app} : ce que fait chaque fonction, comment l\u2019utiliser, avec des exemples chiffr\u00e9s.", "gpagetitle": "Guide de {app} : utiliser chaque fonction",
           "store_soon": "Bient\u00f4t sur l\u2019App Store", "store_btn": "Voir sur l\u2019App Store",
           "home_title": "{app} : application de tr\u00e9sorerie pour iPhone", "home_desc": "{app} est une application de tr\u00e9sorerie pour votre foyer, qui fonctionne sur votre iPhone, garde vos donn\u00e9es sur le t\u00e9l\u00e9phone et montre ce que vous pouvez d\u00e9penser en toute s\u00e9curit\u00e9.",
           "support_title": "Assistance - {app}", "support_desc": "Comment contacter l\u2019assistance de {app}, et les r\u00e9ponses aux questions courantes.",
           "callouts": {"tip": "Astuce", "note": "Remarque", "careful": "Attention", "example": "Exemple", "limit": "Limite"}},
    "ar": {"guide": "\u0627\u0644\u062f\u0644\u064a\u0644", "support": "\u0627\u0644\u062f\u0639\u0645", "browse": "\u062a\u0635\u0641\u0651\u062d \u0627\u0644\u062f\u0644\u064a\u0644", "all": "\u0643\u0644 \u0627\u0644\u0645\u0648\u0627\u0636\u064a\u0639", "onpage": "\u0641\u064a \u0647\u0630\u0647 \u0627\u0644\u0635\u0641\u062d\u0629",
           "unclear": "\u0647\u0644 \u0647\u0646\u0627\u0643 \u0634\u064a\u0621 \u063a\u064a\u0631 \u0648\u0627\u0636\u062d \u0623\u0648 \u0646\u0627\u0642\u0635\u061f \u0627\u0643\u062a\u0628 \u0625\u0644\u0649 {email} \u0648\u0627\u0630\u0643\u0631 \u0627\u0644\u0635\u0641\u062d\u0629.", "search": "\u0627\u0628\u062d\u062b \u0641\u064a \u0627\u0644\u062f\u0644\u064a\u0644",
           "ph": "\u0645\u062b\u0644\u0627\u064b: \u0627\u0644\u062a\u0648\u0642\u0639\u060c \u0628\u0637\u0627\u0642\u0629\u060c \u0646\u0633\u062e\u0629 \u0627\u062d\u062a\u064a\u0627\u0637\u064a\u0629", "none": "\u0644\u0645 \u064a\u064f\u0639\u062b\u0631 \u0639\u0644\u0649 \u0646\u062a\u0627\u0626\u062c. \u062c\u0631\u0651\u0628 \u0643\u0644\u0645\u0629 \u0623\u062e\u0631\u0649.", "prevnext": "\u0627\u0644\u0633\u0627\u0628\u0642 \u0648\u0627\u0644\u062a\u0627\u0644\u064a",
           "gtitle": "\u062f\u0644\u064a\u0644 {app}", "gsuffix": "\u062f\u0644\u064a\u0644 {app}", "glead": "\u0645\u0627 \u062a\u0641\u0639\u0644\u0647 \u0643\u0644 \u0645\u064a\u0632\u0629 \u0645\u0646 {app} \u0648\u0643\u064a\u0641 \u062a\u0633\u062a\u062e\u062f\u0645\u0647\u0627\u060c \u0628\u0643\u0644\u0645\u0627\u062a \u0628\u0633\u064a\u0637\u0629 \u0648\u0623\u0645\u062b\u0644\u0629 \u0645\u062d\u0633\u0648\u0628\u0629. \u0643\u0644 \u0627\u0644\u0623\u0645\u062b\u0644\u0629 \u062a\u0633\u062a\u062e\u062f\u0645 \u0623\u0634\u062e\u0627\u0635\u0627\u064b \u0648\u0623\u0631\u0642\u0627\u0645\u0627\u064b \u0645\u062e\u062a\u0631\u0639\u0629.",
           "gdesc": "\u062f\u0644\u064a\u0644 \u0645\u0641\u0635\u0651\u0644 \u0644\u0640 {app}: \u0645\u0627 \u062a\u0641\u0639\u0644\u0647 \u0643\u0644 \u0645\u064a\u0632\u0629 \u0648\u0643\u064a\u0641 \u062a\u0633\u062a\u062e\u062f\u0645\u0647\u0627 \u0645\u0639 \u0623\u0645\u062b\u0644\u0629 \u0645\u062d\u0633\u0648\u0628\u0629.", "gpagetitle": "\u062f\u0644\u064a\u0644 {app}: \u0643\u064a\u0641 \u062a\u0633\u062a\u062e\u062f\u0645 \u0643\u0644 \u0645\u064a\u0632\u0629",
           "store_soon": "\u0642\u0631\u064a\u0628\u064b\u0627 \u0639\u0644\u0649 App Store", "store_btn": "\u0639\u0631\u0636 \u0641\u064a App Store",
           "home_title": "{app}: \u062a\u0637\u0628\u064a\u0642 \u0627\u0644\u062a\u062f\u0641\u0642 \u0627\u0644\u0646\u0642\u062f\u064a \u0644\u0644\u0622\u064a\u0641\u0648\u0646", "home_desc": "{app} \u062a\u0637\u0628\u064a\u0642 \u0644\u0644\u062a\u062f\u0641\u0642 \u0627\u0644\u0646\u0642\u062f\u064a \u0644\u0623\u0633\u0631\u062a\u0643 \u064a\u0639\u0645\u0644 \u0639\u0644\u0649 \u0647\u0627\u062a\u0641\u0643\u060c \u0648\u064a\u064f\u0628\u0642\u064a \u0628\u064a\u0627\u0646\u0627\u062a\u0643 \u0639\u0644\u0649 \u0627\u0644\u062c\u0647\u0627\u0632\u060c \u0648\u064a\u064f\u0638\u0647\u0631 \u0627\u0644\u0645\u0628\u0644\u063a \u0627\u0644\u0622\u0645\u0646 \u0644\u0644\u0625\u0646\u0641\u0627\u0642.",
           "support_title": "\u0627\u0644\u062f\u0639\u0645 - {app}", "support_desc": "\u0643\u064a\u0641 \u062a\u062a\u0648\u0627\u0635\u0644 \u0645\u0639 \u062f\u0639\u0645 {app}\u060c \u0648\u0625\u062c\u0627\u0628\u0627\u062a \u0639\u0646 \u0627\u0644\u0623\u0633\u0626\u0644\u0629 \u0627\u0644\u0634\u0627\u0626\u0639\u0629.",
           "callouts": {"tip": "\u0646\u0635\u064a\u062d\u0629", "note": "\u0645\u0644\u0627\u062d\u0638\u0629", "careful": "\u062a\u0646\u0628\u064a\u0647", "example": "\u0645\u062b\u0627\u0644", "limit": "\u062d\u062f"}},
}
SITEMAP: list[str] = []
CUR_LANG = "en"


def url_for(lang: str, rel: str) -> str:
    return rel if lang == "en" else f"{lang}/{rel}"


def i18n_src(lang: str, *parts: str) -> Path:
    return ROOT / "content" / "i18n" / lang / Path(*parts)


def exists(lang: str, rel: str) -> bool:
    """Is there a page at this English-relative URL in this language? English always; others only when a translated source exists."""
    if lang == "en":
        return True
    if rel == "":
        return i18n_src(lang, "home.html").exists()
    if rel == "support/":
        return i18n_src(lang, "support.html").exists()
    if rel in ("privacy/", "terms/"):
        return i18n_src(lang, rel.strip("/") + ".md").exists()
    if rel == "guide/":
        return i18n_src(lang, "guide", "sections.json").exists()
    m = re.match(r"guide/([^/]+)/([^/]+)/$", rel)
    return bool(m) and i18n_src(lang, "guide", m.group(1), m.group(2) + ".md").exists()


TOKEN = re.compile(r"\{\{\s*([a-z_]+)\s*\}\}")


def fill(text: str, extra: dict | None = None, where: str = "") -> str:
    """Replace {{key}} with config values. An unknown key is a build error, never silent."""
    values = {k: v for k, v in CFG.items() if isinstance(v, (str, int))}
    values.update(extra or {})

    def sub(m):
        key = m.group(1)
        if key not in values:
            sys.exit(f"build error: unknown placeholder {{{{{key}}}}} in {where}")
        return str(values[key])

    return TOKEN.sub(sub, text)


# ---------- tiny markdown (headings, lists, steps, tips, tables, images, code, paragraphs, bold, italic, links) ----------
def inline(s: str, root: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)

    def link(m):
        text, url = m.group(1), m.group(2)
        if url.startswith("/"):
            if CUR_LANG != "en" and url.startswith("/guide/") and exists(CUR_LANG, url.lstrip("/")):
                url = "/" + CUR_LANG + url   # a page not translated yet links to the English one instead of a dead end
            url = root + url.lstrip("/")
        return f'<a href="{url}">{text}</a>'

    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, s)


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def markdown(src: str, root: str, img_root: str = "", lang: str = "en") -> tuple[str, str]:
    """Return (title from the first # heading, body html)."""
    global CUR_LANG
    CUR_LANG = lang
    title, out = "", []
    para, items, ordered, quote, table, code = [], [], [], [], [], None

    def flush():
        nonlocal para, items, ordered, quote, table
        if para:
            out.append("<p>" + inline(" ".join(para), root) + "</p>")
            para = []
        if items:
            out.append("<ul>" + "".join(f"<li>{inline(i, root)}</li>" for i in items) + "</ul>")
            items = []
        if ordered:
            out.append('<ol class="steps">' + "".join(f"<li>{inline(i, root)}</li>" for i in ordered) + "</ol>")
            ordered = []
        if quote:
            text = " ".join(quote)
            kind = "note"
            m = re.match(r"\*\*(Tip|Note|Careful|Example|Limit)[:.]?\*\*", text)
            if m:
                kind = m.group(1).lower()
                if lang != "en":  # the translated page keeps the English marker word; the label shown is the translated one
                    text = f"**{CHROME[lang]['callouts'][kind]}{text[m.end() - 3] if text[m.end() - 3] in ':.' else ''}**" + text[m.end():]
            out.append(f'<aside class="callout {kind}"><p>{inline(text, root)}</p></aside>')
            quote = []
        if table:
            rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in table if not re.match(r"^\s*\|?\s*:?-{2,}", r)]
            head, body = rows[0], rows[1:]
            out.append('<div class="table"><table><thead><tr>' + "".join(f"<th>{inline(c, root)}</th>" for c in head) + "</tr></thead><tbody>"
                       + "".join("<tr>" + "".join(f"<td>{inline(c, root)}</td>" for c in r) + "</tr>" for r in body) + "</tbody></table></div>")
            table = []

    for line in src.splitlines():
        line = line.rstrip()
        if code is not None:
            if line.startswith("```"):
                out.append("<pre><code>" + html.escape("\n".join(code)) + "</code></pre>")
                code = None
            else:
                code.append(line)
            continue
        if line.startswith("```"):
            flush()
            code = []
        elif not line:
            flush()
        elif line.startswith("<!--"):
            flush()
            out.append(line)  # TODO-OWNER comments stay visible in the page source on purpose
        elif line.startswith("# "):
            flush()
            title = line[2:].strip()
        elif line.startswith("## "):
            flush()
            h = line[3:].strip()
            out.append(f'<h2 id="{slug(h)}">{inline(h, root)}</h2>')
        elif line.startswith("### "):
            flush()
            h = line[4:].strip()
            out.append(f'<h3 id="{slug(h)}">{inline(h, root)}</h3>')
        elif re.match(r"^!\[[^\]]*\]\([^)]+\)$", line):
            flush()
            m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", line)
            alt, src_ = m.group(1), m.group(2)
            out.append(f'<figure><img src="{img_root}{src_}" alt="{html.escape(alt, quote=True)}" loading="lazy"><figcaption>{inline(alt, root)}</figcaption></figure>')
        elif line.startswith("|"):
            if para or items or ordered or quote:
                flush()
            table.append(line)
        elif line.startswith("> "):
            if para or items or ordered or table:
                flush()
            quote.append(line[2:].strip())
        elif re.match(r"^\d+\. ", line):
            if para or items or quote or table:
                flush()
            ordered.append(re.sub(r"^\d+\. ", "", line).strip())
        elif line.startswith("- "):
            if para or ordered or quote or table:
                flush()
            items.append(line[2:].strip())
        else:
            if items or ordered or quote or table:
                flush()
            para.append(line.strip())
    flush()
    return title, "\n".join(out)


# ---------- pages ----------
def render(rel: str, title: str, description: str, body: str, current: str = "", wide: bool = False, lang: str = "en",
           path: str | None = None, root: str | None = None) -> None:
    """Write one page. `rel` is the English-relative URL of the page (for example "privacy/" or "guide/start/x/"); for another language the page
    lives under /<lang>/. The language switcher lists the languages that have this page, and the equivalent hreflang links go in the head."""
    base = (ROOT / "templates" / "base.html").read_text(encoding="utf-8")
    L, C = LANGS[lang], CHROME[lang]
    page_path = path or (url_for(lang, rel) + "index.html")
    if root is None:
        depth = page_path.count("/")
        root = "../" * depth if depth else "./"
    nav = []
    for key, label, r in (("guide", C["guide"], "guide/"), ("support", C["support"], "support/"), ("privacy", L["privacy"], "privacy/"), ("terms", L["terms"], "terms/")):
        if not exists(lang, r):
            continue
        cur = ' aria-current="page"' if key == current else ""
        nav.append(f'<a href="{root}{url_for(lang, r)}"{cur}>{label}</a>')
    footer_links = " &middot; ".join(f'<a href="{root}{url_for(lang, r)}">{label}</a>' for label, r in
                                    ((C["guide"], "guide/"), (C["support"], "support/"), (L["privacy"], "privacy/"), (L["terms"], "terms/")) if exists(lang, r))
    site = CFG["site_url"].rstrip("/")
    alternates, switcher = "", ""
    if rel is not None and path is None:
        have = [c for c in LANGS if exists(c, rel)]
        if len(have) > 1:
            alternates = "\n".join(f'<link rel="alternate" hreflang="{c}" href="{site}/{url_for(c, rel)}">' for c in have)
            alternates += f'\n<link rel="alternate" hreflang="x-default" href="{site}/{url_for("en", rel)}">'
        # every language is offered: the same page when it exists there, otherwise that language's home page
        links = []
        for c in LANGS:
            target = rel if exists(c, rel) else ("" if exists(c, "") else None)
            if target is None:
                continue
            if c == lang:
                links.append(f'<span aria-current="true">{LANGS[c]["name"]}</span>')
            else:
                links.append(f'<a href="{root}{url_for(c, target)}" lang="{c}" hreflang="{c}">{LANGS[c]["name"]}</a>')
        if len(links) > 1:
            switcher = f'<nav class="lang-switch" aria-label="{L["switch"]}">' + " &middot; ".join(links) + "</nav>"
    home = f'{root}{url_for(lang, "")}' if exists(lang, "") else root
    canon_rel = "" if page_path == "index.html" else page_path.replace("index.html", "")
    page = fill(
        base,
        {
            "title": html.escape(title),
            "description": html.escape(description, quote=True),
            "content": body,
            "root": root,
            "home": home,
            "nav": "\n".join(nav),
            "canonical": site + "/" + canon_rel,
            "year_note": "",
            "main_class": "wrap wide" if wide else "wrap",
            "lang": lang,
            "dir": L["dir"],
            "skip": L["skip"],
            "note": L["note"].format(app=CFG["app_name"]),
            "alternates": alternates,
            "switcher": switcher,
            "footer_links": footer_links,
        },
        where="base.html",
    )
    dest = OUT / page_path
    dest.parent.mkdir(parents=True, exist_ok=True)
    # Internal owner notes live in the SOURCE (templates/content) and README, never in the published HTML.
    page = re.sub(r"[ \t]*<!--(?:(?!-->).)*?TODO-OWNER(?:(?!-->).)*?-->[ \t]*\n?", "", page, flags=re.S)
    dest.write_text(page, encoding="utf-8")
    if path is None:
        SITEMAP.append(canon_rel)


def fragment(name: str, root: str, lang: str = "en") -> str:
    extra = {"root": root}
    C = CHROME[lang]
    if CFG.get("app_store_url"):
        extra["store"] = f'<a class="button" href="{html.escape(CFG["app_store_url"])}">{C["store_btn"]}</a>'
    else:
        extra["store"] = f'<p class="soon"><strong>{C["store_soon"]}</strong></p>'
    src = ROOT / "templates" / name if lang == "en" else i18n_src(lang, "home.html" if name == "index.html" else name)
    return fill(src.read_text(encoding="utf-8"), extra, where=str(src))


def legal(md_name: str, root: str, lang: str = "en") -> tuple[str, str]:
    src = ROOT / "content" / md_name if lang == "en" else ROOT / "content" / "i18n" / lang / md_name
    raw = fill(src.read_text(encoding="utf-8"), where=str(src))
    visible = re.sub(r"<!--.*?-->", "", raw, flags=re.S)
    left = re.findall(r"\[[^\]]+\](?!\()", visible)
    if left:
        sys.exit(f"build error: unreplaced [bracket] placeholder(s) in {md_name}: {left}")
    title, body = markdown(raw, root, lang=lang)
    return title, body


# ---------- guide ----------
GUIDE = ROOT / "content" / "guide"
SEARCH_JS = r"""(function () {
  var menu = document.querySelector('.guide-menu');
  if (menu && window.matchMedia('(max-width: 52rem)').matches) menu.removeAttribute('open');
  var box = document.getElementById('guide-search'), out = document.getElementById('guide-results');
  if (!box || !out) return;
  var index = null;
  function load(cb) {
    if (index) return cb();
    fetch(box.dataset.index).then(function (r) { return r.json(); }).then(function (j) { index = j; cb(); });
  }
  function run() {
    var q = box.value.trim().toLowerCase();
    out.textContent = '';
    if (q.length < 2) return;
    var words = q.split(/\s+/);
    var hits = index.map(function (p) {
      var score = 0;
      words.forEach(function (w) {
        if (p.title.toLowerCase().indexOf(w) >= 0) score += 5;
        if (p.summary.toLowerCase().indexOf(w) >= 0) score += 2;
        if (p.text.indexOf(w) >= 0) score += 1; else score -= 100;
      });
      return { p: p, score: score };
    }).filter(function (h) { return h.score > 0; }).sort(function (a, b) { return b.score - a.score; }).slice(0, 12);
    if (!hits.length) { var li = document.createElement('li'); li.textContent = box.dataset.none || 'Nothing found. Try another word.'; out.appendChild(li); return; }
    hits.forEach(function (h) {
      var li = document.createElement('li'), a = document.createElement('a'), sm = document.createElement('span');
      a.href = box.dataset.root + h.p.url; a.textContent = h.p.title; sm.textContent = ' ' + h.p.summary; sm.className = 'small';
      li.appendChild(a); li.appendChild(sm); out.appendChild(li);
    });
  }
  box.addEventListener('input', function () { load(run); });
})();
"""


def front_matter(raw: str, where: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m:
        sys.exit(f"build error: {where} has no front matter")
    meta = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip()
    for need in ("title", "summary", "order"):
        if need not in meta:
            sys.exit(f"build error: {where} front matter lacks '{need}'")
    return meta, m.group(2)


def build_guide(lang: str = "en") -> None:
    """Render the guide for one language. English reads content/guide; another language reads content/i18n/<lang>/guide and builds only the pages that
    exist there. Screenshots: content/guide/img/<lang>/<file> when it exists, otherwise the English screenshot."""
    gdir = GUIDE if lang == "en" else i18n_src(lang, "guide")
    if not (gdir / "sections.json").exists():
        return
    C = CHROME[lang]
    app = CFG["app_name"]
    sections = json.loads((gdir / "sections.json").read_text(encoding="utf-8"))
    pages = []
    for sec in sections:
        d = gdir / sec["id"]
        if not d.exists():
            continue
        items = []
        for f in sorted(d.glob("*.md")):
            raw = fill(f.read_text(encoding="utf-8"), where=str(f.relative_to(ROOT)))
            meta, body = front_matter(raw, str(f.relative_to(ROOT)))
            left = re.findall(r"\[VERIFY[^\]]*\]|TODO|\[bracket\]", body)
            if left:
                sys.exit(f"build error: unresolved marker(s) {left} in {f.relative_to(ROOT)}")
            items.append((int(meta["order"]), f.stem, meta, body))
        items.sort(key=lambda x: (x[0], x[1]))
        for _, stem, meta, body in items:
            pages.append({"section": sec, "slug": stem, "meta": meta, "body": body, "rel": f"guide/{sec['id']}/{stem}/"})
    if not pages:
        return
    img_rel = url_for(lang, "guide/img/")

    def sidebar(current_rel: str, root: str) -> str:
        out = [f'<details class="guide-menu" open><summary>{C["browse"]}</summary>', '<div class="guide-nav" role="navigation" aria-label="' + C["guide"] + '">',
               f'<a class="guide-home" href="{root}{url_for(lang, "guide/")}">{C["all"]}</a>']
        for sec in sections:
            mine = [p for p in pages if p["section"]["id"] == sec["id"]]
            if not mine:
                continue
            open_ = " open" if any(p["rel"] == current_rel for p in mine) else ""
            out.append(f'<details{open_}><summary>{html.escape(sec["title"])}</summary><ul>')
            for p in mine:
                cur = ' aria-current="page"' if p["rel"] == current_rel else ""
                out.append(f'<li><a href="{root}{url_for(lang, p["rel"])}"{cur}>{html.escape(p["meta"]["title"])}</a></li>')
            out.append("</ul></details>")
        out.append("</div></details>")
        return "\n".join(out)

    index_rows = []
    for i, p in enumerate(pages):
        root = "../" * url_for(lang, p["rel"]).count("/")
        title, body_html = markdown(p["body"], root, img_root=root + img_rel, lang=lang)
        h2s = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body_html)
        toc = ""
        if len(h2s) > 2:
            toc = f'<div class="on-page" role="navigation" aria-label="{C["onpage"]}"><strong>{C["onpage"]}</strong><ul>' + "".join(f'<li><a href="#{a}">{b}</a></li>' for a, b in h2s) + "</ul></div>"
        prev_ = pages[i - 1] if i > 0 else None
        next_ = pages[i + 1] if i + 1 < len(pages) else None
        back, fwd = ("&rarr;", "&larr;") if LANGS[lang]["dir"] == "rtl" else ("&larr;", "&rarr;")
        pager = f'<div class="pager" role="navigation" aria-label="{C["prevnext"]}">'
        pager += f'<a rel="prev" href="{root}{url_for(lang, prev_["rel"])}">{back} {html.escape(prev_["meta"]["title"])}</a>' if prev_ else "<span></span>"
        pager += f'<a rel="next" href="{root}{url_for(lang, next_["rel"])}">{html.escape(next_["meta"]["title"])} {fwd}</a>' if next_ else "<span></span>"
        pager += "</div>"
        unclear = C["unclear"].format(email=f'<span class="email">{CFG["support_email"]}</span>')
        article = (f'<article class="prose guide-page"><p class="crumb"><a href="{root}{url_for(lang, "guide/")}">{C["guide"]}</a> &rsaquo; {html.escape(p["section"]["title"])}</p>'
                   f'<h1>{html.escape(p["meta"]["title"])}</h1><p class="lead-in">{inline(p["meta"]["summary"], root)}</p>{toc}{body_html}'
                   f'<p class="small">{unclear}</p>{pager}</article>')
        page_html = f'<div class="guide-layout">{sidebar(p["rel"], root)}{article}</div><script src="{root}guide/search.js" defer></script>'
        render(p["rel"], f"{p['meta']['title']} - {C['gsuffix'].format(app=app)}", p["meta"]["summary"], page_html, "guide", wide=True, lang=lang)
        plain = re.sub(r"<[^>]+>", " ", body_html)
        plain = re.sub(r"\s+", " ", html.unescape(plain)).lower()
        index_rows.append({"title": p["meta"]["title"], "summary": p["meta"]["summary"], "url": url_for(lang, p["rel"]), "text": plain})

    # the guide home
    root = "../" * url_for(lang, "guide/").count("/")
    cards = []
    for sec in sections:
        mine = [p for p in pages if p["section"]["id"] == sec["id"]]
        if not mine:
            continue
        lis = "".join(f'<li><a href="{root}{url_for(lang, p["rel"])}">{html.escape(p["meta"]["title"])}</a><span class="small"> {inline(p["meta"]["summary"], root)}</span></li>' for p in mine)
        cards.append(f'<section class="card guide-card" id="{sec["id"]}"><h2>{html.escape(sec["title"])}</h2><p class="small">{html.escape(sec.get("blurb", ""))}</p><ul class="guide-list">{lis}</ul></section>')
    home = (f'<article class="prose"><h1>{html.escape(C["gtitle"].format(app=app))}</h1><p class="lead-in">{html.escape(C["glead"].format(app=CFG["short_name"]))}</p>'
            f'<label class="search"><span>{C["search"]}</span><input id="guide-search" type="search" placeholder="{html.escape(C["ph"], quote=True)}" autocomplete="off" data-none="{html.escape(C["none"], quote=True)}" data-index="{root}{url_for(lang, "guide/")}search.json" data-root="{root}"></label>'
            f'<ul id="guide-results" class="results" aria-live="polite"></ul>{"".join(cards)}</article><script src="{root}guide/search.js" defer></script>')
    render("guide/", C["gpagetitle"].format(app=app), C["gdesc"].format(app=app), home, "guide", wide=True, lang=lang)
    out_guide = OUT / url_for(lang, "guide")
    out_guide.mkdir(parents=True, exist_ok=True)
    (out_guide / "search.json").write_text(json.dumps(index_rows, ensure_ascii=False), encoding="utf-8")
    if lang == "en":
        (out_guide / "search.js").write_text(SEARCH_JS, encoding="utf-8")
    # screenshots: the language's own where they exist, the English ones otherwise
    en_img, own_img = GUIDE / "img", GUIDE / "img" / lang
    dst = OUT / img_rel
    if en_img.exists():
        dst.mkdir(parents=True, exist_ok=True)
        for f in en_img.iterdir():
            if f.is_file():
                shutil.copy(f, dst / f.name)
        if lang != "en" and own_img.exists():
            for f in own_img.iterdir():
                if f.is_file():
                    shutil.copy(f, dst / f.name)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    app = CFG["app_name"]

    for lang in LANGS:
        C, L = CHROME[lang], LANGS[lang]
        if exists(lang, ""):
            render("", C["home_title"].format(app=app), C["home_desc"].format(app=app), fragment("index.html", "../" if lang != "en" else "./", lang), "", lang=lang)
        for key, md in (("privacy", "privacy.md"), ("terms", "terms.md")):
            if not exists(lang, key + "/"):
                continue
            root = "../" if lang == "en" else "../../"
            title, body = legal(md, root, lang)
            head = f'<h1>{html.escape(title)}</h1>'
            # the "Last updated" paragraph is the first <p>; give it a class for styling
            body = body.replace("<p>", '<p class="updated">', 1)
            desc = L["desc"][key].format(app=app)
            render(key + "/", f"{title} - {app}", desc, f'<article class="prose">\n{head}\n{body}\n</article>', key, lang=lang)
        if exists(lang, "support/"):
            render("support/", C["support_title"].format(app=app), C["support_desc"].format(app=app), fragment("support.html", "../" if lang == "en" else "../../", lang), "support", lang=lang)
        build_guide(lang)

    render("", f"Page not found - {app}", "This page does not exist.", fragment("404.html", "/"), path="404.html", root="/")

    # static files
    shutil.copy(ROOT / "static" / "style.css", OUT / "style.css")
    for name in ("favicon.ico", "favicon-32.png", "apple-touch-icon.png", "icon-192.png"):
        shutil.copy(ROOT / "assets" / name, OUT / name)
    host = CFG["site_url"].split("://", 1)[1].rstrip("/")
    (OUT / "CNAME").write_text(host + "\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    base = CFG["site_url"].rstrip("/")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n", encoding="utf-8")
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"<url><loc>{base}/{u}</loc><lastmod>{CFG['effective_date']}</lastmod></url>\n" for u in SITEMAP)
        + "</urlset>\n", encoding="utf-8")

    # loud warnings
    n = 0
    for f in sorted(OUT.rglob("*.html")):
        n += len(re.findall(r"TODO-OWNER", f.read_text(encoding="utf-8")))
    if not CFG.get("support_email_confirmed"):
        print("WARNING: support email is not confirmed (site.config.json: support_email_confirmed=false).")
    if not CFG.get("app_store_url"):
        print("NOTE: no App Store URL yet; the home page says 'Coming to the App Store' and shows no link.")
    print(f"built {sum(1 for _ in OUT.rglob('*') if _.is_file())} files into {OUT.name}/ ; {n} TODO-OWNER marker(s) left in the published HTML (should be 0)")


if __name__ == "__main__":
    main()
