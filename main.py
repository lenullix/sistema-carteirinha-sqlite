import datetime
import random
import sys
from interfaces.inicial import *
from interfaces.cadastroAluno import *
from interfaces.cadastroInst import *
from interfaces.cadastroCurso import *
from interfaces.listaInstitutos import *
from interfaces.listaCursos import *
from interfaces.listaAlunos import *
from interfaces.geraCarteirinha import *
from interfaces.listaCarteirinha import *
from interfaces.consultarCarteirinha import *
from PyQt5.QtWidgets import *
import sqlite3


class Main(QMainWindow, Ui_SistemaCarteirinha):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnCadastroAluno.clicked.connect(self.abrirjanelacadastroaluno)
        self.btnCadastoInsti.clicked.connect(self.abrircadastroinstituto)
        self.cadastrarCurso.clicked.connect(self.abrircadastrocurso)
        self.btnListInsti.clicked.connect(self.abrirlistainst)
        self.btnListCursos.clicked.connect(self.abrirlistacursos)
        self.btnListAluno.clicked.connect(self.abrirlistaalunos)
        self.btnGerarCarteirinha.clicked.connect(self.gerarcarteirinha)
        self.btnListCarteirinhas.clicked.connect(self.listarcarteirinhas)
        self.btnConsultarCarteirinha.clicked.connect(self.consultarcarteirinha)

    def abrircadastroinstituto(self):
        stack.setCurrentIndex(1)

    def abrirjanelacadastroaluno(self):
        stack.setCurrentIndex(2)

    def abrircadastrocurso(self):
        stack.setCurrentIndex(3)

    def abrirlistainst(self):
        stack.setCurrentIndex(4)

    def abrirlistacursos(self):
        stack.setCurrentIndex(5)

    def abrirlistaalunos(self):
        stack.setCurrentIndex(6)

    def gerarcarteirinha(self):
        stack.setCurrentIndex(7)

    def listarcarteirinhas(self):
        stack.setCurrentIndex(8)

    def consultarcarteirinha(self):
        stack.setCurrentIndex(9)

class CadastroAluno(QMainWindow, Ui_CadAluno):

    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.labelMensagem.setText('')
        self.btnSalvar.clicked.connect(self.coletardadosaluno)
        self.btnVoltar.clicked.connect(self.voltarinicio)

    def voltarinicio(self):
        stack.setCurrentIndex(0)

    def coletardadosaluno(self):
        nome = self.entradaNome.text()
        cpf = self.entradaCpf.text()
        data_nascimento = self.entradaNascimento.text()
        email = self.entradaEmail.text()
        iniciocurso = self.entradaAnoInicio.text()
        curso = self.entradaCurso.text()
        instituto = self.entradaInstituto.text()
        status = self.entradaStatus.text()
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT CODIGO_CURSO FROM CURSOS_OFERECIDOS WHERE NOME = ?', [curso.upper()])
        numCurso = cursor.fetchone()
        cursor.execute('SELECT CNPJ FROM INSTITUTO WHERE CNPJ = ?', [instituto])
        cnpj = cursor.fetchone()

        if numCurso == None:
            self.labelMensagem.setText('Curso não existe!')
        elif cnpj == None:
            self.labelMensagem.setText('')
            self.labelMensagem.setText('Instituto não existe!')
        else:
            cursor.execute('INSERT INTO ALUNO (NOME, CPF, DATA_NASCIMENTO, EMAIL, CURSO, INSTITUTO, ANO_INICIO, STATUS)'
                   'VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                    [nome.upper(), cpf, data_nascimento, email.upper(), numCurso[0], instituto.upper(), iniciocurso,
                     status.upper()])
            conexao.commit()
            self.labelMensagem.setText('')
            self.labelMensagem.setText('Aluno cadastrado com sucesso!')
        cursor.close()
        conexao.close()


class CadastroInstituto(QMainWindow, Ui_CadInst):

    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.btnVoltar.clicked.connect(self.voltarinicio)
        self.btnSalvar.clicked.connect(self.coletardadosinst)

    def voltarinicio(self):
        stack.setCurrentIndex(0)

    def coletardadosinst(self):

        nome = self.entradaNome.text()
        cnpj = self.entradaCnpj.text()
        endereco = self.entradaEndereco.text()
        telefone = self.entradaTelefone.text()
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO INSTITUTO(NOME, CNPJ, ENDERECO, TELEFONE) VALUES (?, ?, ?, ?)',
                       [nome.upper(), cnpj, endereco.upper(), telefone])
        conexao.commit()
        cursor.close()
        conexao.close()


