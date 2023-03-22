

def main():

    while True:
        try:
            country = str(input().lower().strip())
            resposta = traduzir(country)
            print(resposta)
        except: 
            break
    
def traduzir(country: str) -> str:
    TRADUTOR = {
    "brasil": "Feliz Natal!",
    "alemanha": "Frohliche Weihnachten!",
    "austria": "Frohe Weihnacht!",
    "coreia": "Chuk Sung Tan!",
    "espanha": "Feliz Navidad!",
    "grecia": "Kala Christougena!",
    "estados-unidos": "Merry Christmas!",
    "inglaterra": "Merry Christmas!",
    "australia": "Merry Christmas!",
    "portugal": "Feliz Natal!",
    "suecia": "God Jul!",
    "turquia": "Mutlu Noeller",
    "argentina": "Feliz Navidad!",
    "chile": "Feliz Navidad!",
    "mexico": "Feliz Navidad!",
    "antardida": "Merry Christmas!",
    "canada": "Merry Christmas!",
    "irlanda": "Nollaig Shona Dhuit!",
    "belgica": "Zalig Kerstfeest!",
    "italia": "Buon Natale!",
    "libia": "Buon Natale!",
    "siria": "Milad Mubarak!",
    "marrocos": "Milad Mubarak!",
    "japao": "Merii Kurisumasu!",
    }

    return TRADUTOR.get(country, "--- NOT FOUND ---")


main()