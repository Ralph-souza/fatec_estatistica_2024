# TRABALHO DE ESTATÍSTICA - TERCEIRO SEMESTRE

**FATEC CAMPUS JUNDIAÍ - DEPUTADO ARY FOSSEN (2024)**

Este é um trabalho de conclusão de semestre para a matéria de **ESTATÍSTICA** ministrada pelo professor:<br><br>

**JOÃO CARLOS DOS SANTOS**

O mesmo tem como participantes no seu desenvolvimento os seguintes alunos:<br><br>

**GUSTAVO HENRIQUE KLINGER AMADI**<br>
**KAIQUE BARADEL GUARDA**<br>
**JOÃO PAULO MARCHETTI VECINA**<br>
**RALPH DOS SANTOS SOUZA**<br><br>

---
**FOCO DO PROJETO**<br><br>

O foco da aplicação está no cálculo da **DISTRIBUIÇÃO UNIFORME**, avaliando pontos como:<br><br>

* Média
* Variância
* Desvio Padrão
* Coeficiente de Variação
* Probabilidade<br><br>

---

**EXECUTANDO A APLICAÇÃO**<br><br>

Após clonagem será necessário a criação de uma máquina virtual através do terminal.<br>
*OBS: Os dados descritos a seguir visam esclarecer o passo a passo para execução em ambiente LINUX*<br><br>

```
$ python3 -m venv <nome da máquina virtual>
```

Para acessar a mesma basta aplicar o seguinte comando a seguir.

```
$ source <nome da máquina virtual>/bin/activate
```

Em seguida será necessário a instalação dos componentes necessários para a execução da mesma.<br>
Para isso basta executar o seguinte comando.

```
$ pip install -r requirements.txt
```

Em seguida basta rodar a migração do **DJANGO** através do seguinte comando.

```
$ ./manage.py migrate
```

*OBS: Como o projeto não possui modelos não será necessário criar as migrações, basta apenas a execução das migrações de base do projeto*<br><br>

Agora podemos executar o mesmo atraés do comando:

```
./manage.py runserver
```