class CadastroCurso(QMainWindow, Ui_cadCurso):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.btnVoltar.clicked.connect(self.voltarinicio)
        self.btnSalvar.clicked.connect(self.coletardadoscurso)

    def voltarinicio(self):
        stack.setCurrentIndex(0)

    def coletardadoscurso(self):
        nome = self.entradaNome.text()
        codigo = self.entradaCodigo.text()
        instituto = self.entradaInst.text()

        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        cursor.execute('SELECT CNPJ FROM INSTITUTO WHERE CNPJ = ?', [instituto])
        cnpj = cursor.fetchone()
        if cnpj == None:
            self.labelMensagem.setText('Instituto não existe!')
        else:
            cursor.execute('INSERT INTO CURSOS_OFERECIDOS(NOME, CODIGO_CURSO, INSTITUTO) VALUES (?, ?, ?)',
                       [nome.upper(), codigo, instituto.upper()])
            conexao.commit()
            self.labelMensagem.setText('')
            self.labelMensagem.setText('Curso cadastrado com sucesso!')

        cursor.close()
        conexao.close()


class ListarInstitutos(QMainWindow, Ui_listInstituto):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.btnVoltar.clicked.connect(self.voltarinicio)
        self.tabelaInst.setHorizontalHeaderLabels(["Nome", "CNPJ", "Endereço", "Telefone"])
        self.listardados()

    def voltarinicio(self):
        stack.setCurrentIndex(0)

    def listardados(self):
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM INSTITUTO')
        dados = cursor.fetchall()
        self.tabelaInst.setRowCount(len(dados))
        numLinha = 0
        for linha in dados:
            self.tabelaInst.setItem(numLinha, 0, QtWidgets.QTableWidgetItem(linha[1]))
            self.tabelaInst.setItem(numLinha, 1, QtWidgets.QTableWidgetItem(str(linha[0])))
            self.tabelaInst.setItem(numLinha, 2, QtWidgets.QTableWidgetItem(linha[2]))
            self.tabelaInst.setItem(numLinha, 3, QtWidgets.QTableWidgetItem(str(linha[3])))
            numLinha = numLinha + 1

        cursor.close()
        conexao.close()


class ListarCursos(QMainWindow, Ui_listaCursos):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.btnVoltar.clicked.connect(self.voltarinicio)
        self.tabelaCursos.setHorizontalHeaderLabels(["Código do Curso", "Nome", "Instituto"])
        self.listardados()

    def voltarinicio(self):
        stack.setCurrentIndex(0)

    def listardados(self):
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT C.CODIGO_CURSO, C.NOME, I.NOME '
                       'FROM CURSOS_OFERECIDOS C, INSTITUTO I '
                       'WHERE C.INSTITUTO = I.CNPJ')
        dados = cursor.fetchall()
        self.tabelaCursos.setRowCount(len(dados))
        numLinha = 0
        for linha in dados:
            self.tabelaCursos.setItem(numLinha, 0, QtWidgets.QTableWidgetItem(str(linha[0])))
            self.tabelaCursos.setItem(numLinha, 1, QtWidgets.QTableWidgetItem(linha[1]))
            self.tabelaCursos.setItem(numLinha, 2, QtWidgets.QTableWidgetItem(linha[2]))
            numLinha = numLinha + 1
        cursor.close()
        conexao.close()


