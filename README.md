# HuggingFace - Summarizer

It is a docker based REST API to summarize texts.

## Setup

Install Docker Make sure Docker is installed and running on your machine. You can verify with:

```sh
docker --version
```

Build and run:

```sh
sh run.sh
```

## Usage

**Request**

```sh
curl --location 'http://127.0.0.1:8000/summarize' \
--header 'Content-Type: application/json' \
--data '{"text": "Wikipedia gained early contributors from Nupedia, Slashdot postings, and web search engine indexing. Language editions were created beginning in March 2001, with a total of 161 in use by the end of 2004.[W 8][W 9] Nupedia and Wikipedia coexisted until the former'\''s servers were taken down permanently in 2003, and its text was incorporated into Wikipedia. The English Wikipedia passed the mark of 2 million articles on September 9, 2007, making it the largest encyclopedia ever assembled, surpassing the Yongle Encyclopedia made in China during the Ming dynasty in 1408, which had held the record for almost 600 years."}'
```

**Response**

```json
{
  "summary": " The English Wikipedia passed the mark of 2 million articles on September 9, 2007, making it the largest encyclopedia ever assembled . Nupedia and Wikipedia coexisted until the former's servers were taken down permanently in 2003, and its text"
}
```
