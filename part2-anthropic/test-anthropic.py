from anthropic import AnthropicBedrock

client = AnthropicBedrock()

response = client.messages.create(
    model="d7ed726e32394096",
    max_tokens=1024,
    tools=[
        {
            "type": "bash_20250124",
            "name": "bash"
        }
    ],
    messages=[
        {"role": "user", "content": "List all Python files in the current directory."}
    ]
)
print(response.content)
