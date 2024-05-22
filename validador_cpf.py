# Validação de CPF # Exemplo 529.982.247-25 (2,5)


# Numera o CPF
def numerar_cpf():
    for a in cpf:
        a = int(a)
        cpf_digitado.append(a)


# Verifica o tamanho do CPF
def quantidade():
    if len(cpf) < 11 or len(cpf) > 11:
        # print(f'O CPF é inválido pois nele há {len(cpf)} caracteres.')
        return False
    else:
        return True


# Verifica o primeiro dígito do CPF
def primeiro_digito():
    acumulador = 0  # acumula o resultado #04
    resultado = 0  # 03
    controlador = 10  # 01
    for numeros in cpf_digitado[0:9]:  # 02
        resultado = numeros * controlador  # multiplica os valores
        acumulador += resultado
        controlador = controlador - 1  # diminui 1 do controlador
    acumulador = acumulador * 10 % 11
    if acumulador == 10:
        acumulador = 0
    if acumulador == cpf_digitado[9]:
        return True
    else:
        return False


# Verifica o segundo dígito do CPF
def segundo_digito():
    if len(cpf_digitado) < 11 or len(cpf_digitado) > 11:
        return False
    else:
        acumulador2 = 0  # acumula o resultado #04
        resultado2 = 0  # 03
        controlador2 = 11  # 01
        for numeros2 in cpf_digitado[0:10]:  # 02
            resultado2 = numeros2 * controlador2  # multiplica os valores
            acumulador2 += resultado2
            controlador2 = controlador2 - 1  # diminui 1 do controlador
        acumulador2 = acumulador2 * 10 % 11
        if acumulador2 == 10:
            acumulador2 = 0
        if acumulador2 == cpf_digitado[10]:
            return True
        else:
            return False


cpf_digitado = []
cpf = (
    str(input("Digite seu CPF: ")).replace(".", "").replace("-", "")
)  # Recebe o CPF com ou sem pontuação


numerar_cpf()
quantidade()
primeiro_digito()
segundo_digito()

if quantidade() == True and primeiro_digito() == True and segundo_digito() == True:
    print("O CPF é válido.")
else:
    print("O CPF é inválido.")
