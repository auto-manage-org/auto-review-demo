import google.generativeai as genai
# Make sure you have your API key configured
# genai.configure(api_key="YOUR_API_KEY")

print("Available Models:")
for m in genai.list_models():
  # Check if the model supports the 'generateContent' method
  if 'generateContent' in m.supported_generation_methods:
    print(f"- {m.name}")
