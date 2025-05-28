n_titan, vida_fixo = map(int, input().split())
ordem_titans_texto = input()
p_titan, m_titan, g_titan = map(int, input().split())


damage_map = {'P': p_titan, 'M': m_titan, 'G': g_titan}
ordem_titans = [damage_map[char] for char in ordem_titans_texto]
n_muralhas = 1
vida = vida_fixo

len = len(ordem_titans)

for i in range(len):
    dano_i = ordem_titans[i-1]
    # print(dano_i)
    # print(vida)
    if dano_i < vida:
        vida -= dano_i
    elif dano_i > vida:
        n_muralhas += 1
        vida = vida_fixo
        ordem_titans.insert(dano_i, i)
    else:
        n_muralhas += 1
        vida = vida_fixo

print(n_muralhas)


        # print(f'Titan {ordem_titans_texto[i]} causes {dano_i} to \'vida\', that now is {vida}')
        # print(ordem_titans)
        # print(f'Titan {ordem_titans_texto[i]}, with {dano_i} passes muralha {n_muralhas - 1}')
        # print(f'Titan {ordem_titans_texto[i]}, with {dano_i} passes muralha {n_muralhas - 1}, but dies')