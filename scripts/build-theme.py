# -*- coding: utf-8 -*-
"""Build the Claret Atelier Light / Dark color themes from one palette table.

    py -3 scripts/build-theme.py
"""

import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
THEMES = BASE / "themes"
NAME = "claret-atelier-theme"
SLUG = "claret-atelier"
DISPLAY = "Claret Atelier Theme"
VERSION = "1.0.0"
REPO = "https://github.com/vaxicy/claret-atelier-theme"

UI = {
    "foreground": ("#3A2A30", "#EFE3D6"),
    "editor.foreground": ("#3A2A30", "#EFE3D6"),
    "terminal.foreground": ("#3A2A30", "#EFE3D6"),
    "input.foreground": ("#33232A", "#F5EDE3"),
    "dropdown.foreground": ("#33232A", "#F5EDE3"),
    "quickInput.foreground": ("#33232A", "#F5EDE3"),
    "editorWidget.foreground": ("#33232A", "#F5EDE3"),
    "editorHoverWidget.foreground": ("#33232A", "#F5EDE3"),
    "editorSuggestWidget.foreground": ("#33232A", "#F5EDE3"),
    "notifications.foreground": ("#33232A", "#F5EDE3"),
    "descriptionForeground": ("#8C7A80", "#A09098"),
    "input.placeholderForeground": ("#8C7A80", "#A09098"),
    "focusBorder": ("#8A1A2C", "#D8BC8C"),
    "inputOption.activeBorder": ("#5A0F1E", "#EBD3A6"),
    "input.border": ("#E4D9C6", "#45303A"),
    "dropdown.border": ("#E4D9C6", "#45303A"),
    "editor.background": ("#FAF6EE", "#241318"),
    "tab.activeBackground": ("#FAF6EE", "#241318"),
    "titleBar.activeBackground": ("#F7EDDB", "#1B0D11"),
    "titleBar.activeForeground": ("#4A3038", "#E3D5C6"),
    "titleBar.inactiveBackground": ("#F4EADB", "#170B0E"),
    "titleBar.inactiveForeground": ("#9A888E", "#8C7A82"),
    "activityBar.background": ("#F1E3CC", "#180C10"),
    "activityBar.foreground": ("#5A0F1E", "#C98A92"),
    "activityBar.activeBorder": ("#5A0F1E", "#D8BC8C"),
    "activityBar.inactiveForeground": ("#A8917E", "#6E5860"),
    "sideBar.background": ("#F7F1E6", "#2A161B"),
    "sideBar.foreground": ("#4A3038", "#DCC9BF"),
    "sideBarSectionHeader.background": ("#EFE3CC", "#331B21"),
    "sideBarSectionHeader.foreground": ("#5A3A42", "#E5D2C8"),
    "panel.background": ("#F9F3E9", "#201115"),
    "terminal.background": ("#F9F3E9", "#201115"),
    "panel.border": ("#E7DCC9", "#402630"),
    "editorGroup.border": ("#E7DCC9", "#402630"),
    "tab.border": ("#E7DCC9", "#402630"),
    "sideBar.border": ("#E7DCC9", "#402630"),
    "titleBar.border": ("#E7DCC9", "#402630"),
    "statusBar.background": ("#5A0F1E", "#6E1524"),
    "statusBar.noFolderBackground": ("#5A0F1E", "#6E1524"),
    "statusBar.foreground": ("#F5EFE1", "#F0E4D6"),
    "statusBar.noFolderForeground": ("#F5EFE1", "#F0E4D6"),
    "statusBarItem.hoverBackground": ("#6E1524", "#84202F"),
    "statusBar.debuggingBackground": ("#9A6A18", "#B07A20"),
    "statusBar.debuggingForeground": ("#FAF6EE", "#FFF8EC"),
    "editorGroupHeader.tabsBackground": ("#F2E8D6", "#1E1014"),
    "tab.inactiveBackground": ("#F2E8D6", "#1E1014"),
    "tab.activeForeground": ("#3A2A30", "#F2E6DA"),
    "tab.activeBorderTop": ("#8A1A2C", "#D8BC8C"),
    "tab.inactiveForeground": ("#8C7A80", "#8A737C"),
    "tab.hoverBackground": ("#EADCC4", "#331B21"),
    "tab.activeModifiedBorder": ("#8A6A24", "#E8CE92"),
    "tab.inactiveModifiedBorder": ("#8A6A24", "#E8CE92"),
    "list.hoverBackground": ("#F0E6D4", "#3A2027"),
    "list.activeSelectionBackground": ("#E7D3BA", "#4E2129"),
    "editorSuggestWidget.selectedBackground": ("#E7D3BA", "#4E2129"),
    "list.activeSelectionForeground": ("#33232A", "#F3E4D6"),
    "list.inactiveSelectionForeground": ("#33232A", "#F3E4D6"),
    "editorSuggestWidget.selectedForeground": ("#33232A", "#F3E4D6"),
    "list.inactiveSelectionBackground": ("#EFE0C9", "#402028"),
    "list.highlightForeground": ("#5A0F1E", "#E0B9C0"),
    "list.focusHighlightForeground": ("#5A0F1E", "#E0B9C0"),
    "tree.indentGuidesStroke": ("#E2D6C1", "#3C242B"),
    "editorLineNumber.foreground": ("#B0A090", "#6E5860"),
    "editorLineNumber.activeForeground": ("#8A1A2C", "#D8BC8C"),
    "editor.lineHighlightBackground": ("#F4EDE0", "#301820"),
    "editor.lineHighlightBorder": ("#EFE2CC", "#3A2129"),
    "editorCursor.foreground": ("#8A1A2C", "#D8BC8C"),
    "selection.background": ("#E7D3BA", "#4E2129"),
    "editor.selectionBackground": ("#E7D3BA", "#4E2129"),
    "terminal.selectionBackground": ("#E7D3BA", "#4E2129"),
    "editor.inactiveSelectionBackground": ("#EFE0C9", "#402028"),
    "editor.wordHighlightBackground": ("#E7D3BA80", "#5A2A3399"),
    "editor.wordHighlightStrongBackground": ("#E7D3BA80", "#5A2A3399"),
    "editor.selectionHighlightBackground": ("#E7D3BA66", "#5A2A3388"),
    "editor.findMatchHighlightBackground": ("#F0DCB8", "#5A3540"),
    "editor.findMatchBackground": ("#E8C88E", "#74454F"),
    "editor.findMatchBorder": ("#8A1A2C", "#E8CE92"),
    "editorBracketMatch.background": ("#F0E4CD", "#3A2027"),
    "editorBracketMatch.border": ("#8A1A2C", "#D8BC8C"),
    "editorIndentGuide.background1": ("#E8DCC7", "#362026"),
    "editorIndentGuide.activeBackground1": ("#A8917E", "#5C444C"),
    "editorWhitespace.foreground": ("#E8DCC7", "#362026"),
    "editorRuler.foreground": ("#EFE6D6", "#322028"),
    "textLink.foreground": ("#5A0F1E", "#E0B9C0"),
    "textLink.activeForeground": ("#8A1A2C", "#F0D2D6"),
    "editorLink.activeForeground": ("#8A1A2C", "#F0D2D6"),
    "quickInput.background": ("#FDFAF4", "#2C171C"),
    "editorHoverWidget.background": ("#FDFAF4", "#2C171C"),
    "notifications.background": ("#FDFAF4", "#2C171C"),
    "input.background": ("#FEFCF7", "#241318"),
    "dropdown.background": ("#FEFCF7", "#241318"),
    "editorWidget.background": ("#FDFAF4", "#2C171C"),
    "editorSuggestWidget.background": ("#FDFAF4", "#2C171C"),
    "editorWidget.border": ("#E7DCC9", "#4A2E36"),
    "editorHoverWidget.border": ("#E7DCC9", "#4A2E36"),
    "editorSuggestWidget.border": ("#E7DCC9", "#4A2E36"),
    "notifications.border": ("#E7DCC9", "#4A2E36"),
    "button.background": ("#8A1A2C", "#D8BC8C"),
    "button.foreground": ("#FAF6EE", "#2A1218"),
    "button.hoverBackground": ("#A02436", "#EBD3A6"),
    "button.secondaryBackground": ("#EFE3CC", "#3A2027"),
    "button.secondaryForeground": ("#4A3038", "#E2D2C8"),
    "button.secondaryHoverBackground": ("#E6D5B8", "#4A2E36"),
    "badge.background": ("#5A0F1E", "#8A1A2C"),
    "activityBarBadge.background": ("#5A0F1E", "#8A1A2C"),
    "badge.foreground": ("#F5EFE1", "#F5EFE1"),
    "activityBarBadge.foreground": ("#F5EFE1", "#F5EFE1"),
    "scrollbarSlider.background": ("#A8917E66", "#7A606888"),
    "scrollbarSlider.hoverBackground": ("#8C746688", "#96808899"),
    "scrollbarSlider.activeBackground": ("#5A0F1E99", "#C9A9B299"),
    "errorForeground": ("#B3414B", "#F0929A"),
    "editorError.foreground": ("#B3414B", "#F0929A"),
    "problemsErrorIcon.foreground": ("#B3414B", "#F0929A"),
    "gitDecoration.deletedResourceForeground": ("#B3414B", "#F0929A"),
    "editorGutter.deletedBackground": ("#B3414B", "#F0929A"),
    "editorWarning.foreground": ("#9A6A18", "#E8C86E"),
    "problemsWarningIcon.foreground": ("#9A6A18", "#E8C86E"),
    "editorInfo.foreground": ("#3F6B84", "#9CC3DC"),
    "problemsInfoIcon.foreground": ("#3F6B84", "#9CC3DC"),
    "gitDecoration.addedResourceForeground": ("#3E7A52", "#8FC9A0"),
    "gitDecoration.untrackedResourceForeground": ("#3E7A52", "#8FC9A0"),
    "editorGutter.addedBackground": ("#3E7A52", "#8FC9A0"),
    "gitDecoration.modifiedResourceForeground": ("#9A6A18", "#E8C86E"),
    "editorGutter.modifiedBackground": ("#9A6A18", "#E8C86E"),
    "diffEditor.insertedTextBackground": ("#CFE4D5AA", "#2E4A3A66"),
    "diffEditor.removedTextBackground": ("#F2D5D8AA", "#5A2A3366"),
    "diffEditor.insertedLineBackground": ("#CFE4D566", "#2E4A3A44"),
    "diffEditor.removedLineBackground": ("#F2D5D866", "#5A2A3344"),
    "terminal.ansiBlack": ("#3A2A30", "#2A161B"),
    "terminal.ansiRed": ("#B3414B", "#F0929A"),
    "terminal.ansiGreen": ("#3E7A52", "#8FC9A0"),
    "terminal.ansiYellow": ("#9A6A18", "#E8C86E"),
    "terminal.ansiBlue": ("#3F6B84", "#9CC3DC"),
    "terminal.ansiMagenta": ("#7A4A78", "#D4AED2"),
    "terminal.ansiCyan": ("#2E6E6A", "#8FD0CB"),
    "terminal.ansiWhite": ("#8C7A80", "#D8C8CC"),
    "terminal.ansiBrightBlack": ("#6E5860", "#6E5860"),
    "terminal.ansiBrightRed": ("#CC5B64", "#F5B0B6"),
    "terminal.ansiBrightGreen": ("#5E9A6E", "#A9DDB8"),
    "terminal.ansiBrightYellow": ("#BC8C2E", "#F2D89A"),
    "terminal.ansiBrightBlue": ("#5A86A0", "#B0D2E6"),
    "terminal.ansiBrightMagenta": ("#9A6A98", "#E4C6E2"),
    "terminal.ansiBrightCyan": ("#3E8E88", "#A8E0DC"),
    "terminal.ansiBrightWhite": ("#33232A", "#F3E4D6"),
}

