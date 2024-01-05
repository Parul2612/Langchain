from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = ChatGoogleGenerativeAI(model = "gemini-pro")

    prompt_template_name = PromptTemplate(
        input_variables = ['animal_type', 'pet_color'],
        template= "I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet. One name must be in marathi and one name must be in hindi language. Give one name funny."
    )
    name_chain = LLMChain(llm = llm, prompt = prompt_template_name, output_key= "pet_name")
    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color })
    return response

if __name__ == "__main__":
    print(generate_pet_name("cat", "orange"))
