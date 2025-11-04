def clean_data(rows):
    cleaned = []
    for row in rows:
        if row['age']:
            age = row['age'].strip()
        else:
            age = ''
        if not age or not age.isdigit():
            continue

        cleaned_row = {
            'name': row['name'].strip(),
            'age': int(age),
            'city': row['city'].strip()
        }
        cleaned.append(cleaned_row)
    return cleaned

def stats (rows: list[dict]) ->dict:
    if not rows:
        return {"count":0, "avg_age":0,"by_city": {}}
    ages=[r["age"] for r in rows] 
    by_city={}
    for r in rows:
        city = r["city"]
        by_city[city]=by_city.get(city,0) +1
    return {"count": len(rows), "avg_age":sum(ages)/len(rows), "by_city": by_city}

def build_report(st:dict)->str:
    lines=[]
    lines.append("Rapor")
    lines.append("")
    lines.append(f"Geçerli kayıt sayısı: {st["count"]}")
    lines.append(f"ortalama yaş: {st["avg_age"]}")
    lines.append("Şehir dağılımı:")
    for c,n in st["by_city"].items():
        lines.append(f"{c}: {n}")
    return  "\n".join(lines) +"\n"
