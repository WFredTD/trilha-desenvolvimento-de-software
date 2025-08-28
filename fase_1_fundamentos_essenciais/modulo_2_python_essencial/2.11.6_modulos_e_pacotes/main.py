from utils.cauculos import soma, subtracao
from utils.validadores import eh_email_valido, eh_par

if __name__ == "__main__":
    print(soma(15, 10))
    print(subtracao(15, 10))

    print(eh_par(10))
    print(eh_par(11))

    print(eh_email_valido("teste@exemplo.com"))
    print(eh_email_valido("teste.com"))
