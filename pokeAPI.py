# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pokeAPI.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jchris <jchris@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/17 08:30:17 by jchris            #+#    #+#              #
#    Updated: 2023/06/17 22:53:27 by jchris           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import requests

url = "https://pokeapi.co/api/v2/pokemon/"

print('ポケモン図鑑 No.:')
# 入力文字を取得
poke_id = input('>> ')

# バリデーションチェック
while True:
    # 範囲は1〜1008 (2023/06 現在)
    if not 0 < int(poke_id) < 1011:
        print('存在しないポケモンIDを入力しています! 再度入力してください: ')
        poke_id = input('>> ')
    else:
        break

# urlに図鑑IDを付与
url = url + poke_id

response = requests.get(url)
response = response.json()

# 名前
name = response['name']
# ID
id = response['id']
# ポケモン画像
image = response['sprites']['other']['official-artwork']['front_default']
# タイプ
types = response['types'][0]['type']['name']

print(image)
