from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["paper_title", "style_input", "length_input"],
    template="""
            Please summerize the research paper titled "{paper_title}" with the following specification.
            Style: {style_input}
            Length: {length_input}
            1. Mathematical Details
                - Include relevant equations and formulas.
                - Explain the significance of each mathematical, include the intuative code snippt where required.
            2. Analogies and Examples
                - Use analogies to explain complex concepts.
                - Provide practical examples to illustrate key points.
            If ceration information is not available in the paper, please indicate that clearly.
            Ensure the summary is well-structured and easy to follow.
    """    
)

template.save('template.json')