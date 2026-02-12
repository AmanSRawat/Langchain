from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate the notes from the following text \n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Generate the 5 short questions answers from the following text \n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template= 'Merge the following notes and questions answers into a single text \n Notes: {notes} \n Quiz: {quiz}',
    input_variables= ['notes', 'quiz']
)

model = ChatGroq(model='meta-llama/llama-4-scout-17b-16e-instruct')

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model | parser,
    'quiz': prompt2 | model | parser
})

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain

text = """"A black hole is one of the most extreme and fascinating phenomena in the universe. It is a region of space where gravity is so intense that nothing—not even light—has enough energy to escape its pull.
+1

To understand a black hole, it helps to break it down into its physical structure, how it forms, and how it affects the fabric of reality.

1. The Anatomy of a Black Hole
A black hole isn't just a "hole"; it is a physical object with a specific structure.

The Singularity: At the very center lies the singularity. This is a point of near-infinite density where a massive amount of matter has been crushed into an infinitesimal space. Here, our current laws of physics (General Relativity) break down.
+1

The Event Horizon: This is the "point of no return." It is the spherical boundary surrounding the singularity. Once any object crosses this threshold, the escape velocity required exceeds the speed of light.

The Accretion Disk: Many black holes are surrounded by a swirling disk of gas, dust, and stars being pulled inward. Friction and gravity heat this material to millions of degrees, causing it to glow brightly in X-rays and visible light.
+1

Relativistic Jets: Some supermassive black holes blast beams of ionized matter out from their poles at nearly the speed of light.

2. How Black Holes Form
Black holes are usually the "corpses" of massive stars. The process generally follows these steps:

Stellar Equilibrium: A massive star (at least 10–20 times the mass of our Sun) stays alive by balancing the outward pressure of nuclear fusion with the inward pull of its own gravity.

Iron Dead-End: Once the star begins creating iron in its core, fusion stops producing energy. Gravity suddenly wins the "tug-of-war."

Supernova: The star collapses in seconds, and the outer layers are blasted away in a massive explosion called a supernova.

Gravitational Collapse: If the remaining core is dense enough, no force in nature can stop it from collapsing further until it becomes a black hole.

3. The Warping of Spacetime
According to Albert Einstein’s General Theory of Relativity, gravity isn't just a force; it’s the warping of the "fabric" of spacetime.

Imagine placing a bowling ball on a trampoline; it creates a dip. A black hole is like placing an infinitely heavy marble on that trampoline—it creates a "bottomless" well.

Time Dilation
Because gravity is so strong, time actually slows down near a black hole relative to an outside observer. If you were falling into a black hole, you would feel time passing normally, but an observer watching you from a distance would see you slow down, turn red (due to gravitational redshift), and eventually "freeze" at the event horizon."""

result = chain.invoke({'text': text})

print(result)

chain.get_graph().print_ascii()