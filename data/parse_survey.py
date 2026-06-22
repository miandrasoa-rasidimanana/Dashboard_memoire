#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parser bilingue (EN+FR) pour l'enquete Agilite Asynchrone.
Fusionne les blocs anglais (col 2-48) et francais (col 49-95) qui sont
parallels (offset = 47). Chaque repondant remplit UN seul bloc.
"""
import sys, json, math, re
import pandas as pd

def likert(v):
    """Extrait la valeur numerique 1-5 d'une reponse Likert (EN num ou FR texte)."""
    if v is None or (isinstance(v, float) and math.isnan(v)): return None
    s = str(v).strip()
    m = re.match(r'\s*([1-5])', s)
    return float(m.group(1)) if m else None

def num(v):
    if v is None or (isinstance(v, float) and math.isnan(v)): return None
    s = re.sub(r'[^0-9.\-]', '', str(v))
    try: return float(s) if s not in ('', '-', '.') else None
    except: return None

MODE_MAP = {
    'synchronous-first':'Synchrone-first','synchrone-first':'Synchrone-first',
    'hybrid':'Hybride','hybride':'Hybride',
    'asynchronous-first':'Asynchrone-first','asynchrone-first':'Asynchrone-first',
}
ROLE_MAP = {'other':'Autre','product':'Produit (PO/PM)','product (po/pm)':'Produit (PO/PM)',
            'dev':'Dev','data':'Data','design':'Design','rh':'RH','hr':'RH','ops-sre':'Ops-SRE'}

def norm(v, mp):
    if v is None or (isinstance(v,float) and math.isnan(v)): return None
    return mp.get(str(v).strip().lower(), str(v).strip())

def main(path):
    df = pd.read_csv(path)
    C = list(df.columns)
    def col(i): return C[i]
    # paires (EN_idx, FR_idx) decalage 47
    def coalesce(row, en_idx):
        a = row[col(en_idx)]; b = row[col(en_idx+47)]
        if a is not None and not (isinstance(a,float) and math.isnan(a)) and str(a).strip()!='':
            return a
        return b
    out = []
    excluded = 0
    for _, row in df.iterrows():
        elig = coalesce(row, 3); att = coalesce(row, 46); consent = coalesce(row, 2)
        elig_ok = str(elig).strip().lower() in ('yes','oui')
        att_ok  = str(att).strip().lower() in ('agree',"d'accord","d’accord")
        cons_ok = consent is not None and str(consent).strip()!='' and 'nan' not in str(consent).lower()
        if not (elig_ok and att_ok and cons_ok):
            excluded += 1; continue
        L = lambda i: likert(coalesce(row, i))
        aai_items  = [L(i) for i in range(14,20)]            # 14-19
        perf_items = [L(i) for i in range(20,25)]            # 20-24
        # CC: 25 briefs, 26 doc, 27 interruptions(REV), 28 decisions
        cc_raw = [L(25), L(26), L(27), L(28)]
        cc_items = [cc_raw[0], cc_raw[1], (6-cc_raw[2]) if cc_raw[2] else None, cc_raw[3]]
        # WB: 29 fatigue(R),30 stress(R),31 focus,32 balance,33 workload,34 control,35 pressure(R),36 breaks
        f=L(29); st=L(30); fo=L(31); ba=L(32); wl=L(33); co=L(34); pr=L(35); br=L(36)
        wb_items = [fo,ba,wl,co,br,(6-f) if f else None,(6-st) if st else None,(6-pr) if pr else None]
        inc_items  = [L(i) for i in range(37,46)]            # 37-45
        def mean(xs):
            v=[x for x in xs if x is not None]
            return round(sum(v)/len(v),2) if v else None
        rec = {
            'mode': norm(coalesce(row,10), MODE_MAP) or 'Autre',
            'role': norm(coalesce(row,4), ROLE_MAP) or 'Autre',
            'sector': (str(coalesce(row,7)).strip() if coalesce(row,7) is not None else 'Autre'),
            'team_size': str(int(num(coalesce(row,5)))) if num(coalesce(row,5)) is not None else '',
            'tenure': str(int(num(coalesce(row,6)))) if num(coalesce(row,6)) is not None else '',
            'timezone': str(coalesce(row,8)).strip() if coalesce(row,8) is not None else '',
            'remote_days': str(int(num(coalesce(row,9)))) if num(coalesce(row,9)) is not None else '',
            'meeting_hours': num(coalesce(row,11)),
            'meeting_pct': num(coalesce(row,12)),
            'meetings_harm': L(13),
            'aai': mean(aai_items),
            'perf': mean(perf_items),
            'wb': mean(wb_items),
            'inc': mean(inc_items),
            'cc': mean(cc_items),
            'open_pos': str(coalesce(row,47)).strip() if coalesce(row,47) is not None and str(coalesce(row,47)).strip().lower()!='nan' else '',
            'open_neg': str(coalesce(row,48)).strip() if coalesce(row,48) is not None and str(coalesce(row,48)).strip().lower()!='nan' else '',
        }
        out.append(rec)
    print(f"VALIDES={len(out)} EXCLUS={excluded}", file=sys.stderr)
    return out

if __name__ == '__main__':
    data = main(sys.argv[1])
    print(json.dumps(data, ensure_ascii=False))
