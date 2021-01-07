"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    ano = int(input('Diga um ano:'))
    if ano % 4 == 0 and ano % 100 != 0 or ano %400 == 0:
      print(f'O ano {ano} é bissexto.')
    else:
      print(f'O ano {ano} não é bissexto.')


if __name__ == '__main__':
    main()
