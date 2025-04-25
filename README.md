# Exercicio-de-Programacao-3-Python 🚀

Terceiro Exercício Programa (EP3) desenvolvido para a disciplina **MAC2166 – Introdução à Computação** da Escola Politécnica, Universidade de São Paulo. Este programa implementa o modelo epidemiológico SIR 🦠 e métodos auxiliares para análise crítica e geração de gráficos simples (PGM) 🖼️ e compostos (PPM) 🎨.

## Índice 📑
- Descrição 📝  
- Pré-requisitos ⚙️  
- Estrutura do Projeto 🗂️  
- Instalação 🔧  
- Uso (modos 1 a 7) 🚀  
- Exemplos de Execução 💻  
- Detalhes das Funções 🔍  
- Licença 📜  

## Descrição 📝
Este programa permite:
1. Calcular as curvas de suscetíveis (S), infectados (I) e removidos (R) do modelo SIR;  
2. Determinar o pico de infectados (`critic_SIR`) variando o parâmetro de transmissão β;  
3. Gerar gráficos simples (formato **PGM**) e compostos (formato **PPM**) das curvas resultantes.  

## Pré-requisitos ⚙️
- **Python 3.6** ou superior  
- Nenhuma biblioteca externa além da padrão do Python  

## Estrutura do Projeto 🗂️
```
├── EP3.py             # Código-fonte principal
├── dados1.txt         # Arquivos de entrada (6 linhas)
├── dados2.txt
├── dados3.txt
├── dados4.txt
├── dados5.txt
├── graf_simples.pgm   # Saída dos modos 4 e 5
├── graf_composto.ppm  # Saída dos modos 6 e 7
└── LICENSE            # Licença MIT
```

## Instalação 🔧
Clone o repositório e entre na pasta do projeto:
```bash
git clone https://github.com/rafael-agra/Exercicio-de-Programacao-3-Python.git
cd Exercicio-de-Programacao-3-Python
```
Verifique a versão do Python:
```bash
python --version
```

## Uso 🚀
Execute o programa:
```bash
python EP3.py
```
Você será solicitado a digitar o **modo** (1 a 7). Dependendo do modo, insira parâmetros pelo teclado ou indique um arquivo `.txt`.

### Modos disponíveis
- **Modo 1** – SIR via teclado: entrada `N β γ Tmax`; saída listas S, I, R.  
- **Modo 2** – `critic_SIR` via teclado: entrada `N γ Tmax β_MIN β_MAX β_delta`; saída picos de infectados.  
- **Modo 3** – `critic_SIR` via arquivo: arquivo com 6 linhas conforme acima; saída picos de infectados.  
- **Modo 4** – Gráfico simples PGM no console.  
- **Modo 5** – Gráfico simples PGM salvo como `graf_simples.pgm`.  
- **Modo 6** – Gráfico composto PPM no console.  
- **Modo 7** – Gráfico composto PPM salvo como `graf_composto.ppm`.  

## Exemplos de Execução 💻

### Modo 1
```
Digite modo do programa: 1
Digite N: 1000
Digite Beta: 0.2
Digite Gama: 0.05
Digite Tmax: 30
S = 999.0000 998.8000 …
I =   1.0000   1.1800 …
R =   0.0000   0.0200 …
```

### Modo 3 (arquivo `dados1.txt`)
```
Digite modo do programa: 3
Digite nome do arquivo: dados1.txt
4.0000 5.2000 6.4000 …
```

## Detalhes das Funções 🔍
- **SIR(N, β, γ, Tmax)** – devolve listas S, I e R.  
- **critic_SIR(N, γ, Tmax, β_MIN, β_MAX, β_delta)** – devolve lista de picos de infectados.  
- **gera_grafico_simples(L)** – monta matriz PGM a partir de `L`.  
- **gera_grafico_composto(S, I, R)** – monta matriz PPM com as três curvas.  
- **leitura_de_valores(arquivo)** – lê parâmetros de arquivo-texto (6 linhas).  
- **imprimeLista(L)** – imprime lista com 4 casas decimais.  

## Licença 📜
Distribuído sob a licença **MIT** – consulte o arquivo `LICENSE` para detalhes.

