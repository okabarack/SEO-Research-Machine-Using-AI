import openai

# Replace with your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

def get_keyword_suggestions(seed_keyword, num_suggestions=10):
    prompt = f"Generate {num_suggestions} keyword suggestions related to '{seed_keyword}' for SEO purposes."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    
    suggestions = response.choices[0].text.strip().split("\n")
    return [s.strip() for s in suggestions if s.strip()]

def main():
    seed_keyword = input("Enter a seed keyword: ")
    num_suggestions = int(input("Enter the number of keyword suggestions you want: "))
    
    suggestions = get_keyword_suggestions(seed_keyword, num_suggestions)
    
    print("\nKeyword Suggestions:")
    for idx, suggestion in enumerate(suggestions, start=1):
        print(f"{idx}. {suggestion}")

if __name__ == "__main__":
    main()
  
