# Sistema Bancário com Python

## Desafio

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.


## Demonstrações


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

Informe o valor do depósito: 140

Depósito realizado com sucesso!
-----------------------------------
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

Informe o valor do saque: 29

Saque realizado com sucesso!
-----------------------------------
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

==================== EXTRATO ====================
Depósito:	R$ 140.00
Saque:		R$ 29.00


Saldo: R$ 140.00
=================================================
```



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

Informe o CPF (comente números): 123456789
Informe o nome completo: John Ronald Reuel Tolkien
Informe a data de nascimento (dd-mm-aaaa): 03-01-1892
Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): Rua C, 143 - Arco - Suldo/AS

Usuário criado com sucesso!
-----------------------------------
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

Informe o CPF do usuário: 123456789

Conta criada com sucesso!
-----------------------------------
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

============================================================

Agência:	0001
C/C:		1
Titular:	John Ronald Reuel Tolkien
```