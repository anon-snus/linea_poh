import asyncio

from utils import async_get, change_ip

class Scrapper:
	def __init__(self, proxy):
		self.proxy = proxy

	async def poh(self, wallet:str):
		url = f'https://linea-xp-poh-api.linea.build/poh/{wallet}'

		for i in range(5):
			try:
				res = await async_get(url, self.proxy)
				poh = res.get('poh')
				sybil = res.get('isFlagged')
				return {'wallet': wallet, 'poh': poh, 'sybil': sybil}

			except Exception as e:
				print(e)
				await asyncio.sleep(1)


