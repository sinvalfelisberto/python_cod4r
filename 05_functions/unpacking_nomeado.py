# **kwargs
def resultado_f1(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')


if __name__ == "__main__":
    podium = {'terceiro': 'L. Hamilton',
              'primeiro': 'M. Verstappen', 'segundo': 'S. Vettel'}

    resultado_f1(**podium)
