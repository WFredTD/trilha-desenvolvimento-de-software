# 🤝 Módulo 1: Git e GitHub para Colaboração

Este diretório contém a documentação e os comandos essenciais para o **Módulo 1: Git e GitHub para Colaboração** da minha Trilha de Desenvolvimento de Software. Este módulo é a base para trabalhar com qualquer código, seja individualmente ou em equipe, e é crucial para qualquer desenvolvedor.

Dominar esses conceitos é fundamental para rastrear mudanças no código e facilitar a colaboração em projetos.

## 📝 Visão Geral do Módulo

Cobrimos o Git, o sistema de controle de versão essencial para rastrear suas mudanças, e o GitHub, a plataforma online que armazena seu código e facilita a colaboração.

## 📋 Conteúdo Detalhado (Tópicos Principais)

* 1.1 O Que é Git e Por Que Ele é Essencial?
* 1.2 Criando e Clonando Repositórios
* 1.3 Adicionando, Comitando e Enviando Mudanças
* 1.4 Entendendo Branches e Merges
* 1.5 Desfazendo Mudanças Locais e Remotas
* 1.6 Boas Práticas e Fluxo de Trabalho Git Essencial

## 💡 Resumo do Módulo (Pontos Chave para Consulta Rápida)

### Conceitos Fundamentais

* **Git:** Sistema de Controle de Versão Distribuído (DVCS). Ferramenta que rastreia e gerencia todas as alterações feitas nos arquivos de um projeto ao longo do tempo. Permite voltar no tempo e colaborar.
* **GitHub:** Plataforma online que hospeda repositórios Git remotos. Serve para backup do código e facilita a colaboração em equipe.
* **Repositório:** Uma pasta no seu computador que o Git está monitorando. Contém uma subpasta oculta crucial chamada `.git/`.
* **Branches (Ramificações):** Linhas de desenvolvimento independentes que permitem trabalhar em funcionalidades ou correções isoladamente, sem afetar a linha principal do código (`main` ou `master`).
* **Commit:** Uma "fotografia" do estado do seu projeto em um determinado momento. Cada commit registra as alterações, o autor e uma mensagem descritiva.
* **Staging Area (Área de Preparação):** Uma área intermediária onde você seleciona e organiza as mudanças que deseja incluir no próximo commit.
* **Merge:** O processo de unir as mudanças de uma branch em outra.
* **Conflito de Merge:** Ocorre quando o Git não consegue combinar automaticamente as mudanças de duas branches e precisa da intervenção humana para resolver as divergências.

### Comandos Essenciais (Consulta Rápida)

* `git config --global user.name "Seu Nome"`: Configura o nome de usuário globalmente.
* `git config --global user.email "seu.email@example.com"`: Configura o e-mail do usuário globalmente.
* `git config --list --global`: Lista todas as configurações globais do Git.
* `git init`: Inicializa um novo repositório Git na pasta atual, criando a subpasta `.git/`.
* `git clone <URL_DO_REPOSITORIO>`: Baixa uma cópia completa de um repositório Git existente de um serviço remoto (como o GitHub). Já configura o `.git/` e a conexão remota.
* `git remote -v`: Lista as conexões para os repositórios remotos. Mostra os apelidos (ex: `origin`) e os URLs usados para baixar (`fetch`) e enviar (`push`) dados.
* `git status`: Mostra o estado atual do seu repositório: quais arquivos foram modificados, quais são novos (untracked), e quais estão preparados para o commit (staged).
* `git add <nome_do_arquivo>`: Adiciona um arquivo específico ou todos os arquivos modificados/novos (`.`) para a staging area, preparando-os para o próximo commit.
* `git commit -m "Mensagem do commit"`: Salva as mudanças que estão na staging area no histórico do repositório local. A mensagem deve ser descritiva.
* `git push origin <branch>`: Envia os commits do seu repositório local para o repositório remoto (`origin`) na branch especificada.
* `git pull origin <branch>`: Baixa as mudanças do repositório remoto (`origin`) para a branch local e as integra.
* `git branch`: Lista todas as branches locais.
* `git switch <branch>`: Muda para uma branch existente.
* `git switch -c <nova_branch>`: Cria uma nova branch e muda para ela.
* `git merge <branch-origem>`: Combina as mudanças da `branch-origem` para a branch atual.
* `git revert <hash-do-commit>`: Cria um novo commit que desfaz as alterações de um commit anterior. Preserva o histórico.
* `git restore <arquivo>`: Desfaz mudanças no diretório de trabalho para um arquivo específico.
* `git restore --staged <arquivo>`: Remove um arquivo da staging area, mantendo as mudanças no diretório de trabalho.
* `git clean -f`: Remove arquivos não rastreados (untracked) do diretório de trabalho. Cuidado!
* `git reset --soft HEAD~1`: Move a branch para o commit anterior, mantendo as mudanças no staging area e no diretório de trabalho.
* `git reset --mixed HEAD~1` (padrão): Move a branch, desfaz o commit e as mudanças da staging area, mantendo-as no diretório de trabalho.
* `git reset --hard HEAD~1` (CUIDADO!): Desfaz o commit, as mudanças da staging area e **descarta as mudanças no diretório de trabalho**. Perde dados!
* `git branch -d <branch-local>`: Deleta uma branch local (se ela já foi mesclada).
* `git push origin --delete <branch-remota>`: Deleta uma branch no repositório remoto.

## 🎯 Aplicação Prática

Embora este módulo não contenha exercícios de código Python específicos, os conceitos e comandos de Git e GitHub são aplicados **continuamente** em **todos os Projetos Integradores (PIs)** e em **todos os exercícios de código** ao longo desta trilha. A prática constante é a chave para dominar o controle de versão e a colaboração.

---