Desafio em Python - (Sistema Bancário)

🏦 Sistema Bancário - Gerenciamento de Contas e Transações

Projeto desenvolvido em Python com o objetivo de aplicar na prática conceitos de Programação Orientada a Objetos (POO), por meio da construção de um sistema bancário que simula operações financeiras básicas.

Este projeto faz parte da minha evolução nos estudos de desenvolvimento de software e representa uma oportunidade de aprofundar conhecimentos em Python, explorando recursos da linguagem e boas práticas de programação.

🚀 Sobre o Projeto

O Sistema Bancário é uma aplicação executada pelo terminal que permite cadastrar clientes, criar contas correntes e realizar operações financeiras, como depósitos e saques.

A aplicação foi estruturada utilizando classes, métodos e funções, buscando organizar as responsabilidades do sistema, promover a reutilização de código e facilitar a manutenção.

Além das funcionalidades bancárias, o projeto também implementa recursos como histórico de transações, geração de relatórios e registro de operações em arquivos de log.

⚙️ Funcionalidades

Cadastro de Clientes: permite registrar clientes com nome, CPF, data de nascimento e endereço.

Criação de Contas: possibilita criar contas correntes vinculadas aos clientes cadastrados.

Depósitos: permite adicionar valores ao saldo da conta.

Saques: realiza retiradas respeitando as regras e os limites definidos para a conta.

Extrato Bancário: apresenta o histórico de movimentações, incluindo datas, tipos de transações e valores.

Listagem de Contas: exibe as contas cadastradas, seus respectivos números, agências, titulares e saldos.

Controle de Transações: limita a quantidade de operações diárias realizadas pelo cliente.

Histórico de Operações: armazena as movimentações financeiras realizadas em cada conta.

Relatórios com Geradores: utiliza yield para percorrer e filtrar as transações registradas.

Registro de Logs: utiliza decoradores para registrar a execução das operações em um arquivo log.txt.

🧠 Tecnologias e Conceitos

Linguagem: Python 3.

Programação Orientada a Objetos (POO): classes, objetos, herança, encapsulamento e métodos de classe (@classmethod).

Classes Abstratas: utilização de ABC e @abstractmethod para definir contratos de implementação.

Propriedades: utilização de @property para controlar o acesso aos atributos.

Iteradores: implementação dos métodos __iter__() e __next__().

Geradores: utilização de yield para geração de relatórios de transações.

Decoradores: criação de um decorador personalizado para registrar logs das operações.

Manipulação de Arquivos: utilização de open() e with para registrar informações em arquivos externos.

Bibliotecas: datetime, textwrap, pathlib e abc.

Ferramentas: Git e GitHub para controle de versão.

🎯 Objetivo de Aprendizado

O principal objetivo deste projeto é aprofundar os conhecimentos em Python e Programação Orientada a Objetos, explorando recursos mais avançados da linguagem.

Durante o desenvolvimento, foram trabalhados conceitos importantes para a construção de aplicações mais organizadas, reutilizáveis e estruturadas, simulando funcionalidades básicas de um sistema bancário.