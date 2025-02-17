import random
from utils import *
from config import *
from scrapper import Scrapper
import asyncio

async def main():
    scrapper = Scrapper(proxy=PROXY)

    with open('wallets.txt', 'r') as f:
        wallets = f.read().splitlines()

    for wallet in wallets:
        wallet_data = await scrapper.poh(wallet)  # Получение данных для кошелька
        print(f'{wallet_data["wallet"]} poh: {wallet_data["poh"]}, sybil: {wallet_data["sybil"]} score: {"✅" if wallet_data["poh"] == True and wallet_data["sybil"] == False else "❌"}')
        
        await asyncio.sleep(random.randint(25, 50))  # Ожидание между кошельками

        # Смена IP
        q = await change_ip(CHANGE_IP_LINK)
        print(f'Changing IP: {q}')

    await bot.session.close()  # Закрываем сессию бота после завершения обработки всех кошельков
    print("Обработка завершена, сессия бота закрыта.")

if __name__ == '__main__':
    asyncio.run(main())
