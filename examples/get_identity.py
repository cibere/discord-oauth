import asyncio

import auth_cord

# creating our authorization object
auth = auth_cord.Authorization(
    client_id=123,
    client_secret="...",
    redirect_url="...",
)

# creating our client instance and passing our authorization
client = auth_cord.Client(authorization=auth)


async def main():
    # starting our client
    async with client:
        # exchanging our code with discord for a token
        token = await client.exchange_code("...")

        # getting the users connections
        user = await client.get_user_info(
            token.token
        )  # 'token' is a 'auth_cord.token.Token' object

        # printing the users id
        print(user.id)


# checking if this file is the one that was run
if __name__ == "__main__":
    # if so, run the main function
    asyncio.run(main())
