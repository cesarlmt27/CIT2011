import sqlite3
import re
import json
import sys

def load_index(file):
    index = {}
    with open(file, 'r') as f:
        for line in f:
            word, docs = line.strip().split('\t')
            docs = re.findall(r'\((\d+), (\d+)\)', docs)
            docs = [(int(doc), int(count)) for doc, count in docs]
            index[word] = docs
    return index

def get_url(doc_id, conn):
    cur = conn.cursor()
    cur.execute("SELECT url FROM documento WHERE documento=?", (doc_id,))
    result = cur.fetchone()
    return result[0] if result else None

def search(word, index, conn):
    if word in index:
        docs = index[word]
        docs.sort(key=lambda x: x[1], reverse=True)
        results = []
        for doc, count in docs[:5]:
            url = get_url(doc, conn)
            results.append({"Documento": doc, "Frecuencia": count, "url": url})
        return {word: results}
    else:
        return {}

conn = sqlite3.connect('../database.db')
index = load_index('outhadoop/part-00000')

# Utilizar el primer argumento de la línea de comando como palabra de búsqueda
search_word = sys.argv[1]
results = search(search_word, index, conn)

# Imprimir resultado en formato JSON
print(json.dumps(results, indent=4))

conn.close()