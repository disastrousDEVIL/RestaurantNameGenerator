import os  # Need to import os for setting environment variables

from langchain_community.llms import OpenAI
from secretkey import OPENAI_API_KEY
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain  # Combine imports for readability

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# Initialize OpenAI LLM instance
llm = OpenAI(temperature=0.6)

# Define function to generate restaurant name and menu items
def generate(cuisine):
    # Define prompt template for restaurant name suggestion
    restaurant = PromptTemplate(
        input_variables=['cuisine'],
        template='I want to open a restaurant for {cuisine} food. Suggest a fancy name for it'
    )
    name_chain = LLMChain(llm=llm, prompt=restaurant, output_key='restaurant_name')
    # Define prompt template for menu items suggestion
    items = PromptTemplate(
        input_variables=['restaurant_name'],
        template='suggest 10 MENU items for the {restaurant_name}'
    )
    items_chain = LLMChain(llm=llm, prompt=items, output_key='items_list')

    # Define sequential chain for main process
    main_chain = SequentialChain(
        chains=[name_chain, items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'items_list']
    )

    # Generate response using the chains
    response = main_chain({'cuisine': cuisine})
    return response


