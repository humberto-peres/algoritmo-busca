import time
import os

def naive_search(text, pattern):
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        match = True
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences

def rabin_karp_search(text, pattern, prime=101):
    m = len(pattern)
    n = len(text)
    d = 256
    h = pow(d, m - 1) % prime
    p = 0
    t = 0
    occurrences = []

    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    for s in range(n - m + 1):
        if p == t:
            if text[s:s + m] == pattern:
                occurrences.append(s)
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % prime
            if t < 0:
                t += prime
    return occurrences

def obter_titulo(caminho):
    try:
        with open(caminho, encoding="utf-8") as f:
            for _ in range(20):
                linha = f.readline()
                if linha.lower().startswith("title:"):
                    return linha.strip().split(":", 1)[1].strip()
    except Exception:
        pass
    return "Título desconhecido"

livros_disponiveis = {
    "1": "PeterPan.txt",
    "2": "domCasmurro.txt"
}

print("📚 Livros disponíveis:")
for k, v in livros_disponiveis.items():
    print(f"{k}. {v}")

escolha = input("\nDigite o número do livro que deseja usar: ").strip()

if escolha not in livros_disponiveis:
    print("❌ Opção inválida. Encerrando.")
    exit()

caminho_livro = livros_disponiveis[escolha]

if not os.path.exists(caminho_livro):
    print(f"❌ Arquivo '{caminho_livro}' não encontrado.")
    exit()

with open(caminho_livro, encoding="utf-8") as file:
    texto = file.read()

titulo = obter_titulo(caminho_livro)

trecho = input("\nDigite a palavra ou frase que deseja buscar: ").strip()

if not trecho:
    print("❌ Nenhum trecho informado. Encerrando.")
    exit()

inicio_naive = time.time()
result_naive = naive_search(texto, trecho)
fim_naive = time.time()

inicio_rk = time.time()
result_rk = rabin_karp_search(texto, trecho)
fim_rk = time.time()

print(f"\n📖 Livro: {titulo} ({caminho_livro})")
print(f"🔍 Trecho buscado: '{trecho}'")
print("="*40)
print(f"\n📌 Naive Search:")
print(f"- Ocorrências: {len(result_naive)}")
print(f"- Tempo: {fim_naive - inicio_naive:.6f} segundos")

print(f"\n⚡ Rabin-Karp Search:")
print(f"- Ocorrências: {len(result_rk)}")
print(f"- Tempo: {fim_rk - inicio_rk:.6f} segundos")

print(f"\n✅ Os resultados são iguais? {'Sim' if result_naive == result_rk else 'Não'}")
