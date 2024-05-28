client = op.new_jm_client()
page = client.search_site('美波瑠のはじめて', page=1)

id_list = []
for aid, atitle in page:
    print(aid, atitle)
    id_list.append(aid)

# 要下载这些aid的本子，调用下面的方法
# download_album(aid)
