import os
import openai


class OpenAIClient:
    def _init_(self):
        self.client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    def send_prompt(self, **kwargs):
        prompt_in_kwargs = "prompt" in kwargs
        messages_in_kwargs = "messages" in kwargs
        assert not (messages_in_kwargs and prompt_in_kwargs)
        assert messages_in_kwargs or prompt_in_kwargs
        assert "model" in kwargs

        if prompt_in_kwargs:
            kwargs["messages"] = [
                {
                    "role": "user",
                    "content": kwargs.pop("prompt"),
                }
            ]

        # Always use responses API for all models
        messages = kwargs.pop("messages")
        
        # Extract the content from messages - assuming single user message for simplicity
        # In a more complex scenario, we might need to handle multiple messages
        input_content = None
        for msg in messages:
            if msg.get("role") == "user":
                input_content = msg.get("content")
                break
        
        if not input_content:
            raise ValueError("No user message found in messages")
        
        # Create request body for responses API
        response_kwargs = {
            "model": kwargs["model"],
            "input": input_content
        }
        
        # Copy over other parameters that are supported by responses API
        if "temperature" in kwargs:
            response_kwargs["temperature"] = kwargs["temperature"]
        if "max_tokens" in kwargs:
            response_kwargs["max_output_tokens"] = kwargs["max_tokens"]
        if "top_p" in kwargs:
            response_kwargs["top_p"] = kwargs["top_p"]
        
        # Add reasoning effort support
        if "reasoning_effort" in kwargs:
            response_kwargs["reasoning"] = {"effort": kwargs["reasoning_effort"]}
        elif "reasoning" in kwargs:
            # Allow passing the full reasoning object
            response_kwargs["reasoning"] = kwargs["reasoning"]
        
        # Use the official OpenAI SDK responses.create() method
        response = self.client.responses.create(**response_kwargs)
        
        # The SDK provides a convenient output_text property that aggregates all text outputs
        # This is the simple, direct way to get the text output
        return response.output_text