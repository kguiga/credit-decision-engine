# 💳 Credit Decision Engine

## 📖 Descrição

Motor de decisão de crédito desenvolvido em Python com o objetivo de simular o processo de avaliação de propostas de crédito por meio de regras de negócio.

O projeto foi inspirado em motores de decisão utilizados no mercado financeiro, aplicando conceitos de análise de crédito, cálculo de score consolidado (blend score), validação de políticas e geração de decisões explicáveis.

O sistema recebe informações de um cliente, avalia regras de recusa e derivação e retorna uma decisão estruturada contendo o resultado da análise e os motivos que levaram à decisão.

---

## 🎯 Objetivos

- Simular um motor de decisão de crédito baseado em regras.
- Aplicar conceitos de modelagem de domínio.
- Implementar políticas de crédito reutilizáveis.
- Produzir decisões explicáveis através do registro das regras acionadas.
- Servir como base para futuras evoluções utilizando API REST, PostgreSQL e Docker.

---

## 🛠️ Tecnologias Atuais

- Python
- Programação Orientada a Objetos
- Regras de Negócio

## 🚀 Tecnologias Planejadas

- Pytest
- PostgreSQL
- FastAPI
- Docker

---

## 🏗️ Domínio

### Cliente

Informações utilizadas na análise:

```text
nome
idade
renda

score_bvs
score_serasa
score_quod
```

---

### Política

Responsável pela avaliação da proposta e aplicação das regras de crédito.

---

### Decisão

Resultado da análise realizada pelo motor.

Possíveis resultados:

```text
APROVADO
DERIVADO
RECUSADO
```

---

## 📋 Resumo das Decisões

| Cenário | Resultado |
|----------|----------|
| Qualquer regra de recusa acionada | RECUSADO |
| Nenhuma recusa e alguma derivação | DERIVADO |
| Nenhuma regra acionada | APROVADO |

---

## 📊 Cálculo do Score Blend

O Score Blend representa a consolidação dos bureaus de crédito.

### Observação

O Score Blend somente será calculado quando existirem pelo menos dois scores válidos.

Caso menos de dois scores estejam disponíveis, o Score Blend será considerado nulo.

### Regra

```text
1. Selecionar os três scores disponíveis (não nulos):
   - BVS
   - Serasa
   - Quod

2. Ordenar os scores em ordem decrescente

3. Selecionar os dois maiores valores

4. Somar os dois maiores scores

5. Dividir o resultado por 2
```

### Exemplo

```text
BVS:    400
SERASA: 700
QUOD:   800
```

```text
(800 + 700) / 2 = 750
```

```text
Score Blend = 750
```

---

## ℹ️ Tratamento dos Scores

Neste projeto existe diferença entre:

- Valor 0 → score recebido com valor zero.
- Valor nulo (None) → score não informado.

Esses cenários acionam regras distintas durante a análise de crédito.

---

## 🚫 Regras de Recusa

### NOME_AUSENTE

```text
Nome não informado.
```

---

### IDADE_INVALIDA

```text
Idade menor que 18 anos
ou
Idade maior que 80 anos.
```

---

### SCORES_INSUFICIENTES

```text
Dois dos três scores possuem valor 0.
```

---

### RENDA_INVALIDA

```text
Renda menor ou igual a 0.
```

---

### SCORE_BLEND_BAIXO

```text
Score Blend menor que 500.
```

---

### RENDA_INSUFICIENTE

```text
Score Blend entre 500 e 699
e
Renda inferior a 7000.
```

---

## ⚠️ Regras de Derivação

### SCORE_NULO

```text
Dois dos três scores não foram informados.
```

---

### SCORE_BLEND_MEDIO_COM_RENDA

```text
Score Blend entre 500 e 699
e
Renda igual ou superior a 7000.
```

Nesse cenário a proposta deve ser encaminhada para análise manual.

---

## 🔀 Hierarquia de Decisão

O motor utiliza a seguinte ordem de prioridade:

```text
RECUSADO
   ↓
DERIVADO
   ↓
APROVADO
```

### Observação

O resultado final segue a hierarquia:

RECUSADO > DERIVADO > APROVADO

Entretanto, todos os motivos encontrados durante a análise serão registrados na resposta, independentemente do resultado final.


### Regras

```text
Se existir qualquer regra de recusa:
→ RECUSADO

Se não existir regra de recusa,
mas existir regra de derivação:
→ DERIVADO

Se nenhuma regra for acionada:
→ APROVADO
```

---

## 📤 Formato da Resposta

### RECUSADO

```json
{
  "cliente": "João",
  "score_blend": null,
  "resultado": "RECUSADO",
  "motivos": [
    "IDADE_INVALIDA",
    "SCORE_NULO"
  ]
}
```

---

### DERIVADO

```json
{
  "cliente": "João",
  "score_blend": null,
  "resultado": "DERIVADO",
  "motivos": [
    "SCORE_NULO"
  ]
}
```

---

### APROVADO

```json
{
  "cliente": "João",
  "score_blend": 800,
  "resultado": "APROVADO",
  "motivos": []
}
```

---

## 📂 Estrutura Inicial do Projeto

```text
credit-decision-engine/

├── src/
│   ├── customer.py
│   ├── policy.py
│   ├── decision.py
│   ├── decision_engine.py
│   └── main.py
│
├── tests/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 Evoluções Planejadas

### Fase 1

- Implementação do motor de decisão
- Regras de crédito
- Testes unitários

### Fase 2

- Persistência utilizando PostgreSQL 

### Fase 3

- API REST utilizando FastAPI

### Fase 4

- Dockerização da aplicação

### Fase 5

- Deploy em ambiente Cloud (AWS)

---

## 📚 Aprendizados Esperados

- Modelagem de domínio
- Regras de negócio
- Arquitetura de sistemas de decisão
- Programação Orientada a Objetos
- Testes automatizados
- APIs REST
- Persistência de dados
- Containerização
- Cloud Computing

---

## 📌 Conclusão

Este projeto tem como objetivo reproduzir de forma simplificada o funcionamento de um motor de decisão de crédito utilizado no mercado financeiro.

Além de consolidar conhecimentos em Python e regras de negócio, o sistema servirá como base para a construção de uma arquitetura completa envolvendo APIs, banco de dados, testes automatizados, Docker e serviços em nuvem.
