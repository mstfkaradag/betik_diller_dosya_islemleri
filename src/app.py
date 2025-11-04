from dosya_islemleri import read_csv, write_json,write_text
from processing import clean_data, stats,build_report
def main():
    read_doc="data/people.csv"
    write_doc="data/stats.json"
    write_txt="data/stats_txt.txt"

    #Oku
    try:
        rows=read_csv(read_doc)
        cleaned_rows = clean_data(rows)
        st=stats(cleaned_rows)

        write_json(write_doc,st)
        write_text(write_txt,build_report(st))
        print("bitti")
    except Exception as e:
        print(f"Hata: {str(e)}")

if __name__=="__main__":
    main()