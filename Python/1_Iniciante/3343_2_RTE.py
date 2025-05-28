import math

n_titan, vida = map(int, input().split())
ordem_titans_texto = input()
p_titan, m_titan, g_titan = map(int, input().split())

damage_map = {'P': p_titan, 'M': m_titan, 'G': g_titan}

ordem_titans = [damage_map[char] for char in ordem_titans_texto]
soma_dano = 0
muralhas_antes = 1
i = 0

while i < len(ordem_titans):
    dano_i = ordem_titans[i]

    soma_dano += dano_i
    muralhas_atual = math.ceil(soma_dano/vida)

    if muralhas_antes != muralhas_atual and ((soma_dano-dano_i)%vida) != 0:
        soma_dano = muralhas_antes*vida

        ordem_titans.insert(i, dano_i)

    muralhas_antes = muralhas_atual
    i+=1

print(muralhas_atual)