TOKENS = [
    ("comment", ("#9C8A7E", "#8E7A6E"), "italic"),
    (("keyword", "storage"), ("#8A1A2C", "#E48A92"), None),
    ("string", ("#8F6B2A", "#E8CE92"), None),
    (("entity.name.function", "support.function"), ("#3F6B84", "#9CC3DC"), None),
    (("entity.name.type", "support.type", "support.class"), ("#5F4A6E", "#BCA7CC"), None),
    (("constant.numeric", "constant.language", "variable.other.constant"), ("#8A6A24", "#E8CE92"), None),
    ("variable", ("#3A2A30", "#EFE3D6"), None),
    ("variable.parameter", ("#6E5A60", "#C3B2BA"), None),
    (("variable.other.property", "support.variable.property"), ("#6B4A55", "#C9A8B4"), None),
    ("keyword.operator", ("#8A7A80", "#A8969E"), None),
    ("punctuation", ("#9C8A90", "#8E7A82"), None),
    ("entity.name.tag", ("#8A1A2C", "#E48A92"), None),
    ("entity.other.attribute-name", ("#8A6A24", "#E8CE92"), None),
    ("string.regexp", ("#A65A32", "#E8A87C"), None),
    ("constant.character.escape", ("#8A6A24", "#E8CE92"), None),
    ("markup.heading", ("#2E1A20", "#F5EFE1"), "bold"),
    ("markup.bold", ("#2E1A20", "#F5EFE1"), "bold"),
    ("markup.italic", ("#2E1A20", "#F5EFE1"), "italic"),
    ("invalid", ("#B3414B", "#F0929A"), None),
]

