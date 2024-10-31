from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from twilio.rest import Client
from dotenv import dotenv_values
from comprovante import criar_pdf

# Configurações
config = dotenv_values(".env")
diretorio = config.get("DIRETORIO")
celular_origem = config.get("CELULAR_ORIGEM")
pais = config.get("PAIS")
funcionario = config.get("FUNCIONARIO")
promotor = config.get("PROMOTOR")

# Templates de mensagem
msg_vitima = """Sr(a) {nome}: Comunica-se que inquérito policial nº {num_ip}, em que V. Sa. figurou como vítima, foi arquivado. 
Cópia da referida decisão pode ser solicitada pelo e-mail {funcionario}, com comprovacao de identidade, ou pessoalmente, na \
sede da Promotoria de Justiça, rua Almirante Barroso nº 491, Piracicaba/SP. 
No prazo de 30 dias, V. Sa. poderá solicitar a revisão do arquivamento, por pedido escrito, pelo e-mail informado ou pessoalmente. 
{promotor}"""

msg_averiguado = """Sr(a) {nome}: Comunica-se, nos termos do art. 28 do CPP, que inquérito policial nº {num_ip}, \
no qual V. Sa. figurou como investigado(a), foi arquivado. 
{promotor}"""

class NotificaUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('tela_notificador.ui', self)
        self.bt_enviar.clicked.connect(self.notifica)
    
    def notifica(self):
        # Validação dos campos de entrada
        if not self.validar_campos():
            return

        num_ip = self.num_ip.text()
        nome = self.nome.text()
        celular_destino = pais + self.celular.text()
        
        if self.vitima.isChecked():
            nome_arquivo_pdf = f'{num_ip}_notificacao_vitima_{nome}.pdf' 
            body = msg_vitima.format(nome=nome, num_ip=num_ip, funcionario=funcionario, promotor=promotor)
        else:
            nome_arquivo_pdf = f'{num_ip}_notificacao_averiguado_{nome}.pdf' 
            body = msg_averiguado.format(nome=nome, num_ip=num_ip, promotor=promotor)

        # Envio do SMS e geração de comprovante
        self.enviar_sms(num_ip, nome, celular_destino, body, nome_arquivo_pdf)

    def validar_campos(self):
        """Valida os campos de entrada do formulário."""
        if not self.num_ip.text() or not self.nome.text() or not self.celular.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Todos os campos devem ser preenchidos.")
            msg.exec_()
            return False
        return True
    
    def enviar_sms(self, num_ip, nome, celular_destino, body, nome_arquivo_pdf):
        """Envia SMS via Twilio e cria comprovante em PDF."""
        try:
            client = Client(config['account_sid'], config['auth_token'])
            sms = client.messages.create(
                from_=celular_origem,
                body=body,
                to=celular_destino
            )
            
            dados_do_envio = {
                "ID da Mensagem": sms.sid,
                "Número de Destino": sms.to,
                "Data e Hora do Envio": sms.date_created,
                "Conteúdo da Mensagem": sms.body,
                "Status da Mensagem": sms.status,
                "Número de Origem": sms.from_
            }
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f'SMS enviado com sucesso. SID: {sms.sid}')
            criar_pdf(dados_do_envio, nome, nome_arquivo_pdf, diretorio)
            msg.exec_()

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f'Erro ao enviar SMS. Detalhes: {str(e)}')
            msg.exec_()

if __name__ == '__main__':
    app = QApplication([])
    window = NotificaUI()
    window.show()
    app.exec_()