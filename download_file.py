# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    download_file.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jchris <jchris@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/17 22:53:34 by jchris            #+#    #+#              #
#    Updated: 2023/06/17 22:53:34 by jchris           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import urllib.error
import urllib.request


def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)


for i in range(1009, 1020):
    url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{i}.png'
    dst_path = f'images/{i}.png'
    download_file(url, dst_path)
