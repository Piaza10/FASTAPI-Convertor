import requests
from fastapi import HTTPException
import aiohttp


def sync_converter(from_currency: str, to_currency: str, price: float):
    url = (
    f"https://api.frankfurter.app/latest"
    f"?from={from_currency}"
    f"&to={to_currency}"
    f"&amount={price}"
)
    
    try:
        response = requests.get(url=url)
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)
    
    data = response.json()

    if "rates" not in data:
        raise HTTPException(status_code=400, detail="Rates not in response")

    exchange_rate = data["rates"][to_currency]
    
    return exchange_rate
        
    
async def async_converter(
    from_currency: str,
    to_currency: str,
    price: float
):

    url = (
        f'https://api.frankfurter.app/latest'
        f'?from={from_currency}'
        f'&to={to_currency}'
        f'&amount={price}'
    )

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                data = await response.json()

    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    if "rates" not in data:
        raise HTTPException(
            status_code=400,
            detail="Rates not in response"
        )

    exchange_rate = data["rates"][to_currency]

    return {
        to_currency: exchange_rate
    }



    

    