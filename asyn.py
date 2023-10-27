import asyncio
from flask import Flask

app = Flask(__name__)

# An asynchronous route that sleeps for 5 seconds
@app.route('/async', methods=['GET'])
async def async_route():
    await asyncio.sleep(5)
    return "Async route completed"

if __name__ == '__main__':
    app.run()


# 500 err-flask with aiohttp is not working