class ListarAlunos(QMainWindow, Ui_listAlunos):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.btnVoltar.clicked.connect(self.voltarinicio)
        self.tabelaAlunos.setHorizontalHeaderLabels(["Nome", "CPF", "Dada de Nascimento", "Email", "Curso", "Instituto", "Status"])
        self.btnTodos.clicked.connect(self.listartodos)
        self.btnGraduados.clicked.connect(self.listargraduados)
        self.btnGraduandos.clicked.connect(self.listargraduandos)

    def voltarinicio(self):
        stack.setCurrentIndex(0)

    def listartodos(self):
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT A.NOME, A.CPF, A.DATA_NASCIMENTO, A.EMAIL, C.NOME, I.NOME, A.STATUS '
                       'FROM ALUNO A, CURSOS_OFERECIDOS C, INSTITUTO I '
                       'WHERE A.CURSO = C.CODIGO_CURSO AND A.INSTITUTO = I.CNPJ')
        dados = cursor.fetchall()
        self.tabelaAlunos.setRowCount(len(dados))
        numLinha = 0
        for linha in dados:
            self.tabelaAlunos.setItem(numLinha, 0, QtWidgets.QTableWidgetItem(linha[0]))
            self.tabelaAlunos.setItem(numLinha, 1, QtWidgets.QTableWidgetItem(str(linha[1])))
            self.tabelaAlunos.setItem(numLinha, 2, QtWidgets.QTableWidgetItem(str(linha[2])))
            self.tabelaAlunos.setItem(numLinha, 3, QtWidgets.QTableWidgetItem(linha[3]))
            self.tabelaAlunos.setItem(numLinha, 4, QtWidgets.QTableWidgetItem(linha[4]))
            self.tabelaAlunos.setItem(numLinha, 5, QtWidgets.QTableWidgetItem(linha[5]))
            self.tabelaAlunos.setItem(numLinha, 6, QtWidgets.QTableWidgetItem(linha[6]))
            numLinha = numLinha + 1


    def listargraduados(self):
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT A.NOME, A.CPF, A.DATA_NASCIMENTO, A.EMAIL, C.NOME, I.NOME, A.STATUS '
                       'FROM ALUNO A, CURSOS_OFERECIDOS C, INSTITUTO I '
                       'WHERE A.CURSO = C.CODIGO_CURSO AND A.INSTITUTO = I.CNPJ AND A.STATUS = ?', ['GRADUADO'])
        dados = cursor.fetchall()
        self.tabelaAlunos.setRowCount(len(dados))
        numLinha = 0
        for linha in dados:
            self.tabelaAlunos.setItem(numLinha, 0, QtWidgets.QTableWidgetItem(linha[0]))
            self.tabelaAlunos.setItem(numLinha, 1, QtWidgets.QTableWidgetItem(str(linha[1])))
            self.tabelaAlunos.setItem(numLinha, 2, QtWidgets.QTableWidgetItem(str(linha[2])))
            self.tabelaAlunos.setItem(numLinha, 3, QtWidgets.QTableWidgetItem(linha[3]))
            self.tabelaAlunos.setItem(numLinha, 4, QtWidgets.QTableWidgetItem(linha[4]))
            self.tabelaAlunos.setItem(numLinha, 5, QtWidgets.QTableWidgetItem(linha[5]))
            self.tabelaAlunos.setItem(numLinha, 6, QtWidgets.QTableWidgetItem(linha[6]))
            numLinha = numLinha + 1

    def listargraduandos(self):
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT A.NOME, A.CPF, A.DATA_NASCIMENTO, A.EMAIL, C.NOME, I.NOME, A.STATUS '
                       'FROM ALUNO A, CURSOS_OFERECIDOS C, INSTITUTO I '
                       'WHERE A.CURSO = C.CODIGO_CURSO AND A.INSTITUTO = I.CNPJ AND A.STATUS = ?', ['GRADUANDO'])
        dados = cursor.fetchall()
        self.tabelaAlunos.setRowCount(len(dados))
        numLinha = 0
        for linha in dados:
            self.tabelaAlunos.setItem(numLinha, 0, QtWidgets.QTableWidgetItem(linha[0]))
            self.tabelaAlunos.setItem(numLinha, 1, QtWidgets.QTableWidgetItem(str(linha[1])))
            self.tabelaAlunos.setItem(numLinha, 2, QtWidgets.QTableWidgetItem(str(linha[2])))
            self.tabelaAlunos.setItem(numLinha, 3, QtWidgets.QTableWidgetItem(linha[3]))
            self.tabelaAlunos.setItem(numLinha, 4, QtWidgets.QTableWidgetItem(linha[4]))
            self.tabelaAlunos.setItem(numLinha, 5, QtWidgets.QTableWidgetItem(linha[5]))
            self.tabelaAlunos.setItem(numLinha, 6, QtWidgets.QTableWidgetItem(linha[6]))
            numLinha = numLinha + 1


