import aiohttp
from box import Box 
import asyncio
from .errors import *
class Forpy:
    def __init__(self,token,timeout=10):
        self.token = token
        self.timeout = timeout
        self.session = aiohttp.ClientSession()
        self.headers = {
		'TRN-Api-key': token
	}
		
        self.platforms = ['pc','xbl','psn']
        self.baseurl = 'http://api.fortnitetracker.com/v1'
		
        self.player = self.baseurl + '/profile'

    async def close(self):
        await self.session.close()
            
    async def get_player(self,platform,epic_username):
        platform = platform.lower()
        if platform not in self.platforms:
            raise ValueError('Incorrect platform passed.Options: xbl,pc,psn')
		
        try:
            async with self.session.get(f'{self.player}/{platform}/{epic_username}',timeout=self.timeout,headers=self.headers) as resp:
                if resp.status == 200:
					
                    raw_data = await resp.json()
                    if raw_data.get('error'):
					
                        raise NotFound()					
					

                elif 500 > resp.status >400:
                    raise Unauthorized()

                else:
                    raise UnknownError()
        except asyncio.TimeoutError():
            raise NotResponding()

        data = Box(raw_data,camel_killer_box=True)
        player = Player(data,camel_killer_box=True)
        return player 		

    async def get_id(self,platform,epic_username):
        profile = await self.get_player(platform,epic_username)
        return profile.get_id()

    async def get_solos(self,platform,epic_username):
        profile= await self.get_player(platform,epic_username)
        return profile.get_solos()

    async def get_duos(self,platform,epic_username):
        profile=await self.get_player(platform,epic_username)
        return profile.get_duos()
    async def get_squads(self,platform,epic_username):
        profile=await self.get_player(platform,epic_username)
        return profile.get_squads()
    async def get_lifetime_stats(self,platform,epic_username):
        profile=await self.get_player(platform,epic_username)
        return profile.get_lifetime_stats()


class Player(Box):
    async def get_id(self):
        return self.account_id

    async def get_solos(self):
        try:
            return self.stats.p2
        except AttributeError:
            raise NoGames('solos')

    async def get_duos(self):
        try:
            return self.stats.p10
	    
        except AttributeError:
            raise NoGames('solo')

    async def get_squads(self):
        try:
            return self.stats.p9
        except AttributeError:
            raise NoGames('squads')

    async def get_lifetime_stats(self):
        try:
            return self.life_time_stats

        except AttributeError:
            raise NoGames('the game or any of its')







		








