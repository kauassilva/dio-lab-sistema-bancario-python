# Sistema Bancário com Python

## Desafio

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.


## Demonstrações

### Novo usuário

```
======= MENU =======
[d]  Depositar
[s]  Sacar
[e]  Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q]  Sair
>>> nu

Informe o CPF (comente números): 12345678910
Informe o nome completo: Kauã dos Santos
Informe a data de nascimento (dd-mm-aaaa): 17-09-2024
Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): Rua Carvalho, 81 - Mooca - São Paulo/SP

--- Cliente criado com sucesso! ---
```

### Nova conta

```
======= MENU =======
[d]  Depositar
[s]  Sacar
[e]  Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q]  Sair
>>> nc
Informe o CPF do usuário: 12345678910

--- Conta criada com sucesso! ---
```

### Listar contas

```
======= MENU =======
[d]  Depositar
[s]  Sacar
[e]  Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q]  Sair
>>> lc
************************************************************
Agência:	0001
C/C:		1
Titular:	Kauã dos Santos
```

### Depósitos

```
======= MENU =======
[d]  Depositar
[s]  Sacar
[e]  Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q]  Sair
>>> d
Informe o CPF do cliente: 12345678910
Informe o valor do depósito: 5000

--- Depósito realizado com sucesso! ---
```

### Saque

```
======= MENU =======
[d]  Depositar
[s]  Sacar
[e]  Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q]  Sair
>>> s
Informe o CPF do cliente: 12345678910
Informe o valor do saque: 200

--- Saque realizado com sucesso! ---
```


### Extrato

```
======= MENU =======
[d]  Depositar
[s]  Sacar
[e]  Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q]  Sair
>>> e
Informe o CPF do cliente: 12345678910

==================== EXTRATO ====================

Deposito:
	R$ 5000.00
Saque:
	R$ 200.00

Saldo:
	R$ 4800.00
=================================================
```