class GerarCarteirinha(QMainWindow, Ui_geraCarteirinha):

    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.btnVoltar.clicked.connect(self.voltarinicio)
        self.btnGerar.clicked.connect(self.coletardados)
        self.btnRenovar.clicked.connect(self.renovar)


    def voltarinicio(self):
        stack.setCurrentIndex(0)

    def coletardados(self):
        cpf = self.entradaCPF.text()

        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        cursor.execute('SELECT CPF FROM ALUNO WHERE CPF = ?', [cpf])
        alunoexiste = cursor.fetchone()
        cursor.execute('SELECT ALUNO FROM CARTEIRINHAS WHERE ALUNO =?', [cpf])
        carteirinhaexiste = cursor.fetchone()
        cursor.execute('SELECT STATUS FROM ALUNO WHERE CPF =?', [cpf])
        status = cursor.fetchone()

        if alunoexiste == None:

            self.labelMensagem.setText('Aluno não existe!')

        elif carteirinhaexiste != None:

            self.labelMensagem.setText('Carteirinha já existe, deseja renovar?')

        elif status[0] == 'GRADUADO':

            self.labelMensagem.setText('Aluno já graduado, não é possível gerar carteirinha!')

        else:
            cursor.execute('SELECT A.NOME, C.NOME, A.ANO_INICIO, I.NOME, A.CPF '
                           'FROM ALUNO A, INSTITUTO I, CURSOS_OFERECIDOS C '
                           'WHERE A.CPF = ? AND A.INSTITUTO = I.CNPJ AND A.CURSO = C.CODIGO_CURSO', [cpf])
            resultado = cursor.fetchone()

            codigo = random.randrange(1, 100000)
            self.labelNome.setText('Nome:'+' '+resultado[0])
            self.labelInstituto.setText(resultado[3])
            self.labelCurso.setText('Curso:'+' '+resultado[1])
            self.labelAno.setText('Ano de inicio:'+' '+str(resultado[2]))
            self.labelCodigo.setText('Código da carteirinha:'+' '+str(codigo))
            data = datetime.date.today()
            validade = '{0}-{1}-{2}'.format(str(data.day), str(data.month), str(data.year+5))
            self.labelValidade.setText('Validade:'+' '+str(validade))
            cursor.execute('INSERT INTO CARTEIRINHAS VALUES (?, ?, ?)', [resultado[4], codigo, validade])
            conexao.commit()
            cursor.close()
            conexao.close()

    def renovar(self):
        cpf = self.entradaCPF.text()
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT A.NOME, I.NOME, C.NOME, A.ANO_INICIO  '
                       'FROM ALUNO A, INSTITUTO I, CURSOS_OFERECIDOS C '
                       'WHERE A.CPF = ? AND A.INSTITUTO = I.CNPJ AND A.CURSO = C.CODIGO_CURSO ', [cpf])

        resultado1 = cursor.fetchone()
        cursor.execute('SELECT CODIGO FROM CARTEIRINHAS WHERE ALUNO = ?', [cpf])
        resultado2 = cursor.fetchone()
        self.labelNome.setText('Nome:' + ' ' + resultado1[0])
        self.labelInstituto.setText(resultado1[1])
        self.labelCurso.setText('Curso:' + ' ' + resultado1[2])
        self.labelAno.setText('Ano de inicio:' + ' ' + str(resultado1[3]))
        self.labelCodigo.setText('Código da carteirinha:' + ' ' + str(resultado2[0]))
        data = datetime.date.today()
        validade = '{0}-{1}-{2}'.format(str(data.day), str(data.month), str(data.year + 5))
        self.labelValidade.setText('Validade:' + ' ' + str(validade))
        cursor.execute('UPDATE CARTEIRINHAS SET DATA_VALIDADE = ? WHERE ALUNO = ?', [validade, cpf])
        conexao.commit()
        cursor.close()
        conexao.close()


class ListarCarteirinha(QMainWindow, Ui_listaCarteirinhas):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.btnVoltar.clicked.connect(self.voltarinicio)
        self.tabelaCarteirinha.setHorizontalHeaderLabels(["CPF Aluno", "Código Carteirinha", "Validade"])
        self.listar()

    def voltarinicio(self):
        stack.setCurrentIndex(0)

    def listar(self):
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM CARTEIRINHAS')
        dados = cursor.fetchall()
        self.tabelaCarteirinha.setRowCount(len(dados))
        numLinha = 0
        for linha in dados:
            self.tabelaCarteirinha.setItem(numLinha, 0, QtWidgets.QTableWidgetItem(str(linha[0])))
            self.tabelaCarteirinha.setItem(numLinha, 1, QtWidgets.QTableWidgetItem(str(linha[1])))
            self.tabelaCarteirinha.setItem(numLinha, 2, QtWidgets.QTableWidgetItem(str(linha[2])))
            numLinha = numLinha + 1

        cursor.close()
        conexao.close()


