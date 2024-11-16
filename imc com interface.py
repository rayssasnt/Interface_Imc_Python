import customtkinter as ctk
import emoji
# Inicializa a janela principal
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
janela = ctk.CTk()
janela.geometry("400x300")
janela.title("CALCULE SEU PESO IDEAL")

#tela
titulo = ctk.CTkLabel(janela, text="CALCULE SEU PESO IDEAL", font=("", 20))

# Cria um campo de entrada
titulo.pack(padx=10, pady=10)
campo_altura = ctk.CTkEntry(janela, placeholder_text="Digite sua altura: " , width=110, height=30)
campo_peso = ctk.CTkEntry(janela, placeholder_text="Digite seu peso: " , width=110, height=30)
campo_altura.pack(padx=10,pady=10)
campo_peso.pack(padx=10,pady=10)

#calcular o imc
def calcular_imc(peso , altura):
    return peso /(altura**2)

#exibir 
def exibir_resultado():
    try:
        peso = float(campo_peso.get())# Pega o valor do campo de entrada e converte
    #para float
        altura= float(campo_altura.get())# Pega o valor do campo de entrada e converte
        #para float

        altura_m = altura/100
        imc = calcular_imc(peso, altura_m)


        if imc <= 18.5:
            resultado = "Você está ABAIXO do PESO normal"
        elif 18.5 <= imc < 25:
            resultado = "Você está na faixa de PESO NORMAL"
        elif 25 <= imc < 30:
            resultado = "SOBREPESO"
        elif 30 <= imc < 40:
            resultado = emoji.emojize("OBESO 🔴")
        else:
            resultado = "OBESIDADE MÓRBIDA"


        rotulo_resultado.configure(text=f"Seu Indice Corporal é: {imc:.2f}\n{resultado}",font=("", 17))
    except ValueError:
        rotulo_resultado.configure(text="Digite um valor numérico válido")


# Botão para calcula a area

botao = ctk.CTkButton(janela, text="CALCULAR", command=exibir_resultado , width=110, height=30)
botao.pack(padx =10 ,pady=10)
#exibir

rotulo_resultado = ctk.CTkLabel(janela, text="")
rotulo_resultado.pack(pady=10)

exibir_resultado = ctk.CTkLabel(janela, text="")

janela.mainloop




       






























# Inicia o loop principal da janela
janela.mainloop()