SEMANTIC = {
    "variable": "#3A2A30|#EFE3D6",
    "parameter": "#6E5A60|#C3B2BA",
    "property": "#6B4A55|#C9A8B4",
    "function": "#3F6B84|#9CC3DC",
    "method": "#3F6B84|#9CC3DC",
    "type": "#5F4A6E|#BCA7CC",
    "class": "#5F4A6E|#BCA7CC",
    "interface": "#5F4A6E|#BCA7CC",
    "variable.readonly": "#8A6A24|#E8CE92",
}

PACKAGE = {
    "name": NAME,
    "displayName": DISPLAY,
    "description": "A painter's studio palette: deep claret, warm brass and paper white in the light variant, a candlelit pigment room at night in the dark one.",
    "version": VERSION,
    "publisher": "lilinhuang",
    "engines": {"vscode": "^1.80.0"},
    "categories": ["Themes"],
    "keywords": ["theme", "light", "dark", "claret", "atelier", "wine", "brass", "warm"],
    "icon": "assets/icon.png",
    "license": "SEE LICENSE IN LICENSE",
    "galleryBanner": {"color": "#241318", "theme": "dark"},
    "repository": {"type": "git", "url": REPO},
    "contributes": {
        "themes": [
            {"label": f"{DISPLAY} Light", "uiTheme": "vs",
             "path": f"./themes/{SLUG}-light-color-theme.json"},
            {"label": f"{DISPLAY} Dark", "uiTheme": "vs-dark",
             "path": f"./themes/{SLUG}-dark-color-theme.json"},
        ]
    },
}


def build(variant, index):
    colors = {key: pair[index] for key, pair in UI.items()}
    tokens = []
    for scope, pair, style in TOKENS:
        settings = {"foreground": pair[index]}
        if style:
            settings["fontStyle"] = style
        tokens.append({"scope": [scope] if isinstance(scope, str) else list(scope),
                       "settings": settings})
    theme = {
        "name": f"{DISPLAY} {variant.title()}",
        "type": variant,
        "colors": colors,
        "semanticHighlighting": True,
        "semanticTokenColors": {k: v.split("|")[index] for k, v in SEMANTIC.items()},
        "tokenColors": tokens,
    }
    out = THEMES / f"{SLUG}-{variant}-color-theme.json"
    out.write_text(json.dumps(theme, indent=2) + "\n", encoding="utf-8")
    print("wrote", out.relative_to(BASE), len(colors), "UI colors")


def main():
    THEMES.mkdir(exist_ok=True)
    for index, variant in enumerate(("light", "dark")):
        build(variant, index)
    (BASE / "package.json").write_text(json.dumps(PACKAGE, indent=2) + "\n", encoding="utf-8")
    print("wrote package.json")


if __name__ == "__main__":
    main()
