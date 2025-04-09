# 📘 Relatório Comparativo de Algoritmos de Busca em Texto  
## Obras: *Dom Casmurro* (Machado de Assis) e *Peter Pan* (J.M. Barrie)

---

## 📌 Introdução

Este relatório apresenta uma análise comparativa entre dois algoritmos de busca textual — **Busca Ingênua** (Naive Search) e **Rabin-Karp** — aplicados a dois livros clássicos da literatura.

### Objetivos:
- ✔️ Comparar o desempenho de cada algoritmo em diferentes obras.
- ✔️ Avaliar a influência do tamanho do padrão de busca nos resultados.
- ✔️ Verificar a consistência dos métodos implementados.

---

## 📋 Metodologia

### 📚 Obras Utilizadas

| Livro         | Autor            | Tamanho (aprox.) | Fonte               |
|---------------|------------------|------------------|---------------------|
| Dom Casmurro  | Machado de Assis | ~350 KB          | Project Gutenberg   |
| Peter Pan     | J.M. Barrie      | ~200 KB          | Project Gutenberg   |

### 🔍 Padrões de Busca

- **Dom Casmurro:** `"Bentinho"` (personagem principal)
- **Peter Pan:** `"Peter Pan"` (nome do protagonista)

### ⚙️ Algoritmos Testados

- **Busca Ingênua:** Comparação caractere a caractere (`O(n·m)`).
- **Rabin-Karp:** Utiliza hash para acelerar a busca (`O(n + m)` em média).

### 🖥️ Ambiente de Execução

- **Sistema Operacional:** Windows 10/11  
- **Linguagem:** Python 3.8+  
- **Hardware:** Processador moderno Intel/AMD  
- **Medição de tempo:** `time.time()`

---

## 📊 Resultados

### 🔎 Resultados por Livro

#### 📖 Dom Casmurro — Padrão: `"Bentinho"`  
- Ocorrências encontradas: `57`  
- Tempo Busca Ingênua: `0.08249 s`  
- Tempo Rabin-Karp: `0.09761 s` ➕ **+18.4% mais lento**  
- Consistência de resultados: ✅

#### 📖 Peter Pan — Padrão: `"Peter Pan"`  
- Ocorrências encontradas: `20`  
- Tempo Busca Ingênua: `0.08077 s`  
- Tempo Rabin-Karp: `0.09842 s` ➕ **+21.8% mais lento**  
- Consistência de resultados: ✅

### 📊 Tabela Comparativa

| Livro / Padrão          | Ocorrências | Tempo Naive (s) | Tempo RK (s) | Diferença (%)     | Consistência |
|-------------------------|-------------|-----------------|--------------|-------------------|--------------|
| Dom Casmurro / Bentinho | 57          | 0.08249         | 0.09761      | +18.4% (mais lento) | ✅ Sim       |
| Peter Pan / Peter Pan   | 20          | 0.08077         | 0.09842      | +21.8% (mais lento) | ✅ Sim       |

---

## 📌 Análise dos Resultados

### ✅ Eficiência Prática
Apesar da vantagem teórica do Rabin-Karp em grandes volumes de dados, a **Busca Ingênua foi mais rápida** nos dois casos analisados. Isso se deve, possivelmente, ao overhead da função de hash, que se torna irrelevante quando o padrão é pequeno e o texto moderado.

### ✅ Frequência de Ocorrência
- `"Bentinho"` foi mencionado **57 vezes** — personagem central em *Dom Casmurro*.
- `"Peter Pan"` apareceu **20 vezes** — menos frequente do que o título poderia sugerir.

### ✅ Consistência dos Resultados
Ambos os algoritmos retornaram o **mesmo número de ocorrências**, o que confirma a **correção das implementações**.

---

## 🔎 Conclusões

- A **Busca Ingênua se mostrou superior em desempenho** para textos de até 350 KB com padrões curtos (~8-9 caracteres).
- O **Rabin-Karp** não demonstrou sua vantagem teórica nestes cenários, provavelmente devido ao custo de processamento de hash em padrões pequenos.
- **Recomendações para estudos futuros:**
  - Testar com textos maiores (>1MB), como *War and Peace*.
  - Avaliar padrões mais longos, como frases completas.
  - Incluir o algoritmo **Boyer-Moore** para ampliar a comparação.

---

📌 **Resumo Final:**  
A simplicidade da Busca Ingênua pode ser mais eficiente que algoritmos sofisticados em determinados contextos. A escolha do algoritmo ideal depende diretamente do **tamanho do texto**, do **padrão** e dos **requisitos de tempo** da aplicação.

## 👨‍💻 Desenvolvedores

<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/humberto-peres"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/118866895?s=400&u=a12412e21705d58ab604be67c1e1431c80174b64&v=4" width="100px;" alt=""/><br /><sub><b>Humberto Peres</b></sub></a><br /><a href="https://rocketseat.com.br/" title="Rocketseat">👨‍🚀</a></td>
    <td align="center"><a href="https://github.com/WesllyHn"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/117309594?v=4" width="100px;" alt=""/><br /><sub><b>Weslly Hendler Neres</b></sub></a><br /><a href="https://rocketseat.com.br/" title="Rocketseat">🚀</a></td>

