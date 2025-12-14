# Seamless LLM Integration with Envoy Proxy and SAP AI Core

This series shows how to access foundation models hosted on SAP AI Core through a lightweight Envoy Proxy, so you can keep using familiar, native SDKs and unlock broader integration possibilities.

SAP AI Core exposes models from multiple LLM providers, but its REST APIs don’t map 1-to-1 with most vendor SDKs. By inserting Envoy, we translate those calls automatically.

## [Part 1: Connecting to OpenAI models](https://blog.romk.eu/posts/envoy-aicore/openai/)

- Route OpenAI SDK traffic through Envoy to SAP AI Core
- Generate text with GPT and images with DALL-E
- Plug everything into [LibreChat](https://www.librechat.ai/) in under five minutes
