from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """"
An in memory rate limiter based on a token bucket algorithm.

This is an in memory rate limiter, so it cannot rate limit across different processes.

The rate limiter only allows time-based rate limiting and does not take into account any information about the input or the output, so it cannot be used to rate limit based on the size of the request.

It is thread safe and can be used in either a sync or async context.

The in memory rate limiter is based on a token bucket. The bucket is filled with tokens at a given rate. Each request consumes a token. If there are not enough tokens in the bucket, the request is blocked until there are enough tokens.

These tokens have nothing to do with LLM tokens. They are just a way to keep track of how many requests can be made at a given time.

Current limitations:

The rate limiter is not designed to work across different processes. It is an in-memory rate limiter, but it is thread safe.
The rate limiter only supports time-based rate limiting. It does not take into account the size of the request or any other factors.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
)

chunks = splitter.split_text(text=text)

print(len(chunks))

print(chunks)