class ConsultarCarteirinha(QMainWindow, Ui_consultarCarteirinha):

    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.btnVoltar.clicked.connect(self.voltarinicio)
        self.btnConsultar.clicked.connect(self.coletardados)

    def voltarinicio(self):
        stack.setCurrentIndex(0)

    def coletardados(self):
        entrada = self.entradaCPF.text()
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT ALUNO FROM CARTEIRINHAS WHERE ALUNO = ? ', [entrada])
        cpf = cursor.fetchone()
        cursor.execute('SELECT ALUNO FROM CARTEIRINHAS WHERE CODIGO = ? ', [entrada])
        cpf2 = cursor.fetchone()

        if cpf != None:

            cursor.execute('SELECT A.NOME, I.NOME, C.NOME, A.ANO_INICIO '
                           'FROM ALUNO A, INSTITUTO I, CURSOS_OFERECIDOS C '
                           'WHERE A.CPF = ? AND A.INSTITUTO = I.CNPJ AND A.CURSO = C.CODIGO_CURSO', (cpf))
            resultado = cursor.fetchone()
            cursor.execute('SELECT CODIGO, DATA_VALIDADE FROM CARTEIRINHAS WHERE ALUNO = ?', (cpf))
            resultado2 = cursor.fetchone()
            self.labelInstituto.setText(resultado[1])
            self.labelNome.setText('Nome:'+' '+resultado[0])
            self.labelCurso.setText('Curso:'+' '+resultado[2])
            self.labelAno.setText('Ano de inicio:'+' '+str(resultado[3]))
            self.labelCodigo.setText('Código da carteirinha:'+' '+str(resultado2[0]))
            self.labelValidade.setText('Validade'+ ' '+str(resultado2[1]))

        elif cpf2 != None:
            cursor.execute('SELECT CODIGO, DATA_VALIDADE FROM CARTEIRINHAS WHERE ALUNO = ?', (cpf2))
            resultado = cursor.fetchone()
            cursor.execute('SELECT A.NOME, I.NOME, C.NOME, A.ANO_INICIO '
                           'FROM ALUNO A, INSTITUTO I, CURSOS_OFERECIDOS C '
                           'WHERE A.CPF = ? AND A.INSTITUTO = I.CNPJ AND A.CURSO = C.CODIGO_CURSO', (cpf2))
            resultado2 = cursor.fetchone()

            self.labelInstituto.setText(resultado2[1])
            self.labelNome.setText('Nome:'+' '+resultado2[0])
            self.labelCurso.setText('Curso:'+ ' '+resultado2[2])
            self.labelAno.setText('Ano de inicio:'+' '+str(resultado2[3]))
            self.labelCodigo.setText('Código da carteirinha:'+' '+str(resultado[0]))
            self.labelValidade.setText('Validade:'+' '+str(resultado[1]))
        else:
            self.labelMensagem.setText('Aluno ou carteirinha não existe!')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    main = Main()
    stack = QtWidgets.QStackedWidget()
    stack.insertWidget(0, main)
    cadinst = CadastroInstituto()
    stack.insertWidget(1, cadinst)
    cadastroaluno = CadastroAluno()
    stack.insertWidget(2, cadastroaluno)
    cadcurso = CadastroCurso()
    stack.insertWidget(3, cadcurso)
    listainst = ListarInstitutos()
    stack.insertWidget(4, listainst)
    listacursos = ListarCursos()
    stack.insertWidget(5, listacursos)
    listaalunos = ListarAlunos()
    stack.insertWidget(6, listaalunos)
    gerarcarteirinha = GerarCarteirinha()
    stack.insertWidget(7, gerarcarteirinha)
    listarcarteirinha = ListarCarteirinha()
    stack.insertWidget(8, listarcarteirinha)
    consultacarteirinha = ConsultarCarteirinha()
    stack.insertWidget(9, consultacarteirinha)
    stack.setCurrentIndex(0)
    stack.setFixedWidth(600)
    stack.setFixedHeight(600)
    stack.show()
    qt.exec_()
