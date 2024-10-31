import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Função auxiliar para quebrar texto em várias linhas se necessário
def quebrar_texto(texto, largura, fonte, tamanho_fonte, canvas):
    canvas.setFont(fonte, tamanho_fonte)
    linhas = []
    palavras = texto.split()
    linha_atual = ""
    
    for palavra in palavras:
        if canvas.stringWidth(f"{linha_atual} {palavra}", fonte, tamanho_fonte) <= largura:
            linha_atual += f" {palavra}"
        else:
            linhas.append(linha_atual.strip())
            linha_atual = palavra
    
    if linha_atual:
        linhas.append(linha_atual.strip())
    
    return linhas

def criar_pdf(dados, nome, nome_arquivo, diretorio):
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)

    # Cria o PDF
    c = canvas.Canvas(caminho_arquivo, pagesize=A4)
    largura, altura = A4
    margem_esquerda = 50
    margem_direita = largura - 50
    largura_texto = margem_direita - margem_esquerda
    y = altura - 50  # Posição inicial para começar o texto
    
    # Título do documento
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margem_esquerda, y, f"Notificação por SMS de {nome}")
    y -= 40  # Espaço após o título
    
    # Conteúdo da mensagem com quebra de linha automática
    c.setFont("Helvetica", 12)
    for chave, valor in dados.items():
        # Converte o valor em string, caso não seja
        valor = str(valor)

        linhas_chave = quebrar_texto(f"{chave}:", largura_texto, "Helvetica-Bold", 12, c)
        for linha in linhas_chave:
            c.drawString(margem_esquerda, y, linha)
            y -= 15

        linhas_valor = quebrar_texto(valor, largura_texto, "Helvetica", 12, c)
        for linha in linhas_valor:
            c.drawString(margem_esquerda + 10, y, linha)  # Indenta o valor
            y -= 15

        y -= 10  # Espaço adicional entre os campos
    
    # Salva o PDF
    c.save()
    print(f"PDF '{nome_arquivo}' criado com sucesso em '{diretorio}'.")