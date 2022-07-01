### Step 1

```bash
export VAGRANT_EXPERIMENTAL="disks"
vagrant plugin install vagrant-disksize
```

---

### Step 2

#### Obs:

__Leia o comentário no Vagrantfile__

---

```bash
vagrant up tworp

vagrant ssh tworp

#Dentro da VM
sudo passwd root #coloque a senha como "tworp123"

su root #Coloca o password que definiu

yum update -y

yum install python3 -y

sudo python3 script.py 
```

---
### Documentos Uteis
- [How to Install Apache Zeppelin on CentOS 7](https://www.vultr.com/docs/how-to-install-apache-zeppelin-on-centos-7/)

- [Apache Zeppelin Configuration](https://zeppelin.apache.org/docs/0.8.0/setup/operation/configuration.html)

---

### Considerações Finais

Eu levei 09 horas e 30 minutos(aproximadamente) ao todo pra fazer tudo oque está nesse repositório(ficou faltando só criar e inserir os usuários de um txt) das quais 8 delas foram tentanto resolver um problema no meu sistema operacional, eu uso o Fedora36 e tanto o VMWare quanto o VirtualBox estavam dando um erro no Kernel Headers com vários módulos, oque primeiro me impedia de subir VMs com o vagrant(eu resolvi assinando manualmente os modulos porque desabilitar o Secure Boot não ajudou em nada) e posteriormente tinha erro para criar uma interface bridge na VM pra mim poder acessar o WebServer do Zeppelin atráves do Host, problema este que eu resolvi graças a esse forum: [VirtualBox-6.1 on Fedora 36 - Installation failed](https://forums.virtualbox.org/viewtopic.php?f=7&t=106307). Enfim, eu gastei muito mais tempo tentanto resolver problemas do meu sistema operacional do que com o desafio em si, dentro do prazo determinado eu consegui garantir: 

1. Criar um script Vagrant que suba uma máquina CentOS 7.x com 2 CPUs (2 cores de processador), 4 GB de memória RAM e 50gb de HD chamada “teste-zeppelin”. O acesso a ela deve ser através de uma chave privada, não com senha

2. Criar um programa em python que faça a instalação do Java e do Apache Zeppelin nessa máquina recém criada. Além disso, o programa deve subir o webserver do Zeppelin na porta 8888

---
