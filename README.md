![](https://static.coindesk.com/wp-content/uploads/2021/02/musk-doge-1200x628.png)

Random idea: let's buy cryptocurrencies if an influencer tweets positively about them

## Motivation

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">🎶 Who let the Doge out 🎶</p>&mdash; Elon Musk (@elonmusk) <a href="https://twitter.com/elonmusk/status/1358542364948668418?ref_src=twsrc%5Etfw">February 7, 2021</a></blockquote>

After this tweet, the price of $DOGE increased by roughly 10%.

## Features

A few things this program will take care of:
- Fetching up to date tweets from specified influencers and filter them based on keywords
- Run sentiment analysis on the specified influencers tweets
- Automatically place a customized trade via Binance

## Usage

This program makes use of several different APIs to perform various tasks.

- [Binance](https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md)
- [Twitter](https://developer.twitter.com/)
- [Google Cloud Platform](https://cloud.google.com/)

You must have the following environment variables set in order to run the CLI:

```
BINANCE_API_KEY=
BINANCE_SECRET_KEY=
TWITTER_API_TOKEN=
GOOGLE_APPLICATION_CREDENTIALS=
```

Once these are all set up, you can simply run the following command and let the program run in the background:
```bash
$ python3 deft --run &
```

## Configuration

You must edit the `config.json` file to suit your needs, here is what a sample config file looks like:
```json
{
    "twitter": {
        "accounts": ["elonmusk", "jack"]
    },
    "currencies": {
        "dogecoin": {
            "symbol": "DOGEBUSD",
            "quantity": "100",
            "limitPrice": "0.08",
            "keywords": ["DOGE", "Dogecoin"]
        },
        "ethereum": {
            "symbol": "ETHBUSD",
            "quantity": "0.1",
            "limitPrice": "1800",
            "keywords": ["ETH", "Ethereum"]
        }
    }
}
```
